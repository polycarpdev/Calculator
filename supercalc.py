       ### IMPORT SPECIAL FUNCTIONS FROM THE MATH LIBRARY

from math import*


#####function  prompts the user to enter his/her name and says hi to them
def greet_user(name):
    
    print("\n Hello " + name.upper() + " !")##display te name in caps
name= input("\n Please input your name: ") ##get the name as input from the user
greet_user(name)

## asks the user to choose which operation they want to perform ##

operation= input("\n Choose the operation you wanna perform (reply with number 1,2,3,4 or 5) \n 1. Basic operations(+, -, /, *)\n 2. Square root \n 3. Square \n 4. Cube \n 5. Compare 2 numbers\n \n Operation Number: ")

###### I use the IF statement to choose among the operations to perform ###

       #### BASIC CALCULATOR ####
if operation=="1":
    ##this prints the initialization 
    
    print("\n Basic Calculator for 2 numbers\n")
    ## initialize num1 and get it as input from the user
    num1=float(input("Enter the first number : "))
    
                   ###### inputing the next operation
    op= input("enter the operator(e.g. +, -, *, /) : ")
    num2=float(input("Enter the second number : "))
    ##prints the error message if the choice is out of range
    error_message="\n invalid operator ! "
    
    ####this is an if-else statement to find the sum
    
    if op=="+":
        print("The sum is " + str(num1+num2))
        
        
    elif op=="-":
        print("The sum is " + str(num1-num2))
        
        
    elif op=="*":
        print("The sum is " + str(num1*num2))
        
        
    elif op=="/":
        print("The sum is " + str(num1/num2))
        
        
    else:
            #print the error message when
            print(error_message.upper() + "reload the program and repeat")
            
            
    ###### SRUARE ROOT ######       
elif operation=="2":
    #get the number as input from the user
    num=float(input("Enter the number to find the square root: "))
    #displa the result
    print("The square root of "+ str(num) + " is " + str(sqrt(num)))
    
    ###### SQUARE ######
elif operation=="3":
    ##variable initialisation
    num=float(input("Enter the number to square : "))
    
    print("The square of " + str(num) + " is " + str(num*num))
    
    
    ###### CUBE #####
elif operation=="4":
    
    #########
    num=float(input("Enter the number to find the cube : "))
    print("The cube of " + str(num) + "  is  " + str(num*num*num))



 ##### FINDING THE LARGEST NUMBER ######
elif operation=="5":

###function to pass 2 parameters(numbers)
    def largest(n1, n2):
        if n1>=n2:
            return n1
        else:
            return n2
        
        
        #####get the numbers as input from the user
    
    n1=float(input('Enter the first number : '))
    #initialize the input from the sum
    n2=float(input('Enter the second number : '))

    
    ### displaying the greater number
    print("The greater number is : " + str(largest(n1, n2)))


else:
    #This is gonna display the error message
    error_message="\n invalid selection ! "
    
        ######  this prints the error message in upper case #####
    
    
    
                         ####if the selecion is out of range
print(error_message.upper() + "Run the program again and select  choice within the range!")
    
    
                       ################     IS THIS NOT THE END...      ########################
    
    