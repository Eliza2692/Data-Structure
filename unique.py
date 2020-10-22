def uni_char(s):
    for i in s:
        n=s.count(i)
        if n!=1:
            return False
    return True

print (uni_char('abcde'))

print (uni_char('aabccdee'))