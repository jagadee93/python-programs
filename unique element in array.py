n=[x for x in input().split()]
n.sort()
uniq=[]
for x in n:
    if n.count(x)==1:
        uniq.append(x)
s="".join(uniq)
print(s)
