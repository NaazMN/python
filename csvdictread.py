import csv


try:

       f=open('details1.csv','r')
       read=csv.DictReader(f)
       for lines in read:
           print(lines['id'],'\t',lines['name'],'\t',lines['age'],'\t',lines['salary'])

except Exception as ae:
        print(ae)

finally:
    f.close()

    
