from models.subject import Subject
from DataBase.connection import base_session
from sqlalchemy.orm import Session
from sqlalchemy import select
import os

def create_subject():
    with base_session() as session:
        name = input("Enter the name of your subject: ").capitalize()
        description = input("Enter the description of your subject: ").capitalize()
        
        subject = Subject(name = name, description= description)
        session.add(subject)
        session.commit()

    print(f"Subject < {name} > as created!\n")
    
def show_subject():
    with base_session() as session:
        subjects = session.scalars(select(Subject.name)).all()
        
        if not subjects:
            print("No subject stored")
            return
    
    os.system("clear")
    print("=== Subjects ===")
    for subject in subjects:
        print(f"- {subject}\n")

def count_subjects():
    with base_session() as session:
        subjects = session.scalars(select(Subject.name)).all()
        
        number_of_subjects = len(subjects)
        
        print(f"📚 Subjects: {number_of_subjects}")