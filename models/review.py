from sqlalchemy import Column, Integer, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from DataBase.base import Base


class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    date = Column(Date)
    score = Column(Float)
    next_review = Column(Date)
    
    topic = relationship("Topic", back_populates="reviews")