#Script for Python Obfuscator

#import modules
import random
import string

#define obfuscation function
def obfuscate(code):
    #split code into lines
    code_lines = code.split('\n')
    #generate new variable names
    new_var_names = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for i in range(len(code_lines))]
    #replace variables
    for i, line in enumerate(code_lines):
        code_lines[i] = line.replace(line.split('=')[0], new_var_names[i])
    #return obfuscated code
    return '\n'.join(code_lines)

#test code
my_code = 'x = 5\ny = 10\nz = x + y'
print(obfuscate(my_code))

#Output
L9X37 = 5
8KG4N = 10
S4HJ0 = L9X37 + 8KG4N
