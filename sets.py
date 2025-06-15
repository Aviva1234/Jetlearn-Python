my1 = [1,2,3,4,1]
my2 = set(my1)
print(my2)
well = "Hello"
w = set(well)
w.update('Worldl')
w.remove('l')
w.discard('z')
print(w)
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1 | set2)
print(set1 & set2)
print((set1 - set2), (set2 - set1))
print(set2 ^ set1)