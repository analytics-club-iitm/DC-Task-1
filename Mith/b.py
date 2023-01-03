class Target_Store:
    def __init__(self,list,target):
        self.list = list
        self.target = target
        d = {}
        c = 1
        for i in range(len(list)):
            for j in range(i+1,len(list)):
                if list[j] == target - list[i]:
                    d[c] = (i+1,j+1)
                    d[c+1] = (j+1,i+1)
                    c+=2
        self.dict = d
l = eval(input('Enter the list:'))
target  =int(input("Enter the target:"))
t = Target_Store(l,target)
print(t.dict)
