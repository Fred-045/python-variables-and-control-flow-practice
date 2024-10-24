# Simple Calculator with Conditionals
#asking for input
p1 = float(input("Enter your price:"))
p2 =float(input("Enter your price:"))
p3 = float(input("Enter your price"))
counter=input("Enter the operation(+,-,*,/):")
if counter =='+':
    result =p1 + p2 + p3
    print(f"{p1}+{p2}+{p3}={result}")
elif counter =='-':
    result= p3-p2
    print(f"{p3}-{ p2} = {result}" )
elif counter =='*':
    result =p1 * p2 * p3
    print(f"{p1} * {p2} * {p3} = {result}")
elif counter == '/':
    result =p3/p2
    print(f"{p3}/{p2}={result}")
else:
        print("Error: Division by zero is not allowed.")
