from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Knowledge(Base):
    __tablename__ = 'knowledge'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    content = Column(String)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)

class Telos(Base):
    __tablename__ = 'telos'
    id = Column(Integer, primary_key=True, index=True)
    section = Column(String, index=True)
    content = Column(String)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)

DATABASE_URL = "sqlite:///./personal_api.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
