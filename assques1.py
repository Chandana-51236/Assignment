n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number"))
n4=int(input("Enter fourth number"))
n5=int(input("Enter fifth number"))
if n1<0 or n2<0 or n3<0 or n4<0 or n5<0:
    print("Please enter positive number")
else:
    sum=n1+n2+n3+n4+n5
    x=open("sum.txt","a")
    print("sum","=",sum)
    print("sum","=",sum,file=x)
    x.close()