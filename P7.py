import pandas as pd
data={'C_ID':[1,2,3,1,3],'ORDER_DATE':["01/01/2023","28/04/2023","04/08/2023","20/09/2023","02/11/2023"],'P_NAME':["Maida","Biscuits","Chocolates","Chocolates","Biscuits"],'QTY':[3,1,5,10,5]}
df=pd.DataFrame(data)
print(df)
a=df[['QTY']]
print(a)
