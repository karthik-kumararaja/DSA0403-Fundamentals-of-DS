import pandas as pd
import matplotlib.pyplot as mt
import statsmodel.api as sm

a={'Age':[23,23,27,27,39,41,47,49,50,52,54,56,57,58,58,60,61,34,23,56,67,78],
'Fat%':[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,32.9,41.2,35.7,9.7,34,45,23.5,20,23]}
A=pd.DataFrame(a)
print("Random 18 columns\n",A.head(18))

print("Mean AGE : ",A['Age'].mean())
print("Mean FAT% : ",A['Fat%'].mean())
print("Median AGE : ",A['Age'].median())
print("Median FAT% : ",A['Fat%'].median())
print("Standard Deviation AGE : ",A['Age'].std())
print("Standard Deviation FAT% : ",A['Fat%'].std())

Age=[23,23,27,27,39,41,47,49,50,52,54,56,57,58,58,60,61,34,23,56,67,78]
Fat=[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,32.9,41.2,35.7,9.7,34,45,23.5,20,23]
mt.boxplot(Age,Fat)
mt.xlabel("Age")
mt.ylabel("Fat")
mt.title("Age vs Fat")
mt.show()

Age=[23,23,27,27,39,41,47,49,50,52,54,56,57,58,58,60,61,34,23,56,67,78]
Fat=[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,32.9,41.2,35.7,9.7,34,45,23.5,20,23]
mt.scatter(Age,Fat)
mt.xlabel("Age")
mt.ylabel("Fat")
mt.title("Age vs Fat")
mt.show()

Age=[23,23,27,27,39,41,47,49,50,52,54,56,57,58,58,60,61,34,23,56,67,78]
Fat=[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,32.9,41.2,35.7,9.7,34,45,23.5,20,23]
sm.qqplot(Age,Fat)
mt.show()
