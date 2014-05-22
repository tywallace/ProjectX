import csv
from street_cleaning import if_cleaning

reader= csv.reader(open("signs.CSV","r"))
s = {}

for row in reader:
	description = if_cleaning(row[5])
	if description != None:
		if row[1] not in s:
			s[row[1]] = description

with open("signs_final.CSV", 'wb') as outfile:
	csv_writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	for k,v in s.items():
		csv_writer.writerow([k,v])