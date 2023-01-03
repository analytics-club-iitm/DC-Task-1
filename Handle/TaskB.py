class sum:
    def find(self,target,num):
        x = 1
        dict1 = dict()
        for i in range(len(num)):
            for j in range(len(num)):
                if target==num[i]+num[j] :
                    dict1[x] = [i,j]
                    x = x + 1
        return dict1

s = sum()
targ = int(input("target:"))
nums = list(map(int,input().split()))
print('The list is:', nums)
#for k in range(val):
 #   nums.append(int(input()))
print(s.x)
print(s.find(targ,nums))


