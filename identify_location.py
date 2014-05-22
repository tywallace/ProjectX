import flask, flask.views
from location_dict import d
from word_to_num import convert_word_to_num

def identify_location(boro,street,cross1,cross2,side_list):
	location = {}
	for x in side_list:
			key1 = boro.lower()+convert_word_to_num(street.lower())+convert_word_to_num(cross1.lower())+convert_word_to_num(cross2.lower())+x
			key1 = key1.replace(" ","")
			key2 = boro.lower()+convert_word_to_num(street.lower())+convert_word_to_num(cross2.lower())+convert_word_to_num(cross1.lower())+x
			key2 = key2.replace(" ","")
			
			if key1 in d:
				location[x] = d[key1]
			elif key2 in d:
				location[x] = d[key2]
	if location == {}:
		flask.flash("Street not found")
	else:
		return location