from datetime import datetime
from pydantic import BaseModel, BaseConfig, Field


class ReadingBase(BaseModel):
    date: datetime = Field(...)
    total_power: float = Field(...)
    total_reactive_power: float = Field(...)
    total_apparent_power: float = Field(...)
    power_l1: float = Field(...)
    power_l2: float = Field(...)
    power_l3: float = Field(...)
    reactive_power_l1: float = Field(...)
    reactive_power_l2: float = Field(...)
    reactive_power_l3: float = Field(...)
    voltage_13: float = Field(...)
    voltage_12: float = Field(...)
    voltage_23: float = Field(...)
    voltage_l1: float = Field(...)
    voltage_l2: float = Field(...)
    voltage_l3: float = Field(...)
    current_l1: float = Field(...)
    current_l2: float = Field(...)
    current_l3: float = Field(...)
    current_n: float = Field(...)
    frequency: float = Field(...)
    total_cos: float = Field(...)
    cos_l1: float = Field(...)
    cos_l2: float = Field(...)
    cos_l3: float = Field(...)
    input_EA: float = Field(...)
    return_EA: float = Field(...)
    ind_EQ: float = Field(...)
    cap_EQ: float = Field(...)
    power_DC: float = Field(...)
    voltage_DC: float = Field(...)
    current_DC: float = Field(...)
    power_inv: float = Field(...)
    reactive_power_inv: float = Field(...)
    apparent_power_inv: float = Field(...)
    voltage_UAB_inv: float = Field(...)
    voltage_UBC_inv: float = Field(...)
    voltage_UCA_inv: float = Field(...)
    voltage_UA_inv: float = Field(...)
    voltage_UB_inv: float = Field(...)
    voltage_UC_inv: float = Field(...)
    current_A_inv: float = Field(...)
    current_B_inv: float = Field(...)
    current_C_inv: float = Field(...)
    current_avg_inv: float = Field(...)
    frequency_inv: float = Field(...)
    cos_inv: float = Field(...)
    heat_sink_temp_inv: float = Field(...)
    energy: float = Field(...)
    state_1_inv: float = Field(...)
    state_2_inv: float = Field(...)


class Reading(ReadingBase):
    id: int
