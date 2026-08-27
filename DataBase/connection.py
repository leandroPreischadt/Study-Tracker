from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from DataBase.base import Base

from models.subject import Subject
from models.topic import Topic
from models.review import Review
from models.study_session import StudySession


engine = create_engine("sqlite:///study_tracker.db")

base_session = sessionmaker(engine)

Base.metadata.create_all(engine)