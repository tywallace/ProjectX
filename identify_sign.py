import flask, flask.views
from word_to_num import convert_word_to_num
import csv

reader= csv.reader(open("locations_final.csv","r"))
d = {}
for row in reader:
	d[row[0]] = row[1]

def identify_sign(boro,street,cross1,cross2,side_list):
	location = {}
	for x in side_list:
			boro = boro.lower()
			street = convert_word_to_num(street.lower())
			cross1 = convert_word_to_num(cross1.lower())
			cross2 = convert_word_to_num(cross2.lower())
			key1 = boro + street + cross1 + cross2 + x
			key1 = key1.replace(" ","")
			key2 = boro + street + cross2 + cross1 + x
			key2 = key2.replace(" ","")
			
			if key1 in d:
				location[x] = d[key1]
			elif key2 in d:
				location[x] = d[key2]
	return location