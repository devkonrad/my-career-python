from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class Job(Base):
    __tablename__ = 'jobs'
    id  = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True))