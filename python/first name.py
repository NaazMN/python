name=input("enter first names:\n")
namelist=name.split(',')
count=0
for i in namelist:
    if i[0]=='a' or i[0]=='A':
        count=count+1
print("the number of names that stands with a is ",count)
