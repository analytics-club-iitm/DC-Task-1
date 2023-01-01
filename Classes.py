a=list(eval(input("Enter the array as a tuple")))
t=int(input("Enter your target integer"))
l=[]
f={}
print(a,"\n",t)
for i in range(len(a)):
    for j in range(len(a)):
        if (((a[i]+a[j])==t) and i!=j):
            l.append([i,j])
print(l)
for i in range(len(l)):
    f.update({i+1:l[i]})

print(f)
