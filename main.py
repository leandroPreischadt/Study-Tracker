import os
from services.subject_services import create_subject
from services.subject_services import show_subject
from services.topics_services import create_topic


def main():
    print("Wlcome to your Study Staion!")
    
    while True:
        print("---MENU---")
        print("1.CREATE YOUR STUDY\n")
        
        try:
            option = int(input("Enter a option: "))
        except ValueError:
            print("Invalid option!")
            continue
        
        match option:
            case 1:
                create_subject()
                create_topic()


if __name__ == "__main__":
    main()
