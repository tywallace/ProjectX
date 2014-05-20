import csv

reader= csv.reader(open("signs_test.CSV","r"))
s = {}

for boro,primary,sequence,distance,arrow,description in reader:
	print boro, primary, sequence, distance, arrow, description
	if primary in s:
		s[primary].append(description)
	else:
		s[primary] = [description]

print s