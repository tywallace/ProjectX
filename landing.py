import flask, flask.views
import os

from identify_sign import identify_sign
from identify_regulation import s
from identify_street import street_list

class Landing(flask.views.MethodView):
	def get(self):
		return flask.render_template('landing.html', nycstreets = street_list)

	def post(self):
		boro = flask.request.form['boro']
		if boro == "Bronx":
			boro = "b"
		elif boro == "Brooklyn":
			boro = "k"
		elif boro == "Manhattan":
			boro = "m"
		else:
			boro = "q"

		street = flask.request.form['street']
		cross1 = flask.request.form['cross1']
		cross2 = flask.request.form['cross2']
		side_list = ["n","s","e","w"]
		location = identify_sign(boro,street,cross1,cross2,side_list)
		side_dict = {"n":"north","s":"south","e":"east","w":"west"}
		
		side_sweep_list = []

		if location != {}:
			for x in side_list:
				if x in location:
					sign_code = location[x]
					if sign_code in s:
						parking_reg = s[sign_code]
						flask.flash("Street cleaning will start on the " + side_dict[x] + " side at " + parking_reg[0] + " and end at " + parking_reg[1] + " " + parking_reg[2] + " on " + parking_reg[3])
						side_sweep_list.append(x)

			if "n" in side_sweep_list and "s" not in side_sweep_list:
				flask.flash("There is no street cleaning on the south side of the street.")

			if "s" in side_sweep_list and "n" not in side_sweep_list:
				flask.flash("There is no street cleaning on the north side of the street.")

			if "w" in side_sweep_list and "e" not in side_sweep_list:
				flask.flash("There is no street cleaning on the east side of the street.")

			if "e" in side_sweep_list and "w" not in side_sweep_list:	
				flask.flash("There is no street cleaning on the west side of the street.")

			if side_sweep_list == []:
				flask.flash("There is no street cleaning on this street")
		else:
			flask.flash("Street not found.")
		return flask.redirect(flask.url_for('landing'))