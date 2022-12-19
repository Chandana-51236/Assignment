import pandas as pd
x=[int(input("Enter the number:")) for i in range(5)]
ser_x=pd.Series(x)
dic={"x":x,"Squares":ser_x*ser_x}
df=pd.DataFrame(dic)
print(df)