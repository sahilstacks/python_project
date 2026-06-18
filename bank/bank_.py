import mysql.connector

mydb=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bank_py"
                        )
mycursor=mydb.cursor()


def add():
    print("+-------------------------------------------------------------------+")
    print("|                       [ INSERT THE DETAILS ]                      |")
    print("+-------------------------------------------------------------------+")
    an=int(input("| [ Enter the Account Number ] "))
    n=input("| [ Enter the Name ] ")
    age=int(input("| [ Enter the Age ] "))
    o=input("| [ Enter the Occupation ]")
    ad=input("| [ Enter the Address ]")
    mb=int(input("| [ Enter the Mobile Number ]"))
    adhar=int(input("| [ Enter the Adhar Number ] "))
    amt=float(input("| [ Enter the Deposite Ammount ] "))
    at=input("| [ Enter the Account Type ( Saving/Rd/PPF/Current ) ] ")
    data=(an,n,age,o,ad,mb,adhar,amt,at)
    query="insert into account(Acc_no,Name,Age,Occu,Address,Mob_no,Adhar_no,Amt,Acc_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,data)
    mydb.commit()
    print("+-------------------------------------------------------------------+")
    print("|                    [ RECORD ADDED SUCESSFULLY ]                   |")
    print("+-------------------------------------------------------------------+")


def view():
    print("+-------------------------------------------------------------------+")
    print("|                 [ SELECT THE SEARCHING CRITERIA ]                 |")
    print("+-------------------------------------------------------------------+")
    print("| [ Press 1 for Account Number ] |")
    print("| [ Press 2 for Account Holder Name ] |")
    print("| [ Press 3 for Mobile Number ] |")
    print("| [ Press 4 for Adhar Number ] |")
    print("| [ Press 5 To View all Records ] |")
    ch=int(input("| [ Enter Your Choice ] "))
    print("+-------------------------------------------------------------------+")
    if (ch==1):
        an=int(input("| [ Enter the Account Number ] "))
        data=(an,)
        query="select * from account where Acc_no=%s"
        mycursor.execute(query,data)
        data=mycursor.fetchall()
        for i in data:
            print(i)
    elif (ch==2):
        n=input("| [ Enter the Account Holder Name ] ")
        data=(n,)
        query="select * from account where Name=%s"
        mycursor.execute(query,data)
        data=mycursor.fetchall()
        for i in data:
            print(i)
    elif (ch==3):
        mn=int(input("| [ Enter the Mobile Number ] "))
        data=(mn,)
        query="select * from account where Mob_no=%s"
        mycursor.execute(query,data)
        data=mycursor.fetchall()
        for i in data:
            print(i)
    elif (ch==4):
        ad=int(input("| [ Enter the Adhar_no ] "))
        data=(ad,)
        query="select * from account where Adhar_no=%s"
        mycursor.execute(query,data)
        data=mycursor.fetchall()
        for i in data:
            print(i)
    elif (ch==5):
        query="select * from account"
        mycursor.execute(query)
        data=mycursor.fetchall()
        print("|                     [ ALL CUSTOMER'S DETAILS ]                    |")
        print("+-------------------------------------------------------------------+")
        for d in data:
            for j in d:
                print(j,end=' ')
            print()


def deposit():
    print("+-------------------------------------------------------------------+")
    print("|                   [ ENTER THE DEPOSITE DETAILS ]                  |")
    print("+-------------------------------------------------------------------+")
    ac=int(input("| [ Enter the Account Number ] "))
    amt=float(input("| [ Enter the Deposite Amount ] "))
    m=input("| [ Enter the Month ] ")
    data=(ac,amt,m)
    query="insert into amt(Acc_no,Amt_deposite,Month) values(%s,%s,%s)"
    mycursor.execute(query,data)
    mydb.commit()


def close():
    print("+-------------------------------------------------------------------+")
    print("|                         [ CLOSE ACCOUNT ]                         |")
    print("+-------------------------------------------------------------------+")
    ac=int(input("| [ Enter the Account Number ] "))
    data=(ac,)
    query="delete from amt where Acc_no=%s"
    mycursor.execute(query,data)
    mydb.commit()
    query="delete from account where Acc_no=%s"
    mycursor.execute(query,data)
    mydb.commit()
    print("| Account of USER",ac," is DELETED")
    print("+-------------------------------------------------------------------+")


def menu():
    ch='y'
    print("+-------------------------------------------------------------------+")
    print("|                    [ WELCOME TO BANKING SOFTWARE ]                |")
    print("+-------------------------------------------------------------------+")
    while (ch=='y' or ch=='Y'):
        print("| [ Press 1 To ADD CUSTOMER ]                                       |")
        print("| [ Press 2 To VIEW CUSTOMER ]                                      |")
        print("| [ Press 3 To DEPOSITE MONEY ]                                     |")
        print("| [ Press 4 To CLOSE ACCOUNT ]                                      |")
        print("+-------------------------------------------------------------------+")
        try:
            num=int(input("| [ Enter Your Choice ] "))
        except ValueError:
            exit("WRONG CHOICE ! ")
        else:
            print("\n")
        if (num==1):
            add()
        elif(num==2):
            view()
        elif(num==3):
            deposit()
        elif(num==4):
            close()
        ch=input("| [ Do You Want To Continue... (Y/N)? ] ")
    

menu()
