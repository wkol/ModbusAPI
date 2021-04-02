from sqlalchemy import func
from datetime import datetime
from ..database import database, readings
from pydantic import BaseModel
from typing import List


class Read(BaseModel):
    date: str
    values: List[float]


async def get_reading(reading_id: int):
    query = readings.select().where(reading_id == readings.c.id)
    return await database.fetch_one(query=query)


async def get_reading_by_date(reading_date: datetime):
    query = readings.select().where(reading_date.date() ==\
                                    func.DATE(readings.c.date))
    return await database.fetch_all(query=query)


async def get_reading_by_dates(start_date: datetime,
                               end_date: datetime
                               ):
    query = readings.select().where(func.DATE(start_date) < func.DATE(readings.c.date))
    return await database.fetch_all(query=query)


async def get_readings():
    query = readings.select()
    return await database.fetch_all(query=query)


async def delete_reading(reading_id: int):
    query = readings.delete().where(reading_id == readings.c.id)
    await database.execute(query)
    return {'msg': f'Reading with id {reading_id} deleted'}


async def get_last_reading():
    query = readings.select().order_by(readings.c.id.desc()).limit(1)
    return await database.fetch_one(query=query)


async def add_reading(read: Read):
    query = readings.insert().values(date=datetime.fromisoformat(read.date),
                                     voltage_13=read.values[0],
                                     voltage_12=read.values[1],
                                     voltage_23=read.values[2],
                                     current_l1=read.values[3],
                                     current_l2=read.values[4],
                                     current_l3=read.values[5],
                                     total_power=read.values[6],
                                     total_reactive_power=read.values[7],
                                     total_apparent_power=read.values[8],
                                     frequency=read.values[9],
                                     total_cos=read.values[10],
                                     current_n=read.values[11],
                                     input_EA=read.values[12],
                                     input_EA_MSB=read.values[13],
                                     return_EA=read.values[14],
                                     return_EA_MSB=read.values[15],
                                     ind_EQ=read.values[16],
                                     ind_EQ_MSB=read.values[17],
                                     cap_EQ=read.values[18],
                                     cap_EQ_MSB=read.values[19],
                                     voltage_l1=read.values[20],
                                     voltage_l2=read.values[21],
                                     voltage_l3=read.values[22],
                                     power_l1=read.values[23],
                                     power_l2=read.values[24],
                                     power_l3=read.values[25],
                                     reactive_power_l1=read.values[26],
                                     reactive_power_l2=read.values[27],
                                     reactive_power_l3=read.values[28],
                                     cos_l1=read.values[29],
                                     cos_l2=read.values[30],
                                     cos_l3=read.values[31]
                                     )

    return await database.execute(query=query)
