from sqlalchemy import Column, String, Integer, Float ,ForeignKey
from sqlalchemy.orm import relationship
from DataBase import Base

class Topic(Base):
    __tablename__ = "topics"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    mastery = Column(Float)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    
    subject = relationship("Subject", back_populates="topics")
    
    reviews = relationship("Review", back_populates="topic")
    
    study_sessions = relationship("StudySession", back_populates="topic")