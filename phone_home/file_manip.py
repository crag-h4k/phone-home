from subprocess import check_output
from sys import argv
from urllib.request import urlopen
from pprint import pprint
#from paramiko import *
from Flag import Flag, find_flag, make_flags

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

def x_clear_tracks(flag, fname):
    flag.encode()

    with open(fname, 'br+') as f:
        lines = f.readlines()
        f.seek()
        for line in lines:
            if flag in line: continue
            else: f.write(line)
    return

def clear_tracks(flag, fname):
    flag.encode()

    with open(fname, 'br+') as f:
        lines = f.readlines()
        f.seek()
        for line in lines:
            if flag in line: continue
            else: f.write(line)
    return

if __name__ == '__main__':
    flag = argv[1]
    F_list = make_flags(find_flag(flag, '../tests'))
    [print(F.fname, F.line_no, F.line_text) for F in F_list]
