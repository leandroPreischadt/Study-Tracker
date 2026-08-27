from models.topic import Topic
from models.subject import *
from sqlalchemy.orm import session
from DataBase.connection import base_session
from services.subject_services import show_subject
from sqlalchemy import select
import os

def create_topic():
    
    try:
        with base_session() as session:
            topics = session.scalars(select(Topic)).all()
            
            if not topics:
                show_subject()
            else:
                show_topic()
            
            subject_topic = input("Enter the subject wish you want to insert the topic: ").capitalize()
            name_topic = input("Enter the topic of your subject: ").capitalize()
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

def delete_topic():
    show_topic()
    print()
    delete_choice = int(input("Enter the topic wish you want to delete: "))

    try:
        with base_session() as session:
            topic = session.scalar(select(Topic).where(Topic.id == delete_choice))
            print(f"You deleted <{topic.name}>")
            session.delete(topic)
            session.commit()
    except ValueError:
        print("Error\n")
    
    
    
def show_topic():
    try:
        with base_session() as session:
            subjects = session.scalars(select(Subject)).all()
            
            if not subjects:
                os.system("clear")
                print("No subjects stored\n")
                return 
            
            print()
            for subject in subjects:
                print(f"#{subject.name}")
                
                if not subject.topics:
                    os.system("clear")
                    print("No topics stored\n")
                    return
                
                for topic in subject.topics:
                    print(f"|")
                    print(f"|__ {topic.id}) {topic.name}")
                print()
    except ValueError:
        print("No subjects stored")

def count_topics():
    with base_session() as session:
        topics = session.scalars(select(Topic)).all()
        
        number_of_topics = len(topics)
        
        print(f"📖 Topics: {number_of_topics}")