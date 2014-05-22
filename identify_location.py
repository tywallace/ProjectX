import flask, flask.views
from location_dict import d

def identify_location(boro,street,cross1,cross2,side_list):
	location = {}
	for x in side_list:
			key1 = boro+street+cross1+cross2+x
			key1 = key1.replace(" ","")
			key1 = key1.lower()
			key2 = boro+street+cross2+cross1+x
			key2 = key2.replace(" ","")
			key2 = key2.lower()
			if key1 in d:
				location[x] = d[key1]
			elif key2 in d:
				location[x] = d[key2]
	if location == {}:
		flask.flash("Street not found")
	else:
		flask.flash(location)
		return location