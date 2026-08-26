from models.topic import Topic
from sqlalchemy.orm import session
from sqlalchemy import select
from DataBase.connection import base_session
from services.topics_services import show_topic
from datetime import timedelta
from models.review import Review
import os

def create_review():
    
    try:
        with base_session() as session:
            show_topic()
            
            select_topic = input("Select a topic: ").capitalize()
            
            topics = session.scalars(select(Topic).where(Topic.name == select_topic)).one_or_none()
            
            if topics is None:
                print("Topic not founded!")
                return
            
            
            for topic in topics.study_sessions:
                date_now = topic.study_date
            
            print("How do you feel about this topic?\n")
            print("1- I forgotten practically everthing")
            print("2- I remember a little bit")
            print("3- I remember reasonably well")
            print("4- I remember well")
            print("5- I domain")
            
            topic_domain = int(input("Select a number between (1-5): "))
            
            match topic_domain:
                case 1:
                    new_date = date_now + timedelta(days=1)
                case 2:
                    new_date = date_now + timedelta(days=2)
                case 3:
                    new_date = date_now + timedelta(days=4)
                case 4:
                    new_date = date_now + timedelta(days=7)
                case 5:
                    new_date = date_now + timedelta(days=14)
            
            review = Review(topic_id= topics.id, date= date_now, score= topic_domain, next_review= new_date)
            
            session.add(review)
            session.commit()
            
            os.system("clear")
            print("Review registred")
            
    except ValueError:
        print("The answer must be a digit!")
        return 


def show_review():
    pass