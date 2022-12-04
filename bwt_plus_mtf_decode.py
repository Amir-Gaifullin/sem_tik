from __future__ import print_function
from string import ascii_lowercase

SYMBOLTABLE = list(ascii_lowercase)

def mtf_decode(sequence, symboltable):
    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)

def read_code(text):
    with open(text,'r') as f:
        lines = f.readlines()
        code_input = [int(i) for i in list(lines[0].split(", "))]
        dictianory = list(lines[1].strip())
        index = int(lines[2])

        result = (code_input, dictianory, index)
    return result

def bwt_decode(bwt, index_bwt):
    table = [""] * len(bwt)  # Make empty table
    for i in range(len(bwt)):
        table = [bwt[i] + table[i] for i in range(len(bwt))]  # Add a column of r
        table = sorted(table)
    return table[index_bwt]

    
if __name__ == '__main__':
    text = r'code_mtf_input.txt'
    code = read_code(text)
    print(code)
    decode = mtf_decode(code[0], code[1])
    print('MTF decodes to %r' % decode)
    final_decode = bwt_decode(decode, code[2])
    print('BWT decodes to %r' % final_decode)
