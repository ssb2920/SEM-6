exp = input('Enter the expression: ')
exp_arr = exp.split(' ')
print(exp_arr)

sc = None
for char in exp_arr:
    if char[-1] == ";":
        sc = char[-1]
        char = char[:-1]

    try:
        num = float(char)
        print(char, ": Number Constant")
    except:
        if char.isalpha():
            print(char, ": Variable")            
        elif char[0] == '"' or char[0] == "'":
            print(char, ": Text Constant")
        else:
            print(char, ": Operator")
    finally:
        if sc:
            print(sc, ": Special Character")
            sc = None

# Enter the expression: a = b + c / 2.34; a = b - 'abc' + 6.0 + f;
# ['a', '=', 'b', '+', 'c', '/', '2.34;', 'a', '=', 'b', '-', "'abc'", '+', '6.0', '+', 'f;']
# a : Variable
# = : Operator
# b : Variable
# + : Operator
# c : Variable
# / : Operator
# 2.34 : Number Constant
# ; : Special Character
# a : Variable
# = : Operator
# b : Variable
# - : Operator
# 'abc' : Text Constant
# + : Operator
# 6.0 : Number Constant
# + : Operator
# f : Variable
# ; : Special Character