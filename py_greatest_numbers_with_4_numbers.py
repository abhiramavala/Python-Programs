# take 4 numbers from the user and find the greatest number

a = int(input("Enter the first number  \n"))
b = int(input("Enter the second number  \n"))
c = int(input("Enter the third number  \n"))
d = int(input("Enter the fourth number  \n"))

if a>b:
    if a>c:
        if a>d:
            print("a is the greatest")
        else:
            print("d is the greatest")
    else:
        print("c is the greatest")
elif b>a:
    if b>c:
        if b>d:
            print("b is the greatest")
        else:
            print("d is the greatest")
    elif b<c:
        if c>d:
            print("c is the greatest")
        else:
            print("d is the greatest")