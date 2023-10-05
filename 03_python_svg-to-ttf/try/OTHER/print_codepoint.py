
cs = {
    '?'
}

for c in cs:
    print(f"{c}", end='\t')
    word=ord(c.encode('unicode_escape'))
    print(word, end='\t')
    print(format(word, '#08x'))
