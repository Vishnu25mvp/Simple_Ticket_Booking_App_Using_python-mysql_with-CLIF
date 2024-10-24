import bussince_logic as BL
from User import User
from Agent import Agent


def Agent_Main_Menu(data):
    a = True
    while a:
        print("1. Upload Event")
        print("2. Exit")
        option = int(input("ENter Your Option's"))
        if option == 1:
            event_name = input("Enter Event Name : ")
            year = input("Enter the exact Year in this format YYYY:")
            month = input("Enter the month in this formar MM : ")
            date = input("Enter the date in this format DD")
            HH = input("Enter the time only HH :")
            MM = input("Enter the time only mm : ")
            datetime = f"{year}-{month}-{date} {HH}:{MM}:00"
            seat = int(input("Enter Number of Seat available "))
            data.post_event(event_name,datetime,seat)
        elif option == 2:
            a = False
        else:
            print("Invalid Value ")


def Menu(data):
    cond = True
    user_option = int()
    while cond:
        print("""\n
                        1. View available events.\n
                        2. Book tickets.\n
                        3. Cancel tickets.\n
                        4. View booking history.\n
                        5. Log Out.\n""")

        try:

            user_option = int(input("Enter Your Option"))
        except ValueError:
            print("""Enter Vaild Option """)
            # global user

        if user_option == 1:
            data.display_event()
            pass
        elif user_option == 2:
            event_id = input("Enter Event ID : ")
            data.Book_Ticket(event_id)
        elif user_option == 3:
            booking_id = int(input("Eneter the Booking_Id to cancel the Ticet : "))
            data.Cancel_Ticker(Booking_id=booking_id)
        elif user_option == 4:
            data.Booking_history()
        elif user_option == 5:
            cond = False


def user_menu():
    a = True
    while a:
        print("Welcome to Ticket Booking App for Event")
        print("1. Log in")
        print("2. Sing up")
        print("3. Exit")
        global user_option
        try:
            user_option = int(input("Enter Your Option : "))
        except ValueError:
            print("Enter Vaild Option Please enter the Correct vlaue ")
        finally:
            if user_option == 1:
                user = input("Enter Your User Id : ")
                passwd = input("Enter Your Password : ")
                data = BL.login(user, passwd)
                if bool(data):
                    user_id = int(data[0][0])
                    user_name = str(data[0][1])
                    mail = str(data[0][2])
                    user_instance = User(user_id, user_name, mail)
                    Menu(user_instance)
                else:
                    print("Incorrect Username and Password")

            elif user_option == 2:
                user_name = input("Enter Your User Name : ")
                email = input("Enter Your Email ID : ")
                password = input("Enter Your Password : ")
                BL.Singup(user_name, email, password)
            elif user_option == 3:
                a = False

            else:
                print("Enter Vaild Number")


def Agent_Menu():
    a = True
    while a:
        print("1. Log in")
        print("2. Sing up")
        print("3. Exit")
        option = int(input("ENnter Your Option : "))
        if option == 1:
            user = input("Enter Agent Name : ")
            password = input("Enter your password : ")
            data = BL.Agent_login(user, password)
            if bool(data):
                agent_id = int(data[0][0])
                agent_name = str(data[0][1])
                agent_gstin = str(data[0][2])
                agent_instance = Agent(agent_id, agent_name, agent_gstin)
                Agent_Main_Menu(agent_instance)
            else:
                print("""Incorrect Username and Password""")

        elif option == 2:
            agent_name = input("Enter Your Agent Name : ")
            gstin = input("Enter Your GSTIN : ")
            password = input("Enter Your Password : ")
            BL.Agent_Singup(agent_name, gstin, password)

        elif option == 3:
            a = False
        else:
            print("Invaild Number ")


if __name__ == "__main__":
    while True:
        print("Welcome to Ticket Booking App ")
        print("1. User log in")
        print("2. Agent log in")
        option = int(input("Enter your option"))
        if option ==1:
            user_menu()
        elif option ==2:
            Agent_Menu()
        else:
            print("Invild Option's")
