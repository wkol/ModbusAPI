from datetime import datetime
from typing import List
from fastapi import Depends, HTTPException, APIRouter, Security
from starlette.status import HTTP_403_FORBIDDEN
from .schemas import Reading
from .services import crud
from fastapi.security.api_key import APIKeyHeader, APIKey
from pydantic import parse_obj_as
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


@router.post('/readings/')
async def create_reading(read: crud.Read,
                         api_key: APIKey = Depends(get_api_key)
                         ):
    reading_id = await crud.add_reading(read=read)
    return {"id": reading_id,
            "date": read.date,
            "voltage_13": read.values[0],
            "voltage_12": read.values[1],
            "voltage_23": read.values[2],
            "current_l1": read.values[3],
            "current_l2": read.values[4],
            "current_l3": read.values[5],
            "total_power": read.values[6],
            "total_reactive_power": read.values[7],
            "total_apparent_power": read.values[8],
            "frequency": read.values[9],
            "total_cos": read.values[10],
            "current_n": read.values[11],
            "input_EA": read.values[12],
            "input_EA_MSB": read.values[13],
            "return_EA": read.values[14],
            "return_EA_MSB": read.values[15],
            "ind_EQ": read.values[16],
            "ind_EQ_MSB": read.values[17],
            "cap_EQ": read.values[18],
            "cap_EQ_MSB": read.values[19],
            "voltage_l1": read.values[20],
            "voltage_l2": read.values[21],
            "voltage_l3": read.values[22],
            "power_l1": read.values[23],
            "power_l2": read.values[24],
            "power_l3": read.values[25],
            "reactive_power_l1": read.values[26],
            "reactive_power_l2": read.values[27],
            "reactive_power_l3": read.values[28],
            "cos_l1": read.values[29],
            "cos_l2": read.values[30],
            "cos_l3": read.values[31]
            }


@router.get('/readings/{reading_id}/', response_model=Reading)
async def read_reading(reading_id: int):
    reading = await crud.get_reading(reading_id=reading_id)
    return reading


@router.get('/readings_last/', response_model=Reading)
async def read_last_reading():
    reading = await crud.get_last_reading()
    if reading is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return reading


@router.get('/readings/', response_model=List[Reading])
async def read_readings():
    readings = await crud.get_readings()
    if readings is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return readings


@router.get('/readings/date')
async def read_readings_by_date(date: str):
    formatted_date = datetime.fromisoformat(date)
    readings = await crud.get_reading_by_date(reading_date=formatted_date)
    if readings is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return readings


@router.get('/readings/period')
async def read_readings_between(dates: PeriodDependency = Depends(PeriodDependency)):
    readings = await crud.get_reading_by_dates(dates.from_date, dates.to_date)
    if readings is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return readings


@router.delete('/readings/{reading_id}')
async def delete_reading(reading_id: int,
                         api_key: APIKey = Depends(get_api_key)
                         ):
    reading = await crud.delete_reading(reading_id=reading_id)
    # if not reading:
    #     raise HTTPException(status_code=404, detail="Reading not found")
    return reading


@router.get('/readings_chart')
async def read_chart_readings():
    readings = await crud.get_readings()
    if readings is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return readings[::10]
