import matplotlib.pyplot as mt
a=[1,2,3,4,5,6,7,8,9,10,11,12]
b=[8,12,34,57,45,35,67,78,77,65,76,90]
mt.plot(a,b)
mt.xlabel("Months")
mt.ylabel("Products Sold")
mt.title("Months vs Products")
mt.show()
mt.bar(a,b)
mt.xlabel("Months")
mt.ylabel("Products Sold")
mt.title("Months vs Products")
mt.show()
