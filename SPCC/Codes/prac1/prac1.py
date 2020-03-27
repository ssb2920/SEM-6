import random

ops = ['+', '-', '/', '*', '=', '%']

table = {}

def free_addr():
    addr_list = [table[sym]['addr'] for sym in table]
    addr = random.randint(0, 2000)
    while addr in addr_list:
        addr = random.randint(0, 2000)
    return addr

def create_table(exp):
    for sym in exp:
        if sym in ops:
            table[sym] = {"addr": free_addr(), "type": "operator"}
        else:
            table[sym] = { "addr": free_addr(), "type": "identifier"}
    return table

def search_table(sym):
    if sym in table:
        print(f"Symbol: {sym} | Address: {table[sym]['addr']} | Type: {table[sym]['type']}")
    else:
        print("Symbol not in Symbol Table")

def add_symbol(sym):
    _type = "identifier"
    if sym in ops:
        _type = "operator"
    table[sym] = {"addr": free_addr(), "type": _type}

def remove_symbol(sym):
    del table[sym]

def print_table():
    for sym in table:
        print(f"Symbol: {sym} | Address: {table[sym]['addr']} | Type: {table[sym]['type']}")


while True:
    _choice = int(input("1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit\nEnter your choice: "))
    
    if _choice == 1:
        exp = input("Enter expression: ")
        table = create_table(exp)
    
    if _choice == 2:
        sym = input("Enter symbol to search: ")
        search_table(sym)

    if _choice == 3:
        sym = input("Enter symbol: ")
        add_symbol(sym)

    if _choice == 4:
        sym = input("Enter symbol to remove: ")
        remove_symbol(sym)

    if _choice == 5:
        print_table()

    if _choice == 6:
        break

    
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 1
# Enter expression: D=A+B*C
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 6
# (new_main) kad99kev@kad99kev SPCC % python prac1.py
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 1
# Enter expression: D=A+B*C
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 5
# Symbol: D | Address: 1574 | Type: identifier
# Symbol: = | Address: 1192 | Type: operator
# Symbol: A | Address: 199 | Type: identifier
# Symbol: + | Address: 1520 | Type: operator
# Symbol: B | Address: 921 | Type: identifier
# Symbol: * | Address: 1084 | Type: operator
# Symbol: C | Address: 579 | Type: identifier
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 1
# Enter expression: X=W/M-L
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 5
# Symbol: D | Address: 1574 | Type: identifier
# Symbol: = | Address: 356 | Type: operator
# Symbol: A | Address: 199 | Type: identifier
# Symbol: + | Address: 1520 | Type: operator
# Symbol: B | Address: 921 | Type: identifier
# Symbol: * | Address: 1084 | Type: operator
# Symbol: C | Address: 579 | Type: identifier
# Symbol: X | Address: 1389 | Type: identifier
# Symbol: W | Address: 1879 | Type: identifier
# Symbol: / | Address: 772 | Type: operator
# Symbol: M | Address: 1863 | Type: identifier
# Symbol: - | Address: 1670 | Type: operator
# Symbol: L | Address: 1749 | Type: identifier
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 3
# Enter symbol: E
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 5
# Symbol: D | Address: 1574 | Type: identifier
# Symbol: = | Address: 356 | Type: operator
# Symbol: A | Address: 199 | Type: identifier
# Symbol: + | Address: 1520 | Type: operator
# Symbol: B | Address: 921 | Type: identifier
# Symbol: * | Address: 1084 | Type: operator
# Symbol: C | Address: 579 | Type: identifier
# Symbol: X | Address: 1389 | Type: identifier
# Symbol: W | Address: 1879 | Type: identifier
# Symbol: / | Address: 772 | Type: operator
# Symbol: M | Address: 1863 | Type: identifier
# Symbol: - | Address: 1670 | Type: operator
# Symbol: L | Address: 1749 | Type: identifier
# Symbol: E | Address: 1194 | Type: identifier
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 4
# Enter symbol to remove: D
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 5
# Symbol: = | Address: 356 | Type: operator
# Symbol: A | Address: 199 | Type: identifier
# Symbol: + | Address: 1520 | Type: operator
# Symbol: B | Address: 921 | Type: identifier
# Symbol: * | Address: 1084 | Type: operator
# Symbol: C | Address: 579 | Type: identifier
# Symbol: X | Address: 1389 | Type: identifier
# Symbol: W | Address: 1879 | Type: identifier
# Symbol: / | Address: 772 | Type: operator
# Symbol: M | Address: 1863 | Type: identifier
# Symbol: - | Address: 1670 | Type: operator
# Symbol: L | Address: 1749 | Type: identifier
# Symbol: E | Address: 1194 | Type: identifier
# 1. Create table 2. Search table 3. Enter symbol 4. Remove symbol 5. View table 6. Exit
# Enter your choice: 6