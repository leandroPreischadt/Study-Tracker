import os
from services.subject_services import create_subject
from services.subject_services import show_subject
from services.topics_services import create_topic
from services.topics_services import delete_topic

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
        print("2.QUIT")
        print("3.DELETE TOPIC")
        
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
                loggout = quit_option()
                if loggout == True:
                    break
                else:
                    os.system("clear")
                    print("invalid option!")
                    continue
            case 3:
                delete_topic()
                

if __name__ == "__main__":
    main()
