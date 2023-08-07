import pandas as pd
a = {"Property_ID":[101,102,103,104],"Location":["Delhi","Mumbai","Bangalore","Chennai"],"No_of_Bedrooms":[3,2,4,3],"Area(Sq.ft)":[1200,800,1800,1350],"Listing_Price":[6000000,5500000,9000000,8000000]}
b = pd.DataFrame(a)
print(b)
print("Mean : ",b["Listing_Price"].mean())
print(b[["No_of_Bedrooms"]]>4)
print("Maximum Area(Sq.ft) : ",b["Area(Sq.ft)"].max())


