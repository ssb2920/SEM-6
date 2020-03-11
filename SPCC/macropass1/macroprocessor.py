input_program = [line.strip() for line in open("input.txt")]
#Pass 1

macro_name_table,mdtable = [],[]
macro = 0
for linenumber,line in enumerate(input_program):
    if line == "MACRO":
        continue
    elif input_program[linenumber-1] == "MACRO":
        macro_name_table.append(line)
        #mdtable.append(line)
        macro = 1
    elif line == "MEND":
        macro = 0
    elif macro == 1:
        mdtable.append(line)
    else:
        continue

with open('mnt.txt','a') as mnt:
    for i in macro_name_table:
        mnt.write(i)
with open('mdt.txt','a') as mdt:
    for i in mdtable:
        i = i + '\n'
        mdt.write(i)

#Pass 2
macro_name_table = [line.strip() for line in open('mnt.txt')]
macro_definition_table = [line.strip() for line in open('mdt.txt')]
with open('expanded.txt','a+') as expanded_source_code:
    for linenumber,line in enumerate(input_program):
        if line in macro_name_table:
            for macro_lines in macro_definition_table:
                expanded_source_code.write(macro_lines + '\n')
        else:
            expanded_source_code.write(line + '\n')