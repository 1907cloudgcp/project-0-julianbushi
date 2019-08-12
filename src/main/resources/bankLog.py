#!/usr/bin/env python3

'''
Logging

Includes: Use the Logger, Logging Levels

Note: For this example to work create a folder in /var/log called my_script
'''
import logging
import logging.config
import os
import yaml

def main():
    simple_logging()
    configured_logging()

def simple_logging():
    '''
    -> Use the same name of logger to get the same object back in another class
    -> Create it first in your main script
    -> You could also declare it just once in the global scope of your main script
    -> If no name is provided, you get the "root" logger
    '''
    logger = logging.getLogger('8-logging')

    '''
    -> Remember the default is WARNING (if you comment this line, DEBUG and INFO will disappear)
    -> If you want messages to print in stdout, remove filename=
    '''
    logging.basicConfig(level=logging.DEBUG, 
filename='../../../resources/log.txt')

'''
Logging can be configured through:
-> A YAML file
-> A JSON file
-> A dict object

Let's proceed with the YAML approach. Research the other approaches!

-> In this case, we are specifying optional values for the yaml configuration location
and the level
'''
def configured_logging(config_path='logging.yaml'):
    if os.path.exists(config_path):
        with open(config_path,'r') as f:
            config = yaml.safe_load(f.read())
        #Enable our loaded configuration
        logging.config.dictConfig(config)
    else:
        raise ValueError('Logging configuration not found')

    #Test our configuration
    logger = logging.getLogger('8-logging')

    #Goes to a file
    logger.info('I have configured logging through a file')

    #Goes to another file
    logger.error('I have configured logging through a file')

    #Goes to the console
    logger.debug('I have configured logging through a file')
