from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.models import TrafficLog
from backend.app.schemas import TrafficLogResponse
from typing import List

router = APIRouter(prefix="/api/v1", tags=["Traffic Management"])

@router.get("/status", response_model=TrafficLogResponse)
def get_latest_status(db: Session = Depends(get_db)):
    latest_log = db.query(TrafficLog).order_by(TrafficLog.created_at.desc()).first()
    if not latest_log:
        return TrafficLogResponse(
            id=0, intersection_id="INT_NAGPUR_01", lane_1_count=0, 
            lane_2_count=0, active_signal=1, emergency_override=False, created_at=None
        )
    return latest_log

@router.get("/history", response_model=List[TrafficLogResponse])
def get_traffic_history(limit: int = 20, db: Session = Depends(get_db)):
    logs = db.query(TrafficLog).order_by(TrafficLog.created_at.desc()).limit(limit).all()
    return logs