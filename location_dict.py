import csv
from word_to_num import convert_word_to_num

reader= csv.reader(open("locations.CSV","r"))
d = {}
s = {}

for boro,primary,street,cross1,cross2,side in reader:
	street = convert_word_to_num(street)
	street = " ".join(street.split())
	cross1 = convert_word_to_num(cross1)
	cross1 = " ".join(cross1.split())
	cross2 = convert_word_to_num(cross2)
	cross2 = " ".join(cross2.split())
	s[primary] = [boro,street,cross1,cross2,side]

with open("street_final.CSV", 'wb') as outfile:
	csv_writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

	for k,v in s.items():
		csv_writer.writerow([k,v[0],v[1],v[2],v[3],v[4]])

print s["S-206325"]