#!/usr/bin/env python3
from fileio import io
from service import service
from controller import controller
'''
This is your main script, this should call several other scripts within your packages.
'''
def main():
        controller.login_menu()
        #print(service.getUserList())
        #service.registerUser('newperson', 'passww')

if __name__ == '__main__':
	main()
