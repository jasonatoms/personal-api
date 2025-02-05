from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Knowledge, Telos, SessionLocal
from typing import List, Optional
import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/knowledge_base")
def get_knowledge(category: Optional[str] = None, db: Session = Depends(get_db)):
    if category:
        data = db.query(Knowledge).filter(Knowledge.category == category).all()
    else:
        data = db.query(Knowledge).all()
    return {"data": data}

@router.post("/knowledge_base")
def add_knowledge(category: str, content: str, db: Session = Depends(get_db)):
    entry = Knowledge(category=category, content=content, last_updated=datetime.datetime.utcnow())
    db.add(entry)
    db.commit()
    return {"message": "Knowledge added successfully!"}

@router.get("/telos")
def get_telos(db: Session = Depends(get_db)):
    data = db.query(Telos).all()
    return {"telos": data}

@router.post("/telos")
def add_telos(section: str, content: str, db: Session = Depends(get_db)):
    entry = Telos(section=section, content=content, last_updated=datetime.datetime.utcnow())
    db.add(entry)
    db.commit()
    return {"message": "Telos entry added successfully!"}
