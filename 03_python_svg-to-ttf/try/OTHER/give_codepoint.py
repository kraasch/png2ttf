
import sys
import os

input_file=sys.argv[1]

with open(input_file) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        #if not c == os.linesep:
        if not c == '\n':
            print(f"{c}", end='\t')
            word=ord(c.encode('utf-8'))
            print(word, end='\t')
            print(format(word, '#04x'), end='\t')
            print()
