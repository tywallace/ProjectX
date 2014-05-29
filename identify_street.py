import csv
from word_to_num import convert_word_to_num
import re

reader= csv.reader(open("locations.CSV","r"))
street_list = []

for boro,primary,street,cross1,cross2,side in reader:
	street = re.sub( '\s+', ' ', street).strip()
	street_list.append(convert_word_to_num(street.lower()))

street_list = list(set(street_list))
street_list.sort()