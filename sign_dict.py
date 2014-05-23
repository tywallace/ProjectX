import csv
from street_cleaning import if_cleaning

signs_list = ["signs1.CSV","signs2.CSV","signs3.CSV","signs4.CSV","signs5.CSV","signs6.CSV","signs7.CSV","signs8.CSV"]

s = {}

for x in signs_list:
	reader= csv.reader(open(x,"r"))

	for row in reader:
		description = if_cleaning(row[5])
		if description != None:
			if row[1] not in s:
				s[row[1]] = description

with open("signs_final.CSV", 'wb') as outfile:
	csv_writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	for k,v in s.items():
		csv_writer.writerow([k,v[0],v[1],v[2],v[3]])
