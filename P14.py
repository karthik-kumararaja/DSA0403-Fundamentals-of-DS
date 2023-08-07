import pandas as pd
a={'Name':["AA KK","BB","CC"],"Age":['18','19','17'],"Schl":["PA","SNP","SGHS"]}
b=pd.DataFrame(a)
b["Words_Name"]=b['Name'].apply(lambda n:(len(n.split())))
b["Words_Age"]=b['Age'].apply(lambda n:(len(n.split())))
b["Words_Schl"]=b['Schl'].apply(lambda n:(len(n.split())))
print(b.head())
