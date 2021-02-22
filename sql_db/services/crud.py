from sqlalchemy.orm import Session
from ..models import readings as modelReading
from datetime import datetime
from typing import List


def get_reading(db: Session, reading_id: int):
    return db.query(modelReading.Reading).\
        filter(modelReading.Reading.id == reading_id).first()


def get_reading_by_date(db: Session, reading_date: datetime):
    return db.query(modelReading.Reading).\
        filter(modelReading.Reading.date == reading_date).all()


def get_reading_by_dates(db: Session, start_date: datetime,
                         end_date: datetime
                         ):
    return db.query(modelReading.Reading).\
        filter((modelReading.Reading.date > start_date) &
               (end_date > modelReading.Reading.date)).all()


def get_readings(db: Session):
    return db.query(modelReading.Reading).all()


def add_reading(db: Session, date: datetime, values: List[float]):
    db_reading = modelReading.Reading(date=date, voltage_13=values[0],
                                      voltage_12=values[1],
                                      voltage_23=values[2],
                                      current_l1=values[3],
                                      current_l2=values[4],
                                      current_l3=values[5],
                                      total_power=values[6],
                                      total_reactive_power=values[7],
                                      total_apparent_power=values[8],
                                      frequency=values[9],
                                      total_cos=values[10],
                                      current_n=values[11],
                                      input_EA=values[12],
                                      input_EA_MSB=values[13],
                                      return_EA=values[14],
                                      return_EA_MSB=values[15],
                                      ind_EQ=values[16],
                                      ind_EQ_MSB=values[17],
                                      cap_EQ=values[18],
                                      cap_EQ_MSB=values[19],
                                      voltage_l1=values[20],
                                      voltage_l2=values[21],
                                      voltage_l3=values[22],
                                      power_l1=values[23],
                                      power_l2=values[24],
                                      power_l3=values[25],
                                      reactive_power_l1=values[26],
                                      reactive_power_l2=values[27],
                                      reactive_power_l3=values[28],
                                      cos_l1=values[29],
                                      cos_l2=values[30],
                                      cos_l3=values[31],
                                      )
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading
