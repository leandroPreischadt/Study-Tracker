from models.topic import Topic
from models.study_session import StudySession
from sqlalchemy.orm import session
from sqlalchemy import select
from DataBase.connection import base_session
from datetime import date, timedelta
from services.topics_services import show_topic
import os

def study_register():
    
    show_topic()
    try:
        
        with base_session() as session:
            default_date = date.today()
            
            select_topic = input("Enter the topic wish you want register your study: ").capitalize()
            
            id_topic = session.scalars(select(Topic.id).where(Topic.name == select_topic)).one_or_none()
            
            if id_topic is None:
                print("Topic not founded!")
                return
            
            hours = int(input("How many hours do you spand?: ")) * 60
            minutes = int(input("How many minutes do you spand?: "))
            time = hours + minutes
            
            
            topic = StudySession(topic_id= id_topic, study_date = default_date, duration= time)
            session.add(topic)
            session.commit()
    except ValueError:
        print("Error")

def show_study_register():
    try:
        with base_session() as session:
            show_topic()
            
            topic_id= int(input("What topic do you want to see?: "))
            
            sessions = session.scalars(select(StudySession).where(StudySession.topic_id == topic_id)).one_or_none()
            
            if not sessions:
                print("sessions not founded!")
                return 
            
            hours = sessions.duration // 60
            minutes = sessions.duration % 60
            
            os.system("clear")
            print(f"# {sessions.topic.name}\n")
            print(f"Data: {sessions.study_date}")
            print(f"Time: {hours}h{minutes}min" if hours < 2 else f"{hours}hours: {minutes}min")
            
            quit_option = input("\npress enter to quit: ")
            
            if quit_option == "":
                return 
            
    except ValueError:
        print()