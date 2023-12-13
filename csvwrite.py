import csv


try:
    #field names

    fields=['id','name','age','salary']

    #data rows of csv file

    rows=[['1','naaz','21','25000'],['2','livya','22','10000']]

    #writing into csv file

    f=open('details.csv','w',newline='')
    w=csv.writer(f) #creating a csv writer object
    w.writerow(fields) #writing fields
    w.writerows(rows)

except exception as ae:
        print(ae)


finally:
        f.close()
        
