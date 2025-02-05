from sqlalchemy.orm import Session
from app.models import Knowledge, Telos
import datetime

def add_entry(db: Session, model, section: str, content: str):
    entry = model(section=section, content=content, last_updated=datetime.datetime.utcnow())
    db.add(entry)
    db.commit()
    return {"message": f"{model.__tablename__.capitalize()} entry added successfully!"}

def get_entries(db: Session, model):
    return db.query(model).all()

def get_entries_by_section(db: Session, model, section: str):
    return db.query(model).filter(model.section == section).all()
