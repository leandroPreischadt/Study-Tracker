from models.topic import Topic
from models.subject import *
from sqlalchemy.orm import session
from DataBase.connection import base_session
from services.subject_services import show_subject
from sqlalchemy import select

def create_topic():
    
    try:
        with base_session() as session:
            show_subject()
            
            subject_topic = input("Enter the subject wish you want to insert the topic: ")
            name_topic = input("Enter the topic of your subject: ")
            mastery = float(input("how many do you domain this topic?: "))
            
            id_subject = session.execute(select(Subject.id).where(Subject.name == subject_topic)).scalar_one_or_none()
            
            if id_subject is None:
                print("Subject not founded!")
                return 
            
            topic = Topic(name=name_topic, mastery=mastery, subject_id = id_subject)
            
            session.add(topic)
            session.commit()
    except ValueError:
        print("Error")
