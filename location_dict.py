import csv
from word_to_num import convert_word_to_num

reader= csv.reader(open("locations.CSV","r"))
d = {}

for boro,primary,street,cross1,cross2,side in reader:
	location = boro.lower()+convert_word_to_num(street.lower())+convert_word_to_num(cross1.lower())+convert_word_to_num(cross2.lower())+side.lower()
	location = location.replace(" ","")
	d[location] = primary

with open("locations_final.CSV", 'wb') as outfile:
	csv_writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

	for k,v in d.items():
		csv_writer.writerow([k,v])