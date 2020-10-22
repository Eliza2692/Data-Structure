
def anagram (s1,s2):
    #eliminar espacios
    s1= ''.join(s1.split())
    s2= ''.join(s2.split())
    #tomar longitud
    len1=len(s1)
    len2=len(s2)
    #comparar longitud
    if len1==len2:
        comp=len1
        for i in s1:
            for j in s2:
                if i==j:
                    j=""
                    comp-=1
                    break
        if comp==0:
            return True
        else:
            return False
    else:
        return False

    
print (anagram("clint eatwood","old west action"))
Print (hi)