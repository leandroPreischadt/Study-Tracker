import os
from services.subject_services import create_subject
from services.subject_services import show_subject
from services.subject_services import count_subjects
from services.topics_services import *
from services.sessions_services import study_register
from services.sessions_services import show_study_register
from services.reviews_services import create_review
from services.reviews_services import show_review
from services.reviews_services import deshboard_review
import time

def quit_option():
    
    try:
        option = input("press ENTER to loggout: ")
        
        if option == "":
            return True

    except ValueError:
        print("invalid option!")
        return False

def main():
    os.system("clear")
    
    
    
    while True:
        
        print("=======================")
        print("    STUDY TRACKER")
        print("=======================\n")
        
        count_subjects()
        count_topics()
        
        print()
        
        deshboard_review()
        
        print("\n-----------------------\n")
        
        print("---MENU---")
        print("1.CREATE YOUR STUDY")
        print("2.DELETE TOPIC")
        print("3.SHOW STUDIES")
        print("4.REGISTER STUDY")
        print("5.SHOW STUDY REGISTER")
        print("6.CREATE REVIEW")
        print("7.SHOW REVIEW")
        print("8.QUIT")
        
        try:
            option = int(input("Enter a option: "))
        except ValueError:
            os.system("clear")
            print("Invalid option!")
            continue
        
        match option:
            case 1:
                create_subject()
                create_topic()
            case 2:
                delete_topic()
            case 3:
                show_topic()
            case 4:
                study_register()
            case 5:
                show_study_register()
            case 6:
                create_review()
            case 7:
                show_review()
            case 8:
                loggout = quit_option()
                if loggout == True:
                    os.system("clear")
                    break
                else:
                    os.system("clear")
                    print("invalid option!\n")
                    time.sleep(2)
                    os.system("clear")
                    continue
                

if __name__ == "__main__":
    main()
