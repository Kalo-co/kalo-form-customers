from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import SessionLocal, User, Developer, engine
import uvicorn

app = FastAPI()

# Modelos Pydantic
class UserCreate(BaseModel):
    full_name: str
    email: str
    company: str
    location: str

class DeveloperCreate(BaseModel):
    full_name: str
    email: str
    linkedin: str
    age: int
    country: str
    formal_education: str
    skills: str
    work_experience: str
    role: str
    english_level: str
    
# Dependencia para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/customers/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"status": "success", "data": db_user}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/developers/", status_code=status.HTTP_201_CREATED)
def create_developer(dev: DeveloperCreate, db: Session = Depends(get_db)):
    try:
        db_dev = Developer(**dev.dict())
        db.add(db_dev)
        db.commit()
        db.refresh(db_dev)
        return {"status": "success", "data": db_dev}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def init_db():
    from models import Base
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    
    init_db()  # Iniciar DB y crear tablas
    uvicorn.run(app, host="0.0.0.0", port=8000)
