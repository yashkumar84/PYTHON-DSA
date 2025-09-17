f = open('./text.txt' , '+a')
text= f.read()
print(text)

f.write("Hello, I am Yash , and Now I am Here to Tell You About Python")
f.close()


#Exception Handling 

try:
    with open('./text.txt' ) as file:
        file.write('hello My name is yash')
except IOError as e:
    print("Ha ha There is Some Issue We will Come Back" ,e )

print("My name is yash and i am in the file filehandling")


try:
    n = int(input("Enter the Input"))
    if(n % 2 == 0):
        print("We are getting the Correct Even Number")
    else:
        raise ValueError('"Hey Please Give the Even Number"')
       
except ValueError as e:
    print("Hey there , we are Experiencing Error " , e)

finally:
    print("I Executes Everytime")

# print(10 / 0)

