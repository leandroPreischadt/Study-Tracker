from sqlalchemy import Column, Integer, ForeignKey, Date, Interval
from sqlalchemy.orm import relationship
from DataBase import Base
import time

class StudySession(Base):
    __tablename__ = "study_sessions"
    
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer,ForeignKey("topics.id"))
    study_date = Column(Date)
    duration = Column(Interval)
    
    topic = relationship("Topic", back_populates="study_sessions")