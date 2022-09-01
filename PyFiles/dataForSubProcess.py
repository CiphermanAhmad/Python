import csv
fileName =  r"E:\\Python\\csvFile.csv"
reader = csv.reader(open(fileName,'r'))
#skip the header of csv file , header has been defined
#header = reader.__next__()
#read
for rec in reader:
    print(rec)      