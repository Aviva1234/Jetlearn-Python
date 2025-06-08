twoDList = [[1,2,3], [4,5,6], [7,8,9]]
print(twoDList[1][0])
twoDList[0][0] = "mango"
print(twoDList)
for row in twoDList:
    print(row)
    # for item in row:
    #     print(item)
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = [[0,0],[0,0]]
d = [[0,0],[0,0]]
rows = len(a)
col = len(a[0])
print(rows,col)
for i in range(rows):
    for j in range(col):
        #print(a[i][j])
        c[i][j] = a[i][j] + b[i][j]
        d[i][j] = a[i][j] - b[i][j]
print(c,d)