import sys
sys.setrecursionlimit(60)
no_nonterm=int(input("Enter no of non terminals"))
nonterm=[]
print("Enter non terminals")
for i in range(no_nonterm):
    nonterm.append(input())
no_term=int(input("Enter no of terminals"))
print("Enter terminals")
term=[]
for i in range(no_term):
    term.append(input())
start=input("Enter start symbol")
no_of_prod=int(input("No of prod"))
prod=[]
print("Enter productions")
for i in range(no_of_prod):
    prod.append(input())
productions={}
for rule in prod:
    lhs,rhs=rule.split("->")
    productions[lhs]=list(rhs.split("|"))
FIRST={}
FOLLOW={}
def first(st):
    res=set()
    if st in nonterm:
        alt=productions[st]
        for a  in alt:
            res=res|first(a)
    elif st in term:
        res={st}
    elif st =="" or st=="@":
        res={'@'}
    else:
        r=first(st[0])
        if '@' in r:
            i=1
            while('@' in r):
                res=res|r-{'@'}
                if st[i:] in term:
                    res=res|st[i:]
                elif st=="":
                    res=res|{'@'}
                    break
                r=first(st[i:])
                res=res|r-{'@'}
                i+=1
        else:
            res=res|r
    return res
def follow(st):
    res=set()
    if(st==start):
        res=res|{'$'}
    for nt,rhs in productions.items():
        for alt in rhs:
            for char in alt:
                if char==st:
                    followstr=alt[alt.index(char)+1:]
                    if(followstr==""):
                        if(st==nt):
                            continue
                        else:
                                
                            res=res|follow(nt)
                    else:
                        r=first(followstr)
                        if '@' in r:
                            res=res|r-{'@'}
                            res=res|follow(nt)
                        else:
                            res=res|r
    return res


    
print(term,nonterm)
for i in nonterm:
    FIRST[i]=set(first(i))
for i in nonterm:
    FOLLOW[i]=set(follow(i))
for i in nonterm:
    print(i+"\t\t"+str(FIRST[i])+"\t\t"+str(FOLLOW[i]))


