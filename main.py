from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import SessionLocal, User, engine
import uvicorn

app = FastAPI()

# Modelos Pydantic
class UserCreate(BaseModel):
    full_name: str
    email: str
    company: str
    location: str

# Dependencia para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/customers/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def init_db():
    from models import Base
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    
    init_db()  # Iniciar DB y crear tablas
    uvicorn.run(app, host="0.0.0.0", port=8000)
