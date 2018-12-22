from subprocess import check_output
from sys import arg
from urllib.request import urlopen
#from paramiko import *


def find_files(fname, loc):
    cmd = " ".join(['find', loc, ' -name ', '\"*'+ fname + '*\"', ])
    fnames = check_output(cmd, shell=True).decode('utf-8')
    fname_list = fnames.split('\n')
    i = 0
    for name in fname_list:
        if '/' not in name: del fname_list[i]
        else: continue
        i += 1
    return fname_list

def insert_text(text, fname, line_no = None):
    print(type(text))
    try: text.encode()
    except Exception as e: print(e)
    print(type(text))
    if line_no == None:
        with open(fname, 'ba+') as f: f.write(text)
    else: 
        with open(fname, 'br') as f:
            lines = f.readlines()
            print(lines)
            lines[line_no - 1] += text
        with open(fname, 'bw+') as f:
            for line in lines:
                f.write(line)
    return


def find_flag(flag, loc):
    cmd = " ".join(["grep -iRn", flag, search_dir])
    flags = check_output(cmd, shell=True).decode('utf-8')
    return [flag] + flags.split('\n')

def clear_tracks(flag, logs):
    #auth, 
    return


if __name__ == '__main__':
    url = argv[1]
    fname = argv[2]
    insert_text('poopypants', fname, line_no = 1)
