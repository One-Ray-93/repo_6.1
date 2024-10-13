import csv

with open('TMP/File_2.csv', newline='') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)