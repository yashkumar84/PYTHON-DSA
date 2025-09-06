# String , List , Tuple , Set , Dictionary

#Strings

# a = "yash"
# a = a + " Tyagi"
# print(a)
# print(a.upper())
# print(a.lower())
# print(a)
# print(a.capitalize())
# print(a.count('a'))
# print(a.endswith('i'))

# a = a.upper()

#List

# list = [1, 2, 3, 4]
# list[2] = 5
# list1 = ["Yash" , "Vivek" ,"Aryan" , "Aman"]

# print(list1[-1])
# print(list1[1:3])

# print(list1[3 : 1 : -1])

# b = list1[3 : 1 : -1]
# print(b)

# for name in list1:
#     print(name)

# list1[1] = "Harsh"
# print(list1)

# list1.append("Vivek")
# print(list1)

# list1.insert(1 , "Vansh")
# print(list1)

# list1.reverse()
# print(list1)

# list1.extend(["Aarti" , "Arjun"])
# print(list1)
# list1.sort(reverse=True)

# print(list1)

# nestedList = [[1 , 2] ,[2 , 3]]
# print(nestedList[0][1])

#Tuple

# tuple1 = (1 ,2 , 3, 4, 5 ,2 , 2)
# print(tuple1[1])
# print(tuple1.count(2))
# print(tuple1.index(2 , 2 , 6))

# list2 = [ 1,2 , 3, 4]
# list2 = tuple(list2)

# myList = list(tuple1)
# print(myList)

myTuple = (1 , 2, 3, 4, 5)
myList = list(myTuple)
print(myList)

myStr = "Hello I am Yash Tyagi"
strList = myStr.split(" ")
print(strList)

print(''.join(strList))





