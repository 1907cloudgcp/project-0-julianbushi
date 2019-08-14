import logging
from service import service
from error import exceptions

def login_menu():
    print('Welcome to the Bank\n')
    
    selection = ''
    
    while True:
        print('Press L to login. Press R to register. Press Q to exit...')
        selection = input()
        if selection.upper() == 'Q':
            return None
        elif selection.upper() == 'L':
            loggedUser = login()
            user_menu(loggedUser)
        elif selection.upper() == 'R':
            register()
        else:
            print('That is not a valid input. Please try again.\n')

    
    
def user_menu(loggedUser):
    
    selection = ''
    print('Welcome, ' + loggedUser + '. What would you like to do?')
    while True:
        print('1) Deposit\n2) Withdraw\n3) View Balance\n4) View Transaction History\nPress Q to logout...')
        selection = input()
        if selection == '1':
            #Deposit
            while True:
                print('Enter the amount you wish to deposit: ')
                try:
                    amount = float(input('$'))
                    if amount < 0:
                        raise InputError
                    service.transfer(loggedUser, amount, 1)
                    break
                except:
                    print('Please enter a positive value')
        elif selection == '2':
            #Withdraw
            while True:
                print('Enter the amount you wish to withdraw: ')
                try:
                    amount = float(input('$'))
                    if amount < 0:
                        raise InputError
                    service.transfer(loggedUser, amount, 2)
                    break
                except:
                    print('Please enter a positive value')
        elif selection == '3':
            #View Balance
            print('\nYour balance is: $' + str(service.getBalance(loggedUser)) + '\n')
        elif selection == '4':
            # View Transaction History
            service.printHistory(loggedUser)
        elif selection.upper() == 'Q':
            return
        else:
            print('That is not a valid input. Please try again.\n')
    
def login():
    loggedOn = False
    user = None
    
    print('Enter your username and password.\n')
    while not loggedOn:
        user = input('user: ')
        passwd = input('pass: ')

        try:
            check = service.loginUser(user, passwd)

            if  check == 0: #user not found
                print('That username does not exist. Please try again.\n')
            elif check == 1: #user found, password incorrect
                print('Password for user ' + user + ' is incorrect. Please try again.\n')
            elif  check == 2: #user found & password correct
                loggedOn = True
            else:
                raise CheckError
        except:
            logging.error('An exception occured!')
    
    return user

def register():
    validUserEntry = False
    validPassEntry = False
    
    while not validUserEntry:
        user = input('Enter the username for your new account: ')

        if service.checkUser(user) is False:
            validUserEntry = True 
        else:
            print('That username already exists. Try again')
       
    while not validPassEntry:
        passwd = input('Enter the password for your new account: ')
        passwd2 = input('Confirm new password: ')

        if passwd == passwd2:
            service.registerUser(user, passwd)
            validPassEntry = True
        else:
            print('Entered passwords do not match. Please try again.\n\n')

    return

    

    
    
