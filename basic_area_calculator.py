print("|-------------------------------------|")
print("| Welcome to Area Calculator Program  |")
print("|-------------------------------------|")
print("| Enter [Y] to Continue               |")
print("| Enter [N] to EXIT                   |")
print("|-------------------------------------|")

ch=input("| Enter [Y] or [N] : ")
if(ch=='Y' or ch=='y'):
    print("|-------------------------------------|")
    print("|-----------Area Calculator-----------|")
    print("|-------------------------------------|")
    print("| [ Enter 1 for: Area of Circle ]     |")
    print("| [ Enter 2 for: Area of Square ]     |")
    print("| [ Enter 3 for: Area of Rectangle ]  |")
    print("| [ Enter 4 for: Area of Cube ]       |")
    print("| [ Enter 5 for: Area of Cuboid ]     |")
    print("|-------------------------------------|")

    num=int(input("| Enter Your Choice for Calculation : "))
    print("|-------------------------------------|")
    if(num==1):
        r=float(input("| Enter the Radius of Circle : "))
        p=3.14
        ar=p*r*r
        print("|-------------------------------------|")
        print("| Area of a Circle is ", ar)
        print("|-------------------------------------|")
        
    elif(num==2):
        s=float(input("| Side of Square : "))
        ar=s*s
        print("|-------------------------------------|")
        print("| Area of Square is : ", ar)
        print("|-------------------------------------|")
        
    elif(num==3):
        l=float(input("| Enter the Length of Rectangle : "))
        b=float(input("| Enter the Width of Rectangle : "))
        ar=l*b
        print("|-------------------------------------|")
        print("| Area of Rectangle is : ", ar)
        print("|-------------------------------------|")
        
    elif(num==4):
        s=float(input("| Enter the Side of Cube : "))
        ar=6*s*s
        print("|-------------------------------------|")
        print("| Area of Cube is : ", ar)
        print("|-------------------------------------|")
        
    elif(num==5):
        l=float(input("| Enter the Length of Cuboid : "))
        b=float(input("| Enter the Width of Cuboid : "))
        h=float(input("| Enter the Height of Cuboid : "))
        ar=2*(l*b+b*h+h*l)
        print("|-------------------------------------|")
        print("| Area of Cuboid : ", ar)
        print("|-------------------------------------|")
        
    else:
        print("| Wrong Input....!                    |")
        print("|-------------------------------------|")

elif(ch=='N' or ch=='n'):
    print("|-------------------------------------|")
    print("| Exiting the Program...              |")
    print("|-------------------------------------|")
    
else:
    print("|-------------------------------------|")
    print("| Wrong Choice.....                   |")
    print("|-------------------------------------|")