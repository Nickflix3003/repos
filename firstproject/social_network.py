#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui

#Create instance of main social network object
ai_social_network = SocialNetwork()
ai_social_network.reload_social_media()
#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()
        elif choice == "2":
            name = input("enter a name: ")
            if (ai_social_network.findUser(name)):
                ai_social_network.setCurrentUser(name)
                inner_menu_choice = social_network_ui.manageAccountMenu()
                #Handle inner menu here
                while True: 
                    if inner_menu_choice == "1":
                        user = ai_social_network.getCurrentUser()
                        print(user.view_details())
                    if inner_menu_choice == "2":
                        #edit details
                        user = ai_social_network.getCurrentUser()
                        print(user.view_details())
                        choice = input ("1: Change name \n 2: Change age \n")
                        if choice == "1":
                            name = input("Enter in a new name: ")
                            ai_social_network.getCurrentUser().set_name(name)
                        elif choice == "2":
                            age = input("Enter in a new age: ")
                            ai_social_network.getCurrentUser().set_age(age)
                    if inner_menu_choice == "3":
                        #add friend
                        print(f"People: {ai_social_network}")
                        added = input("Enter the name of a person you would like to add: ")
                        if (ai_social_network.findUser(added)):
                            ai_social_network.getCurrentUser().add_friend(ai_social_network.getUser(added))
                            print(f"{added} added")
                            print("Length of friends list: " + str(len(ai_social_network.getCurrentUser().get_friends_list())))
                        else:
                            print("Person does not exist")
                    if inner_menu_choice == "4":
                        #view all my friends
                        print(ai_social_network.getCurrentUser().view_friends())
                    if inner_menu_choice == "5":
                        #view all my messages
                        print(ai_social_network.getCurrentUser().view_blocked())
                    if inner_menu_choice == "6": 
                        print(ai_social_network.getCurrentUser().view_messages())
                    if inner_menu_choice == "7":
                        ai_social_network.send_message()
                    if inner_menu_choice == "8": 
                        print(f"Friends: {ai_social_network.getCurrentUser().view_friends()}")
                        added = input("Enter the name of a friend you would like to block: ")
                        if (ai_social_network.getCurrentUser().block(added)):
                            print(f"{added} blocked")
                        else:
                            print(f"{name} is not your friend")
                    if inner_menu_choice == "9":

                        # go back
                        break
                    else:
                        inner_menu_choice = social_network_ui.manageAccountMenu()
            else:
                print("User does not exist")
        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        