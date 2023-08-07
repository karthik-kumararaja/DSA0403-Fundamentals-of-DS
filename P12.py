import matplotlib.pyplot as mt
months=[1,2,3,4,5,6,7,8,9,10,11,12]
temp=[26,27,29,32,34,29,27,25,26,20,24,23]
rainfall=[8,5,3,1,2,4,3,3,5,6,7,8]
mt.plot(months,temp)
mt.xlabel("Months")
mt.ylabel("Temperature")
mt.title("Months vs Temperature")
mt.show()

mt.scatter(months,rainfall)
mt.xlabel("Months")
mt.ylabel("Rainfall")
mt.title("Months vs Rainfall")
mt.show()
