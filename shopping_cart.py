def greeting():
    print("|---------------------------------------|")
    print("         WELCOME TO RYZEN STORE          ")
    print("|---------------------------------------|")

def show_items():
    print("|  SNo  |      ITEMS       |   Price(₹) |")
    print("|---------------------------------------|")
    print("|   1   |  Battlefield 6   |   ₹3,999   |")
    print("|   2   |   ARC Raiders    |   ₹4,399   |")
    print("|   3   |  Borderlands 4   |   ₹2,499   |")
    print("|   4   |  Cyberpunk 2077  |   ₹3,490   |")
    print("|   5   |   Helldivers 2   |   ₹2,499   |")
    print("|   6   |       Stray      |   ₹1,499   |")
    print("|   7   |     Takken 8     |   ₹1,499   |")
    print("|   8   |    Elden Ring    |   ₹1,999   |")
    print("|   9   |  GTA V Enhanced  |   ₹3,999   |")
    print("|   10  |      GTA VI      |   ₹9,999   |")
    print("|---------------------------------------|")

def buy(buy_total):
    print("| What Do You Want To Purchase           ")
    order_sno=input("| Please Gave The SNo To Buy : ")
    print("|---------------------------------------|")
    if(order_sno=='1'):
        buy_total=buy_sno1(buy_total)
    elif(order_sno=='2'):
        buy_total=buy_sno2(buy_total)
    elif(order_sno=='3'):
        buy_total=buy_sno3(buy_total)
    elif(order_sno=='4'):
        buy_total=buy_sno4(buy_total)
    elif(order_sno=='5'):
        buy_total=buy_sno5(buy_total)
    elif(order_sno=='6'):
        buy_total=buy_sno6(buy_total)
    elif(order_sno=='7'):
        buy_total=buy_sno7(buy_total)
    elif(order_sno=='8'):
        buy_total=buy_sno8(buy_total)
    elif(order_sno=='9'):
        buy_total=buy_sno9(buy_total)
    elif(order_sno=='10'):
        buy_total=buy_sno10(buy_total)
    else:
        print("|            Invalid SNo...!            |")
        print("|---------------------------------------|")
    return buy_total

def buy_sno1(buy_total):
    n=int(input("| How many copies of Battlefield 6 : "))
    p=n*3999
    buy_total=buy_total+p
    print("| Price of ",n," Battlefield 6 : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def buy_sno2(buy_total):
    n=int(input("| How many copies of ARC Raiders : "))
    p=n*4399
    buy_total=buy_total+p
    print("| Price of ",n," ARC Raiders : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def buy_sno3(buy_total):
    n=int(input("| How many copies of Boderlands 4 : "))
    p=n*2499
    buy_total=buy_total+p
    print("| Price of ",n," Boderlands 4 : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def buy_sno4(buy_total):
    n=int(input("| How many copies of Cyberpunk 2077 : "))
    p=n*3490
    buy_total=buy_total+p
    print("| Price of ",n," Cyberpunk 2077 : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def buy_sno5(buy_total):
    n=int(input("| How many copies of Helldivers 2 : "))
    p=n*2499
    buy_total=buy_total+p
    print("| Price of ",n," Helldivers 2 : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def buy_sno6(buy_total):
    n=int(input("| How many copies of Stray : "))
    p=n*1499
    buy_total=buy_total+p
    print("| Price of ",n," Stray : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def buy_sno7(buy_total):
    n=int(input("| How many copies of Takken 8 : "))
    p=n*1499
    buy_total=buy_total+p
    print("| Price of ",n," Takken 8 : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def buy_sno8(buy_total):
    n=int(input("| How many copies of Elden Ring : "))
    p=n*1999
    buy_total=buy_total+p
    print("| Price of ",n," Elden Ring : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def buy_sno9(buy_total):
    n=int(input("| How many copies of GTA 5 Enhanced : "))
    p=n*3999
    buy_total=buy_total+p
    print("| Price of ",n," GTA 5 Enhanced : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def buy_sno10(buy_total):
    n=int(input("| How many copies of GTA 6 : "))
    p=n*9999
    buy_total=buy_total+p
    print("| Price of ",n," GTA 6 : ₹ ", p)
    print("|---------------------------------------|")
    return buy_total

def calculate_discount(pay):
    d=0
    if(pay>=5000 and pay<=9000):
        d=pay*(0.025)  #2.5% discount
    if(pay>9000):
        d=pay*(0.12) #10% discount
    return d

#Main Body
buy_total=0
#discount=0
greeting()
while True:
    show_items()
    buy_total=buy(buy_total)
    print("| Enter 1 for Buy More")
    print("| Enter 2 for Bill")
    c=input("| Enter Your Choice : ")
    print("|---------------------------------------|")
    if (c=='1'):
        continue
    elif (c=='2'):
        break
    else:
        print("|              Wrong Choice             |")
        print("|---------------------------------------|")

original_amount=buy_total
dis_count=calculate_discount(original_amount)
after_discount=original_amount-dis_count
gst=after_discount*(18 / 100)
total_bill=gst+after_discount
print("|---------------------------------------|")
print("| AMOUNT :                  ₹", original_amount)
print("| DISCOUNT :                ₹", dis_count)
print("| AFTER DISCOUNT :          ₹", after_discount)
print("| SGST :                    ₹",gst/2)
print("| CGST :                    ₹",gst/2)
print("| TOTAL GST :               ₹", gst)
print("|---------------------------------------|")
print("| TOTAL BILL :              ₹",total_bill)
print("|---------------------------------------|")
print("|      THANKS FOR SHOPPING WITH US      |")
print("|---------------------------------------|")

