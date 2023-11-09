number=input("enter the numbers:")
numberlist=number.split()
small=int(numberlist[0])
large=int(numberlist[0])
for i in numberlist:
    if(int(i)>large):
    large=int(i)
    elif(int(i)<small):
        small=int(i)
        print("the list is\n",numberlist)
        print("maximum number is",large,'\nminimum number is',small)
