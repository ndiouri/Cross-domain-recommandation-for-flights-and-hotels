import csv
with open('flight_order_BJS_new.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print ', '.join(row)