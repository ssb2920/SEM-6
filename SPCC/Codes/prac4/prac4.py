with open('prac4.txt') as f:
    lines = f.read().splitlines()

name = ''
for line in lines:
    if 'H' in line:
        _word = line.split(' ')
        name = _word[1]
        print(f'Name of program : {name}')
    elif 'E' in line:
        _word = line.split(' ')
        start = _word[1]
        print(f'Starting index : {start}')
    elif 'T' in line:
        _word = line.split(' ')
        byte_no = int(_word[2])
        start_index = int(_word[1])
        _number = list(_word[3])
        i = 0
        while True:
            print(f'{start_index} : {_number[i]}{_number[i + 1]}')
            start_index = start_index + 1
            byte_no = byte_no - 1
            if (byte_no == 0):
                break
            i = i + 2


     
# Name of program : COPY
# 1000 : 14
# 1001 : 10
# 1002 : 20
# 1003 : 11
# 1004 : 00
# 1005 : 0F
# 1006 : 01
# 1007 : 02
# 1020 : 10
# 1021 : 20
# 1022 : 21
# 1023 : 10
# 1024 : 11
# 1025 : 12
# 1026 : 18
# 1027 : 11
# 1028 : 81
# 1029 : AA
# Starting index : 001000