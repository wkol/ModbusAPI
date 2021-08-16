from sqlalchemy import (Column, DateTime, Integer, MetaData, Float, Table,
                        create_engine)
from databases import Database
import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
readings = Table('readings',
                 metadata,
                 Column('id', Integer, primary_key=True, index=True),
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
                 Column('input_ea', Float),
                 Column('return_ea', Float),
                 Column('ind_eq', Float),
                 Column('cap_eq', Float),
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
                 Column('power_dc', Float),
                 Column('voltage_dc', Float),
                 Column('current_dc', Float),
                 Column('power_inv', Float),
                 Column('reactive_power_inv', Float),
                 Column('apparent_power_inv', Float),
                 Column('voltage_uab_inv', Float),
                 Column('voltage_ubc_inv', Float),
                 Column('voltage_uca_inv', Float),
                 Column('voltage_ua_inv', Float),
                 Column('voltage_ub_inv', Float),
                 Column('voltage_uc_inv', Float),
                 Column('current_a_inv', Float),
                 Column('current_b_inv', Float),
                 Column('current_c_inv', Float),
                 Column('current_avg_inv', Float),
                 Column('frequency_inv', Float),
                 Column('cos_inv', Float),
                 Column('heat_sink_temp_inv', Float),
                 Column('energy', Float),
                 Column('state_1_inv', Float),
                 Column('state_2_inv', Float)
                 )

database = Database(DATABASE_URL)