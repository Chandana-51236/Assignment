y=open('car.txt','a')
brandname=list(map(str,input().split()))
color=list(map(str,input().split()))
car=dict(zip(brandname,color))
print("Brand names of the car are :",brandname)
print("Brand names of the car are :",brandname,file=y)
print("colors of the car are",color)
print("colors of the car are",color,file=y)
print("The dictionary is :",car)
print("The dictionary is :",car,file=y)
y.close()

