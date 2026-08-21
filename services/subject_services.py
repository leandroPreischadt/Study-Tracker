from models.subject import Subject
from DataBase.connection import base_session
from sqlalchemy.orm import Session
from sqlalchemy import select
import os

def create_subject():
    with base_session() as session:
        name = input("Enter the name of your subject: ")
        description = input("Enter the description of your subject: ")
        
        subject = Subject(name = name, description= description)
        session.add(subject)
        session.commit()

    print(f"Subject < {name} > as created!\n")
    
def show_subject():
    with base_session() as session:
        subjects = session.scalars(select(Subject.name)).all()
    
    os.system("clear")
    for subject in subjects:
        print("=== Subjects ===")
        print(f"- {subject}\n")
        
        