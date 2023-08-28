import art
print(art.logo)

#Calculator

#Add function  
def add(n1,n2):
    return  n1 + n2

#Subtract function
def subtract(n1,n2):
    return n1-n2

#Multiply function
def multiply(n1,n2):
    return n1*n2

#Divide function
def divide(n1,n2):
    return n1/n2
#Create dictionary with operations
operations={
    "/":divide,
    "+":add,
    "*":multiply,
    "-":subtract 
}
#Create a calculator function
def calculator():
    num1=(float(input("What's the first number?: ")))
    #Loop to print all the operations the calculator can perform
    for symbol in operations:
        print(symbol)
    #Loop to keep the program running
    should_continue=True
    while should_continue:
        operation_symbol=input("Pick an operation: ")
        num2=(float(input("What's the next number?: ")))
        calc_function=operations[operation_symbol]
        answer=calc_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        
        
        #If user wants to continue or start a new calculation
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.: ").lower()=="y":
            num1=answer
        else:
            should_continue=False
            calculator()


calculator()