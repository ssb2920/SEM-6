### MOT and POT is constant
MOT = {
        "A": {"BO": "5A", "ILen": 4, "IForm": "RX"},
        "L": {"BO": "5A", "ILen": 4, "IForm": "RX"},
        "AH": {"BO": "4A", "ILen": 4, "IForm": "RX"},
        "ST": {"BO": "4E", "ILen": 4, "IForm": "RR"},
        "AL": {"BO": "5A", "ILen": 4, "IForm": "RX"},
        "AR": {"BO": "4E", "ILen": 2, "IForm": "RR"},
        "ALR": {"BO": "5A", "ILen": 2, "IForm": "RX"}
}
POT = {"DROP": "P1DROP", "END": "P1END", "EQU": "P1EQU", "START": "P1START", "USING": "P1USING"}
ST = {}

### PASS1
with open('assem.txt', 'r') as f:
    lines = f.readlines()

    entries = []
    for line in lines:
        entry = ''
        line = line.strip('\n')
        _line = line.replace(', ', ',')
        words = _line.split(' ')

        # Generate Symbol Table
        if len(words) > 2:
    
            # Get the start address
            if words[1] == 'START':
                start_len = int(words[2])
                curr_addr = start_len
                entry = words[2] + '\n'
                ST[words[0]] = {"ADDR": curr_addr, "LEN": start_len + 4, "RELOC": "R"}

            # Adds entry in symbol table using label field
            else:
                ST[words[0]] = {"ADDR": curr_addr, "LEN": start_len + 4, "RELOC": "R"}
                entry = str(curr_addr) + '\n'
                curr_addr += 4
        
        # These lines have no labels
        # Generate address space
        else:
            # Using gives us base address which we store in else 
            if words[0] != 'USING':
                # Locate operands, these are lines that have operations (no labels either)
                if words[0] != 'END':
                    m = words[0]
                    operands = words[1].split(',')
                    # Finds forward references and leaves them blank
                    for o in operands:
                        try:
                            char = int(o)
                        except:
                            entry = str(curr_addr) + ' ' + MOT[m]['BO'] + " _ (0, " + str(base_pos)  + ')\n'
                            curr_addr += MOT[m]['ILen']
                # If there is no operation or FR
                # Just print current address and move next
                else:
                    entry = str(curr_addr) + '\n'
            # Get base address
            else:
                base_pos = int(words[1].split(',')[1])
                entry = str(start_len) + '\n'
        entries.append(entry)

for e in entries:
    print(e),

### PASS2
for i, entry in enumerate(entries):
    entry = entry.strip('\n')
    if '_' in entry:
        line = lines[i].replace(',', '')
        line = line.strip('\n')
        words = line.split(' ')
        for w in words:
            # Check if word in symbol table and replace
            # Uses the blank spaces declares above to easily identify forward references 
            # and replace them in the symbol table
            if w in ST.keys():
                entries[i] = entry.replace('_', str(ST[w]['ADDR']))
                entries[i] += '\n'

with open('assem_out.txt', 'w') as f:
    f.writelines(entries)

# INPUT
# PG1 START 100
# USING *, 15
# L 1, four
# A 1, five
# ST 1, temp
# five DC F'5'
# four DC F'6'
# temp DS 1F
# END

# PASS 1
# 100
# 100
# 100 5A _ (0, 15)
# 104 5A _ (0, 15)
# 108 4E _ (0, 15)
# 112
# 116
# 120
# 124

# PASS 2
# 100
# 100
# 100 5A 116 (0, 15)
# 104 5A 112 (0, 15)
# 108 4E 120 (0, 15)
# 112
# 116
# 120
# 124