def add(a1,a2) :
    return a1+a2

def sub(a1,a2) :
    return a1-a2

def mul(a1,a2) :
    return a1*a2

def div(a1,a2) :
     if a2 == 0:
        return "Error: Cannot perform modulus by zero!"
     return a1 / a2

def mod(a1,a2) :
     if a2 == 0:
        return "Error: Cannot perform modulus by zero!"
     return a1 % a2

def pow(a1,a2) :
    return a1**a2

def flordiv(a1,a2):
    if a2 == 0:
        return "Error: Cannot perform floor division by zero!"
    return a1 // a2


print("=====Simple Calculator=====")

a1 = int(input("Enter a number :"))
a2 = int(input("Enter a number :"))

# Feature 
print("Choose an Operation :")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multipication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Power (**)")
print("7. Floor Division (//)")

c = input("Enter a choice 1 to 7 ")

if c == "1":
    print("Result is :",add(a1,a2))

elif c == "2":
    print("Result is :",sub(a1,a2))

elif c == "3":
    print("Result is :",mul(a1,a2))

elif c == "4":
    print("Result is :",div(a1,a2))

elif c == "5":
    print("Result is :",mod(a1,a2))

elif c == "6":
    print("Result is :",pow(a1,a2))

elif c == "7":
    print("Result is :",flordiv(a1,a2))









