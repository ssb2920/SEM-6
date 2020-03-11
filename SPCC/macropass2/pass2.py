input_program = [line.strip() for line in open("input.txt")]
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