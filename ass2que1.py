import pandas as pd
x=[int(input("Enter values of x")) for i in range(4)]
y=[int(input("Enter values of y")) for i in range(4)]
ser_x=pd.Series(x)
ser_y=pd.Series(y)
print("Pandas series of x are:",ser_x)
print("Pandas series of y are:",ser_y)
print("Addition of numbers in two pandas series is", ser_x+ser_y)
print("subrtraction of numbers in two pandas series is ",ser_x-ser_y)
print("Multiplication of numbers in two pandas series is ",ser_x*ser_y)
print("Division of numbers in two pandas series is ",ser_x/ser_y)
print("Reminder of numbers in two pandas series is ",ser_x%ser_y)

