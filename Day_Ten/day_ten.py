#calculatr + usign docstrings
operations = {"1":"/", "2":"*", "3":"+", "4":"-"}
def second_num():
    """ask for the second number"""
    num = int(input("please tell the second number: "))
    return num
def mulitply(num1):
    """multiplye the numbers"""
    num2 = second_num()
    return num1 * num2
def adding(num1):
    """adding the two numbers"""
    num2 = second_num()
    return num1 + num2
def subtracting(num1):
    """subtracing the two numbers"""
    num2 = second_num()
    return num1 - num2
def deviding(num1):
    """deviding the two numbers"""
    num2 = second_num()
    return num1/num2
number = int(input("what number? "))

for a in operations:
    print(operations[a])
ask = input("which operation: ")

if ask == "/":
    print(deviding(number))
if ask == "*":
    print(mulitply(number))
if ask == "+":
    print(adding(number))
if ask == "-":
    print(deviding(number))