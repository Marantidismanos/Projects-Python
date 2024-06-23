from logo import logo

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(logo)
    num1=float(input("Give 1st number: "))
    for i in operations:
        print(i)
    flag=True
    while flag!=False:
        operations_symbol=input("Pick an operation : ")
        num2=float(input("Give 2nd number: "))
        calcop=operations[operations_symbol]
        calc=calcop(num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {calc}")
        
        if (input(f"You want to make another calculation with {calc} ? Yy/Nn : ")=="y"):
            num1=calc
        else:
            flag=False
calculator()
