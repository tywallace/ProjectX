import csv
from street_cleaning import if_cleaning

reader= csv.reader(open("signs.CSV","r"))
s = {}

for row in reader:
	description = if_cleaning(row[5])
	if description != None:
		if row[1] not in s:
			s[row[1]] = description

# u = {}
# for key, value in s.iteritems():
# 	u[key] = list(set(value))
