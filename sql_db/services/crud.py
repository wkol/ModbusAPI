from sqlalchemy import func
from datetime import datetime
from ..database import database, readings
from pydantic import BaseModel
from typing import List
from math import inf
from logging import warning


class Read(BaseModel):
    date: str
    values: List[float]


def post_data_validation(read: Read):
    try:
        datetime.fromisoformat(read.date)
    except ValueError:
        warning(f'Invalid ISO format date - {read.date}')
        return False
    if len(read.values) != 52:
        warning(f'Not enough values passed - {len(read.values)}. Must be 52')
        return False
    for value in read.values:
        if value == inf or value == -inf:
            warning(f'Invalid value (is infinity) in the reading - {value}')
            return False
        elif value is None:
            warning('Invalid value (is Null/None)')
            return False


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


async def get_readings_chart(id: int):
    query = readings.select.where(readings.c.id > id)
    return await database.fetch_all(query=query)


async def add_reading(read: Read):
    query = readings.insert().values(date=datetime.fromisoformat(read.date),
                                     total_power=read.values[0],
                                     total_reactive_power=read.values[1],
                                     total_apparent_power=read.values[2],
                                     power_l1=read.values[3],
                                     power_l2=read.values[4],
                                     power_l3=read.values[5],
                                     reactive_power_l1=read.values[6],
                                     reactive_power_l2=read.values[7],
                                     reactive_power_l3=read.values[8],
                                     voltage_13=read.values[9],
                                     voltage_12=read.values[10],
                                     voltage_23=read.values[11],
                                     voltage_l1=read.values[12],
                                     voltage_l2=read.values[13],
                                     voltage_l3=read.values[14],
                                     current_l1=read.values[15],
                                     current_l2=read.values[16],
                                     current_l3=read.values[17],
                                     current_n=read.values[18],
                                     frequency=read.values[19],
                                     total_cos=read.values[20],
                                     cos_l1=read.values[21],
                                     cos_l2=read.values[22],
                                     cos_l3=read.values[23],
                                     input_EA=read.values[24],
                                     return_EA=read.values[25],
                                     ind_EQ=read.values[26],
                                     cap_EQ=read.values[27],
                                     power_DC=read.values[30],
                                     voltage_DC=read.values[31],
                                     current_DC=read.values[32],
                                     power_inv=read.values[33],
                                     reactive_power_inv=read.values[34],
                                     apparent_power_inv=read.values[35],
                                     voltage_UAB_inv=read.values[36],
                                     voltage_UBC_inv=read.values[37],
                                     voltage_UCA_inv=read.values[38],
                                     voltage_UA_inv=read.values[39],
                                     voltage_UB_inv=read.values[40],
                                     voltage_UC_inv=read.values[41],
                                     current_A_inv=read.values[42],
                                     current_B_inv=read.values[43],
                                     current_C_inv=read.values[44],
                                     current_avg_inv=read.values[45],
                                     frequency_inv=read.values[46],
                                     cos_inv=read.values[47],
                                     heat_sink_temp_inv=read.values[48],
                                     energy=read.values[49],
                                     state_1_inv=read.values[51],
                                     state_2_inv=read.values[52],
                                     )

    return await database.execute(query=query)
