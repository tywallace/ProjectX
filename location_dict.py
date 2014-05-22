import csv

reader= csv.reader(open("locations.CSV","r"))
d = {}

for boro,primary,street,cross1,cross2,side in reader:
	key = boro+street+cross1+cross2+side
	key = key.replace(" ","")
	key = key.lower()
	d[key] = primary
