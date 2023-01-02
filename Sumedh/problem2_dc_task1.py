class Person:
  def __init__(self, name):
    self.name = name
n= int(input("Enter range"))
a = [int(input("Enter a number")) for i in range(0,n)]
t= int(input("Enter target"))
d = {}
c=1
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            continue
        if(a[i]+a[j] == t):
            d[c] = [i,j]
            c+=1
p1 = Person(d)
print(p1.name)

