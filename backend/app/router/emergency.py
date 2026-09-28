from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.app.database import get_db

router = APIRouter(
    prefix="/emergency",
    tags=["Emergency Routing"]
)

@router.post("/override")
def trigger_emergency_override(intersection_id: str, lane_id: str):
    """
    Manually or automatically trigger a green corridor for an approaching emergency vehicle.
    """
    return {
        "status": "success",
        "message": f"Green corridor activated for Lane {lane_id} at Intersection {intersection_id}",
        "override_active": True
    }

@router.get("/status/{intersection_id}")
def get_emergency_status(intersection_id: str):
    """
    Get current emergency override status for an intersection.
    """
    return {
        "intersection_id": intersection_id,
        "override_active": False
    }