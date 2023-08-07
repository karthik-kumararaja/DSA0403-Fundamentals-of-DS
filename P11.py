import matplotlib.pyplot as mt
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
b=[2,3,0,5,7,8,9,0,0,10,12,13,12,14,12,13,15,17,19,24,17,15,23,23,24,22,15,34,32,21]
mt.plot(a,b)
mt.xlabel("Days")
mt.ylabel("Sales")
mt.title("Days vs Sales")
mt.show()

mt.scatter(a,b)
mt.xlabel("Days")
mt.ylabel("Sales")
mt.title("Days vs Sales")
mt.show()

mt.bar(a,b)
mt.xlabel("Days")
mt.ylabel("Sales")
mt.title("Days vs Sales")
mt.show()
