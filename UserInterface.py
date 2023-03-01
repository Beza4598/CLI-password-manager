import FirebaseAdmin
import sys


class UserInterface:

    def start(self):

        initial_choice = input("Please enter L to login, S for Sign-up, or Q to close the program.")

        if initial_choice == "L":
            user_name = input("Enter username: ")
            password = input("Enter password: ")
            FirebaseAdmin.sign_in_with_email_and_password(user_name, password)
        elif initial_choice == "S":
            user_name = input("Enter username: ")
            password = input("Enter password: ")
            FirebaseAdmin.new_user(user_name, password)
            FirebaseAdmin.sign_in_with_email_and_password(user_name, password)
        elif initial_choice == "Q":
            sys.exit()

        user_option = input("(A)dd, (R)etrieve, (U)pdate, (E)nd Session")


