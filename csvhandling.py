import csv
header =['Name','Address','Phone']
rows =[
    ['Shivani','bkt','122121'],
    ['alu','ktm','877897897']
]

with open ('test.csv','w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)

    for x in rows:
        csv_writer.writerow(x)