import csv

header =['Name','Address','Phone']
rows ={
    'Name' : 'shivani',
    'Address':'one',
    'Phone':'21212'
}
with open('test1.csv','w') as f:
    writer = csv.DictWriter(f,fieldnames=header)

    writer.writeheader()
    writer.writerow(rows)
    

  