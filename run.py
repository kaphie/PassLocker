#!/usr/bin/env python3
from user import Credentials
import random



welcome = f""" 
 
***********************************************************
*                                                         *
*                kaphie's Password Locker:                  *
*                                                         *
***********************************************************
\n
User Menu:  
    - 1: Login
    - 2: Create a new account
    - q: quit the application \n
Choose an option:

 """

 

def create_user_account(username,password,accountType):
    new_user_account = Credentials(username,password,accountType)
    return new_user_account

def save_user_account(User):
    User.save_user_account()

def check_existing_user_account(username):
    return Credentials.user_account_exists(username)

def display_user_accounts():
    return Credentials.display_user_accounts()

def delete_user_account(Credentials):
    Credentials.delete_user_account()

def main():
    print ("Hi there, Welcome to PassLock. A safe place to store all your passwords")
    print ("What is your username")
    user_name = input()
    print ("Please input your password")
    user_password = input()
    print (f"Hello {user_name} \n Your password is {user_password}")

    while True:
        print("Use these short codes : nw - Create a new account locker., dp - Display account lockers., dt - Delete Account., ex - Exit Password Locker.  ")

        short_code = input().lower()

        if short_code == 'nw':
            print("New Account Locker")
            print("-"*10)

            print ("Account Username")
            username = input()

            print("Would you like to generate Account password (y/n)")
            answer = input().lower()
            if answer =='y':
                chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
                number = 1
                length = input('password length?')
                length = int(length)
                for pwd in range(number):
                    password = ''
                    for c in range(length):
                        password += random.choice(chars)

            elif answer == 'n':
                print("Input Account password")
                password = input()

            print("Account type")
            accountType = input()

            save_user_account(create_user_account(username,password,accountType))
            print ('\n')
            print(f"New Contact {accountType} {username} created")
            print ('\n')

        elif short_code == 'dp':

            if display_user_accounts():
                print("Here is a list of all your Accounts details")
                print('\n')

                for Credentials in display_user_accounts():
                        print(f" Account type: {Credentials.accountType}\n Username: {Credentials.username} \n Password: {Credentials.password}")
                        print('\n')
                print('\n')
            else:
                print('\n')
                print("You dont seem to have any Account information yet")
                print('\n')

        elif short_code == "dt":
            print("Which account do you want to delete")
            deleteAccount = input()
            if deleteAccount == accountType:
                delete_user_account(Credentials)

            else:
                print("Didn't find user account")

        elif short_code == "ex":
                print("Thank you for trusting us!")
                break

        else:
                print("I did not get that. Please use the short codes")




if __name__ == '__main__':

    main()