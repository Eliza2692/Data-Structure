def rev_word(s):
    lista=s.split()
    s=" ".join(lista[::-1])
    return s

print (rev_word('Hi John,   are you ready to go?'))
