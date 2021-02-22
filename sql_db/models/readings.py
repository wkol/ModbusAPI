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
