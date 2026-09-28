from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from datetime import datetime
from backend.app.database import Base

class TrafficLog(Base):
    __tablename__ = "traffic_logs"

    id = Column(Integer, primary_key=True, index=True)
    intersection_id = Column(String, index=True)
    lane_1_count = Column(Integer)
    lane_2_count = Column(Integer)
    active_signal = Column(Integer)  # 1 for Lane 1 Green, 2 for Lane 2 Green
    emergency_override = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)