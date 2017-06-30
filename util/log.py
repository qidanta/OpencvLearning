import sys
from termcolor import colored, cprint

def info(type, value):
    '''print message in format

    - Params:
    @type: what kind of levels infomation
    @value: print the value
    '''
    type = colored(type, 'white', attrs=['bold'])
    print ('[ INFO ] {} is: \n {}'.format(type, value))