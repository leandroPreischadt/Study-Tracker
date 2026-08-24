import os
from services.subject_services import create_subject
from services.subject_services import delete_subject
from services.subject_services import show_subject
from services.topics_services import create_topic
from services.topics_services import delete_topic
from services.topics_services import show_topic

def quit_option():
    
    try:
        option = input("press q to loggout: ").lower()
        
        if option == "q":
            return True

    except ValueError:
        print("invalid option!")
        return False

def main():
    print("Wlcome to your Study Staion!")
    
    while True:
        print("---MENU---")
        print("1.CREATE YOUR STUDY")
        print("2.DELETE TOPIC")
        print("3.SHOW STUDIES")
        print("4.QUIT")
        
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
                loggout = quit_option()
                if loggout == True:
                    break
                else:
                    os.system("clear")
                    print("invalid option!")
                    continue
                

if __name__ == "__main__":
    main()
