def balance_check(s):
    
    parent=["[","{","("]
    parent2=["]","}",")"]
    control=[]
    #primer descarte
    if len(s)%2 != 0 or s[0] not in parent:
        return False
    for i in range(0,len(s)):
        x=s[i]
        if x in parent:
            control.append(x)
            if x=="[":
                y="]"
            elif x == "{":
                y="}"
            elif x == "(":
                y=")"
        elif x in parent2:
            if x == y :
                control.pop()
                if len(control)>0:
                    if control[-1]=="[":
                        y="]"
                    elif control[-1] == "{":
                        y="}"
                    else:
                        y=")" 
            else:
                return False
    return len(control)==0



print (balance_check('{([{}])}'))

print (balance_check('[](){([[[]]])}'))

print (balance_check('()(){]}'))