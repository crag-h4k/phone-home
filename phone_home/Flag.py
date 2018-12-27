from subprocess import check_output
from pprint import pprint


class Flag:
    def __init__(self, str_flag, fname, line_no, line_text):
        self.str_flag = str_flag
        self.fname = fname
        self.line_no = int(line_no)
        self.line_text = line_text

def find_flag(flag, directory):
    cmd = " ".join(['grep -rnw', directory, '-e', flag])
    flags = check_output(cmd, shell=True).decode('utf-8')
    return [flag] + flags.split('\n')

def make_flags(raw_flags):
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
        #print(F.str_flag, F.fname, F.line_no, F.line_text)
        F_list.append(F)
    return F_list

def get_line_nos(Flags):
    file_names = []
    data = []
    for Flag in Flags:
        if Flag.fname not in file_names:
            file_names.append(Flag.fname)
    for fname in file_names:
        line_nos = []
        for Flag in Flags:
            if fname != Flag.fname: continue
            line_nos.append(Flag.line_no)
        file_data = {'flag':Flag.str_flag, 'file_name':fname, 'lines':line_nos}

        data.append(file_data)

    return data

if __name__ == '__main__':
    F_list = make_flags(find_flag('is','../tests/log'))
    get_line_nos(F_list)
