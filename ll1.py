n=int(input("No of terminals"))
term=[]
for i in range(n):
    term.append(input())
n=int(input("No of nonterminals"))
nonterm=[]
for i in range(n):
    nonterm.append(input())
n=int(input("No of prods"))
prod={}
for  i in range(n):
    lhs,rhs=input().split("->")
    prod[lhs]=list(rhs.split("|"))
start=input("Enter Start symbol")
FIRST={}
FOLLOW={}
def first(st):
    #print("called"+st)
    if(st==""):
        return set('$')
    res=set()
    if st in nonterm:
        for alt in prod[st]:
            res=res|first(alt)
    elif st=="" or st=="@":
        res={"@"}
    elif st in term:
        res={st}
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
        res={'$'}
    for nt,rhs in prod.items():
        for alt in rhs:
            for char in alt:
                if(char==st):
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
for i in nonterm:
    FIRST[i]=first(i)
    FOLLOW[i]=follow(i)
for i in nonterm:
    print(i+"\t"+str(FIRST[i])+"\t"+str(FOLLOW[i]))
table={}
term.append('$')
for i in nonterm:
    for j in term:
        if i not in table:
            table[i]=dict()
        table[i][j]=list()
def llparser():
    for lhs,rhs in prod.items():
        for alt in rhs:
            val=first(alt)
            if '@' in val:
                val=val-{'@'}
                val=val|follow(lhs)
            for v in val:
                if lhs+'->'+alt not in table[lhs][v]:
                    table[lhs][v].append(lhs+'->'+alt)
    for i in table.keys():
        print(i+"\t"+str(table[i]))
llparser()
        
