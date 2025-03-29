from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, crud

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/", response_model=schemas.AttendanceResponse)
def mark_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(database.get_db)):
    return crud.mark_attendance(db, attendance)
