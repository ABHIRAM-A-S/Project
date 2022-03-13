#python calculator program
#creating func for basic arithematic operations
def add(x,y):
    return x + y  

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y
print("Select Arithematic Operation to be done.")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
while True:
    option = input("Enter Option(1/2/3/4): ")  #collecting input from user
    if option in ('1','2','3','4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if option =='1':
            print("Result: ",add(num1, num2))
        elif option == '2':
            print("Result: ",substract(num1, num2))
        elif option =='3':
            print("Result:",multiply(num1, num2))
        elif option =='4':
            print("Result:",divide(num1, num2))
        #checking whether the user want to continue the operation
        same_process=input("Want to continue? (y/n):")
        if same_process == "n":
            break
    else:
        print("wrong input")



