number=input("enter the numbers:")
numberlist=number.split(',')
even=[i for i in numberlist if int(i)%2==0]
print("list of even numbers are",even)
