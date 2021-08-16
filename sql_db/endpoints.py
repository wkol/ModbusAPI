from datetime import datetime
from typing import List
from fastapi import Depends, HTTPException, APIRouter, Security
from starlette.status import HTTP_403_FORBIDDEN, HTTP_422_UNPROCESSABLE_ENTITY
from .schemas import Reading
from .services import crud
from fastapi.security.api_key import APIKeyHeader, APIKey


API_KEY = "2367449623"
API_KEY_NAME = "post_token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

router = APIRouter()


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN,
                            detail="Could not validate credentials"
                            )


class PeriodDependency:
    def __init__(self, from_date: str, to_date: str):
        self.from_date = datetime.fromisoformat(from_date)
        self.to_date = datetime.fromisoformat(to_date)


@router.post('/readings/', response_model=Reading)
async def create_reading(read: crud.Read,
                         api_key: APIKey = Depends(get_api_key)
                         ):
    if not crud.post_data_validation(read):
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Invalid reading's values")
    await crud.add_reading(read=read)
    return await crud.get_last_reading()


@router.get('/readings/{reading_id}/', response_model=Reading)
async def read_reading(reading_id: int):
    reading = await crud.get_reading(reading_id=reading_id)
    return reading


@router.get('/readings_last/', response_model=Reading)
async def read_last_reading():
    reading = await crud.get_last_reading()
    if reading is None:
        raise HTTPException(status_code=404, detail='Readings not found')
    return reading


@router.get('/readings/', response_model=List[Reading])
async def read_readings():
    readings = await crud.get_readings()
    if readings is None:
        raise HTTPException(status_code=404, detail='Readings not found')
    return readings


@router.get('/readings/date', response_model=List[Reading])
async def read_readings_by_date(date: str):
    formatted_date = datetime.fromisoformat(date)
    readings = await crud.get_reading_by_date(reading_date=formatted_date)
    if readings is None:
        raise HTTPException(status_code=404, detail='Readings not found')
    return readings


@router.get('/readings/period', response_model=List[Reading])
async def read_readings_between(dates: PeriodDependency = Depends(PeriodDependency)):
    readings = await crud.get_reading_by_dates(dates.from_date, dates.to_date)
    if readings is None:
        raise HTTPException(status_code=404, detail='Readings not found')
    return readings


@router.delete('/readings/{reading_id}')
async def delete_reading(reading_id: int,
                         api_key: APIKey = Depends(get_api_key)
                         ):
    reading = await crud.delete_reading(reading_id=reading_id)
    return reading


@router.get('/readings_chart', response_model=List[Dict])
async def read_chart_readings(name: str, dates: PeriodDependency = Depends(PeriodDependency)):
    try:
        readings = await crud.get_readings_chart(dates.from_date, dates.to_date, name)
    except KeyError:
        raise HTTPException(status_code=404, detail='Invalid value name')
    if readings is None:
        raise HTTPException(status_code=404, detail='Readings not found')
    return readings[::60]
