import csv

try:
    #field names

    fields=['id','name','age','salary']

    #data rows of csv file

    rows=[{'id':'1','name':'santa','age':'24','salary':'40000'},{'id':'2','name':'jeteena','age':'24','salary':'10000'},{'id':'3','name':'archana','age':'20','salary':'10000'},{'id':'4','name':'anjana','age':'20','salary':'25000'}]
    
    #writing into a csv file

    f=open('details1.csv','w',newline='')
    w=csv.DictWriter(f,fieldnames=fields) #creating a csv writer object
    w.writeheader() #writing fields
    w.writerows(rows)
    print("successfully inserted")

except Exception as ae:
    print(ae)

finally:
    f.close()
          
