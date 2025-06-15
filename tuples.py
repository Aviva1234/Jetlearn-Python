fruits = ('apple', 'banana','mango','strawberry')
a,b,c,d=fruits
print(fruits,"variables",a,b,c,d)
myT = ((1,2),[3,4])
print(myT[1][0])
myT[1][0] = 5
print(myT)
if 'apple' in fruits:
    print("yes")
if 'apple' in myT:
    print("yes")
else:
    print("no")
for item in myT:
    for c in item:
        print(c)
# del(fruits)
# print(fruits)