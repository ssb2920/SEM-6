import re

MDT = {'MDTC': [], 'DEFN': []}
MNT = {'MNTC': [], 'NAME': [], 'MDT IDX': []}
ALA = {'IDX': [], 'ARG': []}
MDTC = 1
MNTC = 1

### PASS 1
with open('macro_txt.txt', 'r') as f:
    lines = f.readlines()
    is_macro = False
    old_MNTC = MNTC

    for line in lines:
        line = line.strip('\n')
        
        if is_macro:
            if old_MNTC != MNTC:
                ### Preparing MNT
                MNT['NAME'].append(line.split(' ')[0])
                MNT['MNTC'].append(old_MNTC)
                MNT['MDT IDX'].append(MDTC)

                ### Preparing ALA
                try: 
                    ALA['IDX'][-1]
                    idx = ALA['IDX'][-1] + 1
                except:
                    idx = 1
                for word in line.split(' '):
                    if '&' in word:
                        ALA['IDX'].append(idx)
                        word = word.replace(',', '')
                        ALA['ARG'].append(word)
                        idx += 1

                ### Preparing MDT
                MDT['MDTC'].append(MDTC)
                MDTC += 1
                MDT['DEFN'].append(line)

                old_MNTC = MNTC
            else:
                ### Preparing MDT
                MDT['MDTC'].append(MDTC)
                MDTC += 1
                for word in line.split(' '):
                    if word in ALA['ARG']:
                        line = line.replace(word,  '#' + str(ALA['ARG'].index(word) + 1))
                MDT['DEFN'].append(line)

        if line == 'MACRO':
            is_macro = True
            MNTC += 1
        if line == 'MEND':
            is_macro = False

print(MNT)
print(MDT)
print(ALA)

### PASS 2
with open('marco_esc.txt', 'w') as w:
    with open('macro_txt.txt', 'r') as f:
        lines = f.readlines()
        is_macro = False
        mac_def = False

        for line in lines:
            line = line.strip('\n')

            # Do not perform operations if it is a macro definition
            if line == 'MACRO':
                mac_def = True
            if line == 'MEND':
                mac_def = False

            # Check if macro called
            mname = line.split(' ')[0]
            if mname in MNT['NAME'] and not mac_def:
                is_macro = True
                idx = MNT['NAME'].index(mname)
                MDTP = MNT['MDT IDX'][idx]

                # Get arguments
                args = []
                for word in line.split():
                    if word != mname:
                        word = word.replace(',', '')
                        args.append(word)
                
                # Replace macro call
                while is_macro:
                    line = MDT['DEFN'][MDTP]

                    # Find number of arguments to be replaced
                    arg_idx = 0
                    for i in range(line.count('#')):
                        arg_idx = line.index('#', arg_idx) + 1
                        ala_idx = int(line[arg_idx]) - 1
                        line = line.replace(line[arg_idx - 1] + str(ala_idx + 1), args[ala_idx], 1)
                        
                    # If end of macro break
                    if line == 'MEND':
                        is_macro = False
                        break
                    MDTP += 1
                    w.write(line + '\n')
            else:
                w.write(line + '\n')

# INPUT          
# MACRO
# incr &A1, &A2
# A 1, &A1
# A 2, &A2
# MEND
# PG1 START
# USING *, 15
# L 1, five
# A 1, four
# incr five, four
# ST 1, temp
# incr four, five
# five DC F'5'
# four DC F'6'
# temp DS 1F
# END

# EXPANDED
# MACRO
# incr &A1, &A2
# A 1, &A1
# A 2, &A2
# MEND
# PG1 START
# USING *, 15
# L 1, five
# A 1, four
# A 1, five
# A 2, four
# ST 1, temp
# A 1, four
# A 2, five
# five DC F'5'
# four DC F'6'
# temp DS 1F
# END
