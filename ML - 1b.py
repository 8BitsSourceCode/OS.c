a=int(input("a : "))
b=int(input("b : "))
op=input("Enter operator : ")
if op=='+':
    r=a+b
    print("Result :",r)
elif op=='-':
    r=a-b
    print("Result :",r)
elif op=='*':
    r=a*b
    print("Result :",r)
elif op=="/":
    r=a/b
    print("Result :",r)
else:
    print("Invalid operator")
