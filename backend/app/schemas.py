from pydantic import BaseModel
from datetime import datetime

class TrafficLogBase(BaseModel):
    intersection_id: str
    lane_1_count: int
    lane_2_count: int
    emergency: bool

class TrafficLogResponse(TrafficLogBase):
    id: int
    active_signal: int
    created_at: datetime

    class Config:
        from_attributes = True

class OverrideRequest(BaseModel):
    intersection_id: str
    force_lane: int