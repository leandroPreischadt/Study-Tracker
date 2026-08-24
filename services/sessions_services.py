from models.topic import Topic
from models.study_session import StudySession
from sqlalchemy.orm import session
from sqlalchemy import select
from DataBase.connection import base_session
from datetime import date, timedelta
from services.topics_services import show_topic

def study_register():
    
    show_topic()
    try:
        default_date = date.today()
        select_topic = input("Enter the topic wish you want register your study: ").capitalize()
        hours = int(input("How many hours do you spand?: ")) * 60
        minutes = int(input("How many minutes do you spand?: "))
        time = hours + minutes
        
        with base_session() as session:
            id_topic = session.scalars(select(Topic.id).where(Topic.name == select_topic)).one_or_none()
            
            topic = StudySession(topic_id= id_topic, study_date = default_date, duration= time)
            session.add(topic)
            session.commit()
    except ValueError:
        print("Error")

def show_study_register():
    pass