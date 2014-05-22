import csv

reader= csv.reader(open("locations.CSV","r"))
d = {}

for boro,primary,street,cross1,cross2,side in reader:
	key = boro+street+cross1+cross2+side
	key = key.replace(" ","")
	key = key.lower()
	d[key] = primary

with open("locations_final.CSV", 'wb') as outfile:
	csv_writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

	for k,v in d.items():
		csv_writer.writerow([k,v])