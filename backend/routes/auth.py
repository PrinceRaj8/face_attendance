from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, schemas, auth

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    user_data = auth.authenticate_user(db, user.username, user.password)
    if not user_data:
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    
    access_token = auth.create_access_token(data={"sub": user_data.username})
    return {"access_token": access_token, "token_type": "bearer"}
