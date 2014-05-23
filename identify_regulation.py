import flask, flask.views
import csv

s = {}

reader= csv.reader(open("signs_final.csv","r"))

for row in reader:
	s[row[0]] = [row[1],row[2],row[3],row[4]]

print s["S-245794"]