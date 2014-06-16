import flask, flask.views
import json
import os

from sign_orm import Sign
from location_orm import Location

class Streets(flask.views.MethodView):
	def get(self,query=""):
		# boro = flask.request.form['boro']
		# if boro == "Bronx":
		# 	boro = "b"
		# elif boro == "Brooklyn":
		# 	boro = "k"
		# elif boro == "Manhattan":
		# 	boro = "m"
		# else:
		# 	boro = "q"
		# cross1 = flask.request.form['cross1']
		# cross2 = flask.request.form['cross2']
		# side_list = ["n","s","e","w"]
		# flask.flash("street: " + street)
		location = Location.main_streets(query)
		return json.dumps([dict(value=x) for x in location])
		# return flask.jsonify(streets = location)

		# side_dict = {"n":"north","s":"south","e":"east","w":"west"}
		
		# side_sweep_list = []

		# if location != {}:
		# 	for x in side_list:
		# 		if x in location:
		# 			sign_code = location[x]
		# 			if sign_code in s:
		# 				flask.flash(sign_code)
		# 				parking_reg = Sign.get(sign_code)
		# 				flask.flash(parking_reg)
		# 				flask.flash("Street cleaning will start on the " + side_dict[x] + " side at " + parking_reg[1] + " and end at " + parking_reg[2] + " " + parking_reg[3] + " on " + parking_reg[4])
		# 				side_sweep_list.append(x)	

		# 	if "n" in side_sweep_list and "s" not in side_sweep_list:
		# 		flask.flash("There is no street cleaning on the south side of the street.")

		# 	if "s" in side_sweep_list and "n" not in side_sweep_list:
		# 		flask.flash("There is no street cleaning on the north side of the street.")

		# 	if "w" in side_sweep_list and "e" not in side_sweep_list:
		# 		flask.flash("There is no street cleaning on the east side of the street.")

		# 	if "e" in side_sweep_list and "w" not in side_sweep_list:	
		# 		flask.flash("There is no street cleaning on the west side of the street.")

		# 	if side_sweep_list == []:
		# 		flask.flash("There is no street cleaning on this street")
		# else:
		# 	flask.flash("Street not found.")

		