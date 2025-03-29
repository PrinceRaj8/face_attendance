from fastapi import FastAPI
from .routes import auth, users, attendance
from .database import engine, Base

app = FastAPI()

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Include Routes
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(attendance.router)

@app.get("/")
def home():
    return {"message": "Face Recognition Attendance System API"}
