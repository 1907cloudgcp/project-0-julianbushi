#!/usr/bin/env python3
import logging
import logging.config
import yaml
from controller import controller

def main():
    try:
        with open('../../../resources/logging.yaml','r') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    except:
        logging.basicConfig(level=logging.DEBUG)
        print('Logging configuration not found')
    
    controller.login_menu()

if __name__ == '__main__':
    main()
