### Considering Grammar ###
# S -> 0B | 1A
# A -> 0 | 0S | 1A
# B -> 1 | 1S | 0B

from six.moves import input

i = 0
check = 0

def S(inp):
    global i
    global check
    if(inp[i] == '0'):
        match(inp, '0')
        B(inp)
    elif(inp[i] == '1'):
        match(inp, '1')
        A(inp)
    return check

def A(inp):
    global i
    global check

    if(inp[i] == '0'):
        match(inp, '0')
        if(inp[i] == '$'):
            match(inp, '$')
            check = 1
            return check
        else:
            S(inp)
    elif(inp[i] == '1'):
        match(inp, '1')
        A(inp)
    return check

def B(inp):
    global i
    global check

    if(inp[i] == '1'):
        match(inp, '1')
        if(inp[i] == '$'):
            match(inp, '$')
            check = 1
            return check
        else:
            S(inp)
    elif(inp[i] == '0'):
        match(inp, '0')
        B(inp)
    return check

def match(inp, t):
    global i
    if(inp[i] == t):
        i = i + 1
    else:
        print('Error')

if __name__ == "__main__":
    inp = input('Enter input string: ')
    inp = list(inp)
    inp.append('$')
    val = S(inp)
    if(val == 1):
        print('Valid String')
    else:
        print('Error: Invalid String')


####### Output #######
# Enter input string: 01
# Valid String
#
# Enter input string: 110
# Valid String
#
# Enter input string: 01110    
# Valid String
#
# Enter input string: 01111001
# Valid String
#
# Enter input string: 0110
# Valid String
#
# Enter input string: 001110
# Valid String
#
# Enter input string: 001100
# Error: Invalid String
#
# Enter input string: 0100
# Error: Invalid String