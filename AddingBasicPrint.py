#Defining a function and passing the arguments
def fun(name):
    # returning the value which i need to work inside the function
    return "Hey welcome to pst",name
#Taking the userInput for the name of the user and storing it into the variable a
a = input("Please Enter your name ")
#calling the function and passing the parameter and printing it
print(fun(a))