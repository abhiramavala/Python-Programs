#Take 3 values from the user and find the greatest.

a = int(input("Enter the first number  \n"));
b = int(input("Enter the second number  \n"));
c = int(input("Enter the third number  \n"));
if a>b:
    if a>c:
        print("a is greatest");
    else:
        print("c is greatest");
elif b>a:
    if b>c:
        print("b is greatest");
    else:
        print("c is greatest");