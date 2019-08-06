from service import service

def login_menu():
    print('Welcome to the Bank\n')
    
    selection = ''
    
    while True:
        print('Press L to login. Press R to register. Press Q to exit...')
        selection = input()
        if selection.upper() == 'Q':
            break
        elif selection.upper() == 'L':
            loggedUser = login()
            return loggedUser
        elif selection.upper() == 'R':
            register()
        else:
            print('That is not a valid input. Please try again.\n')

    user_menu(loggedUser)
    
def user_menu(loggedUser):
    while True:
        print('Welcome, ' + loggedUser '. What would you like to do?')
        print('1) 

    
def login():
    isLogin = False
    user = None
    
    print('Enter your username and password.\n')
    while not isLogin:
        user = input('user: ')
        passwd = input('pass: ')

        check = service.loginUser(user, passwd)

        if  check == 1:
            #user found & password correct
            isLogin = True
        elif check == 2:
            #user found, password incorrect
            print('Password for user ' + user + ' is incorrect. Please try again.\n')
        else:
            #user not found
            print('That username does not exist. Please try again.\n')
    
    return user

def register():
    valid = False

    user = input('Enter the username for your new account: ')
    while not valid:
        passwd = input('Enter the password for your new account: ')
        passwd2 = input('Confirm new password: ')

        if passwd == passwd2:
            service.registerUser(user, passwd)
            valid = True
        else:
            print('Entered passwords do not match. Please try again.\n\n')

    return

    

    
    
