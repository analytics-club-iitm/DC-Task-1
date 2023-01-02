sols={}                        #dictionary for the solutions 
arr=[0,10,20,30,40,50,60]      #any values can be put for this array
num=50                         #the number that we want to check for 
k=1
for i in range(0,len(arr),1):
    for j in range(i+1,len(arr),1):
        if(arr[i]+arr[j]==num):
            sols[k]=[i,j]
            k=k+1

print(sols)