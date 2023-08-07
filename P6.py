Items = ["Wheat","Rice","Biscuits","Chocolates"]
Price = [45,70,30,55]
Amount=0
for i in range(len(Items)):
    print(i+1,Items[i])
print("************************************")
a=1
while a==1:
    o=int(input("Your Order : "))
    q=int(input("Quantities : "))
    if o==1:
        Amount=Amount+Price[0]*q
    elif o==2:
        Amount=Amount+Price[1]*q
    elif o==3:
        Amount=Amount+Price[2]*q
    elif o==4:
        Amount=Amount+Price[3]*q
    a=int(input("To continue shopping press 1 : "))
else:
    Discount=Amount/10
    dis=Amount-Discount
    print("************************************")
    print("AMOUNT : ",Amount)
    print("DISCOUNT PRICE : ",dis)
    c=dis*0.18
    print("TAXES : ",c)
    print("PAYABLE AMOUNT : ",dis+c)
    print("-------THANK YOU ! VISIT AGAIN-------")
    
