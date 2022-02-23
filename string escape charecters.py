n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
print(" ".join(str(x)for x in l))
if(l[-1]%2==0):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
