
import csv

#with open('test.csv','r') as f:
 #   csv_reader =csv.reader(f)

  #  for row in csv_reader:
   #     print(row)

with open('test.csv') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        print(row)