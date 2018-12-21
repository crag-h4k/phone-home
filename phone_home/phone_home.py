from subprocess import check_output
from os import system
from pprint import pprint

#from paramiko import *


class Flag:
    def __init__(self, str_flag, fname, line_no, line_text):
        self.str_flag = str_flag
        self.fname = fname
        self.line_no = int(line_no)
        self.line_text = line_text

def find_files(fname, loc):
    cmd = " ".join(['find', loc, ' -name ', '\"'+ fname + '\"', ])
    fnames = check_output(cmd, shell=True).decode('utf-8')
    pprint(fnames)
    return fnames.split('\n')

def get_key_text(url):
    cmd = " ".join(['curl ', url])
    check_output(cmd)
    return


def save_key_file(key_text, ssh_dir):
    cmd = " ".join(['curl ', url])
    run(cmd)
    return

def send_info(text):
    return

def find_flag(flag, loc):
    cmd = " ".join(["grep -iRn", flag, search_dir])
    flags = check_output(cmd, shell=True).decode('utf-8')
    #pprint(flags)
    return [flag] + flags.split('\n')

    #Flag(str_flag, fname, line_no, line_text):
def make_flag(raw_flags):
    F_list = []
    str_flag = raw_flags[0]
    for flag in raw_flags:
        data = [str_flag] + flag.split(':')
        if len(data) != 4: continue
        F = Flag(
            str_flag = data[0],
            fname = data[1],
            line_no = data[2],
            line_text = data[3],)
        F_list.append(F)
        pprint(data)
    return F_list

        
    print(_flags)
def clear_tracks(flag, logs):
    #auth, 
    return

if __name__ == '__main__':
    #flag = 'flag'
    #search_dir = '../tests/log'
    #raw_flags = find_flag(flag, search_dir)
    #F_list = make_flag(raw_flags)
    #print(F_list)
    find_files('authorized_keys', '/')
