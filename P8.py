import pandas as pd
data = {"PN":['Lays','Kurkure','Cheetos','Maxx','Doritos','Kurkure','Maxx','Pringles'],"OD":[10,5,3,10,10,2,3,20]}
a=pd.DataFrame(data)
sort=a.sort_values(by="OD",ascending=False)
print(sort)
print("\n***Top 5 Products***")
print(sort.head(5))
