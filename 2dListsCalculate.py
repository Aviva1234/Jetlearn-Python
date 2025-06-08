l1 = [[1,2],[3,4],[3,100],[-59, -29]]
sum=0
maxNum = 0
minNum = 0
nums = []
rows = len(l1)
col = len(l1[0])
for i in range(rows):
    for j in range(col):
        sum = sum+ l1[i][j]
        nums.append(l1[i][j])
        if l1[i][j] > maxNum:
            maxNum = l1[i][j]
        if l1[i][j] < minNum:
            minNum = l1[i][j]
print(max(nums))
print(maxNum, minNum)
print(sum)