import csv

reader = csv.reader(open('F:\code\python\python_slb\data\stocks.csv'))
headers = next(reader)
for row in reader:
	print(row[0])
	#symbol=