from sqlalchemy import Column, Integer, DateTime, Float
import datetime
from ..database import Base


class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow())
    voltage_13 = Column(Float)
    voltage_12 = Column(Float)
    voltage_23 = Column(Float)
    current_l1 = Column(Float)
    current_l2 = Column(Float)
    current_l3 = Column(Float)
    total_power = Column(Float)
    total_reactive_power = Column(Float)
    total_apparent_power = Column(Float)
    frequency = Column(Float)
    total_cos = Column(Float)
    current_n = Column(Float)
    input_EA = Column(Float)
    input_EA_MSB = Column(Float)
    return_EA = Column(Float)
    return_EA_MSB = Column(Float)
    ind_EQ = Column(Float)
    ind_EQ_MSB = Column(Float)
    cap_EQ = Column(Float)
    cap_EQ_MSB = Column(Float)
    voltage_l1 = Column(Float)
    voltage_l2 = Column(Float)
    voltage_l3 = Column(Float)
    power_l1 = Column(Float)
    power_l2 = Column(Float)
    power_l3 = Column(Float)
    reactive_power_l1 = Column(Float)
    reactive_power_l2 = Column(Float)
    reactive_power_l3 = Column(Float)
    cos_l1 = Column(Float)
    cos_l2 = Column(Float)
    cos_l3 = Column(Float)
