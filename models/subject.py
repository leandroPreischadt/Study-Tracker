from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from DataBase import Base

class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key= True)
    name = Column(String(50))
    description = Column(String(100))
    
    topics = relationship("Topic", back_populates="subject")