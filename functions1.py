#Functions are Block of codes

a = 10
b = 20

print(a + b)

c = 50
d = 60
print(c + d)
#Positional Arguments
def addTwoNumber(a , b ):
    print(a + b)
    # return a + b

h = addTwoNumber(10 ,20)
print(h)

#keyword arguments


def subTwoNum(a , b):
    print(a - b)

subTwoNum(b= 30,  a =10)

#deafault Arguments

def mul(a  , b = 20):
    print(a * b)

mul( 15)


#args


def addManyNumbers(*args):
    sum = 0
    for ele in args:
        sum += ele
    print(sum)

addManyNumbers(10 , 20 , 50 , 60 , 34 , 32 , 23 )

#kwargs

def printInfo(**kwargs):
    print(kwargs)

printInfo(name = "yash" , age = 17 , hindi = 34 , maths = 45)