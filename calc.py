def add(a , b):
    print(a + b);

def sub(a , b):
    print(a - b)

def mul(a , b):
    print(a * b)

def div(a , b):
    print(a / b)

def mod(a , b):
    print(a % b)

def pow(a , b):
    print(a ** b)

d = True
while(d):
    d = input("Do you want To proceed\n")
    if(d != "y"):
        d = False
        break
    a = int(input("Enter the first Number\n"))
    b = int(input("Enter the second Number\n"))
    c = input("Enter the Operator\n")


    match c:
        case '+':
            add(a , b)
        case '-':
            sub(a , b)
        case "*":
            mul(a , b)
        case '/':
            div(a , b)
        case '%':
            mod(a , b)
        case '^':
            pow(a , b)
        


