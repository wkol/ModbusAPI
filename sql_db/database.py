from sqlalchemy import (Column, DateTime, Integer, MetaData, Float, Table,
                        create_engine)
from databases import Database
import datetime

DATABASE_URL = "postgresql://modbus:solar@localhost/modbuserver"

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
readings = Table('readings',
                 metadata,
                 Column('date', DateTime,
                        default=datetime.datetime.utcnow()
                        ),
                 Column('voltage_13', Float),
                 Column('voltage_12', Float),
                 Column('voltage_23', Float),
                 Column('current_l1', Float),
                 Column('current_l2', Float),
                 Column('current_l3', Float),
                 Column('total_power', Float),
                 Column('total_reactive_power', Float),
                 Column('total_apparent_power', Float),
                 Column('frequency', Float),
                 Column('total_cos', Float),
                 Column('current_n', Float),
                 Column('input_EA', Float),
                 Column('input_EA_MSB', Float),
                 Column('return_EA', Float),
                 Column('return_EA_MSB', Float),
                 Column('ind_EQ', Float),
                 Column('ind_EQ_MSB', Float),
                 Column('cap_EQ', Float),
                 Column('cap_EQ_MSB', Float),
                 Column('voltage_l1', Float),
                 Column('voltage_l2', Float),
                 Column('voltage_l3', Float),
                 Column('power_l1', Float),
                 Column('power_l2', Float),
                 Column('power_l3', Float),
                 Column('reactive_power_l1', Float),
                 Column('reactive_power_l2', Float),
                 Column('reactive_power_l3', Float),
                 Column('cos_l1', Float),
                 Column('cos_l2', Float),
                 Column('cos_l3', Float),
                 Column('id', Integer, primary_key=True, index=True),
                 )

database = Database(DATABASE_URL)
