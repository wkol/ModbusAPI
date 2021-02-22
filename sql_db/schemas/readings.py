from datetime import datetime
from pydantic import BaseModel


class ReadingBase(BaseModel):
    date: datetime
    voltage_13: float
    voltage_12: float
    voltage_23: float
    current_l1: float
    current_l2: float
    current_l3: float
    total_power: float
    total_reactive_power: float
    total_apparent_power: float
    frequency: float
    total_cos: float
    current_n: float
    input_EA: float
    input_EA_MSB: float
    return_EA: float
    return_EA_MSB: float
    ind_EQ: float
    ind_EQ_MSB: float
    cap_EQ: float
    cap_EQ_MSB: float
    voltage_l1: float
    voltage_l2: float
    voltage_l3: float
    power_l1: float
    power_l2: float
    power_l3: float
    reactive_power_l1: float
    reactive_power_l2: float
    reactive_power_l3: float
    cos_l1: float
    cos_l2: float
    cos_l3: float


class Reading(ReadingBase):
    id: int

    class Config:
        orm_mode = True


class ReadingCreate(ReadingBase):
    pass
