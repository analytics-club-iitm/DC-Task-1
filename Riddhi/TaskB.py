arr = []
n = int(input("Enter the list size "))
S=int(input("target="))
print("numbers=")
for i in range(0, n):
    item = int(input())
    arr.append(item)

i=0
j=0
c=1
data={}
for i in range(0,n,1):
  for j in range(0,n,1):
    if(arr[i]+arr[j]==S):
      data[c]=[i,j]
      c=c+1
print(data)arr = []
n = int(input("Enter the list size "))
S=int(input("target="))
print("numbers=")
for i in range(0, n):
    item = int(input())
    arr.append(item)

i=0
j=0
c=1
data={}
for i in range(0,n,1):
  for j in range(0,n,1):
    if(arr[i]+arr[j]==S):
      data[c]=[i,j]
      c=c+1
print(data)
arr = []
n = int(input("Enter the list size "))
S=int(input("target="))
print("numbers=")
for i in range(0, n):
    item = int(input())
    arr.append(item)
arr = []
n = int(input("Enter the list size "))
S=int(input("target="))
print("numbers=")
for i in range(0, n):
    p = int(input())
    arr.append(p)

i=0
j=0
c=1
data={}
for i in range(0,n,1):
  for j in range(0,n,1):
    if(arr[i]+arr[j]==S):
      data[c]=[i,j]
      c=c+1
print(data)

