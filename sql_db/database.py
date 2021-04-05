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
                 Column('input_EA', Float),
                 Column('return_EA', Float),
                 Column('ind_EQ', Float),
                 Column('cap_EQ', Float),
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
                 Column('power_DC', Float),
                 Column('voltage_DC', Float),
                 Column('current_DC', Float),
                 Column('power_inv', Float),
                 Column('reactive_power_inv', Float),
                 Column('apparent_power_inv', Float),
                 Column('voltage_UAB_inv', Float),
                 Column('voltage_UBC_inv', Float),
                 Column('voltage_UCA_inv', Float),
                 Column('voltage_UA_inv', Float),
                 Column('voltage_UB_inv', Float),
                 Column('voltage_UC_inv', Float),
                 Column('current_A_inv', Float),
                 Column('current_B_inv', Float),
                 Column('current_C_inv', Float),
                 Column('current_avg_inv', Float),
                 Column('frequency_inv', Float),
                 Column('cos_inv', Float),
                 Column('heat_sink_temp_inv', Float),
                 Column('energy', Float),
                 Column('state_1_inv', Float),
                 Column('state_2_inv', Float)
                 )

database = Database(DATABASE_URL)
