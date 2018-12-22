from subprocess import check_output
from pprint import pprint
from sys import argv
from urllib.request import urlopen
#from paramiko import *


def get_key(url):
    key = urlopen(url).readlines()
    if len(key) != 1: return False
    #else: return key[0]
    else: 
        print(key[0])
        return key[0]

def send_info(text):
    return

if __name__ == '__main__':
    url = argv[1]
    fname = argv[2]
