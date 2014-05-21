import csv
from street_cleaning import if_cleaning

reader= csv.reader(open("signs.CSV","r"))
s = {}

for boro,primary,sequence,distance,arrow,description in reader:
	description = if_cleaning(description)
	if description != None:
		if primary not in s:
			s[primary] = description


# u = {}
# for key, value in s.iteritems():
# 	u[key] = list(set(value))
