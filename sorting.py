list = [5,2,8,1,3]

n = len(list)

for i in range(n):
    for j in range(0,n-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]

for i in range(n):
    if list[i] == 8:
        print(i+1)