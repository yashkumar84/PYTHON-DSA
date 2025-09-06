#Set DS
myList = [1 ,2 , 3, 4 ,1 ,2 , 3, 1, 3, 2, 4, 4, 2,5 ,6]
mySet = {1 ,2 , 3, 4, 5 ,6 }

newSet = set(myList) #{1 ,2 ,3 ,4 , 5, 6}
print(newSet)

newSet.add(3)
print(newSet)

newSet.update()


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# x.update(y)
# print(x)
x.remove("apple")
print(x)
x.discard("banana")
print(x)

x = x.union([1 ,2 ,3 ])
print(x)

print(x.intersection([2 , "cherry" , 5]))

