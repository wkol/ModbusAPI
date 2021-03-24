from typing import List
from datetime import datetime
from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException, Security
from sqlalchemy.orm import Session
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN

from .models import readings as modelReading
from .schemas import readings as schemaReading
from .database import SessionLocal, engine
from .services import crud

API_KEY = "2367449623"
API_KEY_NAME = "post_token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

modelReading.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Read(BaseModel):
    date: str
    values: List[float]


def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN,
                            detail="Could not validate credentials"
                            )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PeriodDependency:
    def __init__(self, from_date: str, to_date: str):
        self.from_date = datetime.fromisoformat(from_date)
        self.to_date = datetime.fromisoformat(to_date)


@app.post('/readings/', response_model=schemaReading.Reading)
def create_reading(read: Read,
                   db: Session = Depends(get_db),
                   api_key: APIKey = Depends(get_api_key)
                   ):
    formated_date = datetime.fromisoformat(read.date)
    return crud.add_reading(db=db, date=formated_date, values=read.values)


@app.get('/readings/{reading_id}/', response_model=schemaReading.Reading)
def read_reading(reading_id: int, db: Session = Depends(get_db)):
    reading = crud.get_reading(db=db, reading_id=reading_id)
    return reading


@app.get('/readings_last/', response_model=schemaReading.Reading)
def read_last_reading(db: Session = Depends(get_db)):
    reading = crud.get_last_reading(db)
    return reading


@app.get('/readings/', response_model=List[schemaReading.Reading])
def read_readings(db: Session = Depends(get_db)):
    readings = crud.get_readings(db=db)
    return readings


@app.get('/readings/date', response_model=List[schemaReading.Reading])
def read_readings_by_date(date: str, db: Session = Depends(get_db)):
    formatted_date = datetime.fromisoformat(date)
    readings = crud.get_reading_by_date(db=db, reading_date=formatted_date)
    if readings is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return readings


@app.get('/readings/period', response_model=List[schemaReading.Reading])
def read_readings_between(dates: PeriodDependency = Depends(PeriodDependency),
                          db: Session = Depends(get_db)):
    readings = crud.get_reading_by_dates(db, dates.from_date, dates.to_date)
    if readings is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return readings


@app.delete('/readings/{reading_id}', response_model=schemaReading.Reading)
def delete_reading(reading_id: int, 
                   db: Session = Depends(get_db),
                   api_key: APIKey = Depends(get_api_key)
                   ):
    db_reading = crud.delete_reading(db=db, reading_id=reading_id)
    if not db_reading:
        raise HTTPException(status_code=404, detail="Reading not found")
@app.get('/readings_chart', response_model=List[schemaReading.Reading])
async def read_chart_readings(db: Session = Depends(get_db)):
    readings = crud.get_readings(db)
    if readings is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return await readings[::10]
