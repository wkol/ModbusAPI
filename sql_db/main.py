from typing import List
from datetime import datetime

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


@app.post('/readings/', response_model=schemaReading.Reading)
def create_reading(date: int, values: List[float],
                   db: Session = Depends(get_db),
                   api_key: APIKey = Depends(get_api_key)
                   ):
    formated_date = datetime.fromtimestamp(date)
    return crud.add_reading(db=db, date=formated_date, values=values)


@app.get('/readings/', response_model=List[schemaReading.Reading])
def read_readings(db: Session = Depends(get_db)):
    readings = crud.get_readings(db=db)
    return readings


@app.get('/readings/{date}/', response_model=List[schemaReading.Reading])
def read_readings_by_date(timestamp: int, db: Session = Depends(get_db)):
    formatted_date = datetime.fromtimestamp(timestamp)
    readings = crud.get_reading_by_date(db=db, reading_date=formatted_date)
    if readings is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return readings


@app.get('readings/{time}/', response_model=List[schemaReading.Reading])
def read_readings_between(time1: int, time2: int,
                          db: Session = Depends(get_db)
                          ):
    formatted_date1 = datetime.fromtimestamp(time1)
    formatted_date2 = datetime.fromtimestamp(time2)
    readings = crud.get_reading_by_dates(db, formatted_date1, formatted_date2)
    if readings is None:
        raise HTTPException(status_code=404, detail="Readings not found")
    return readings
