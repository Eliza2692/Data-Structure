def compress(s):
    if s=="":
        return ""
    lens=len(s)
    i=n=0
    r=s[0]
    while i<lens:
        if r[-1]==s[i]:
            n+=1
        else:
            r+=str(n)
            r+=s[i]
            n=1
        i+=1
    r+=str(n)
    return r


print (compress('AAaaBBBbbb'))