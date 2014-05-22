import flask, flask.views
import os

from identify_location import identify_location
from sign_dict import s

class Landing(flask.views.MethodView):
	def get(self):
		return flask.render_template('landing.html')

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
		location = identify_location(boro,street,cross1,cross2,side_list)
		side_dict = {"n":"north","s":"south","e":"east","w":"west"}
		for x in side_list:
			if x in location:
				a = location[x]
				if a in s:
					b = s[a]
					flask.flash("Street cleaning will start on the " + side_dict[x] + " side at " + b[0] + " and end at " + b[1] + " " + b[2] + " on " + b[3])
			else:
				flask.flash("There is no street cleaning on the " + side_dict[x] + " side of the street you specified")
		# if "N" in location:
		# 	north = location["N"]
		# 	flask.flash(north)
		# 	nrules = s[north]
		# 	flask.flash(nrules)
		# if "S" in location:
		# 	south = location["S"]
		# 	flask.flash(south)
		# 	srules = s[south]
		# 	flask.flash(nrules)
		# if "E" in location:
		# 	east = location["E"]
		# 	erules = s[east]
		# 	flask.flash(nrules)
		# if "W" in location:
		# 	west = location["W"]
		# 	wrules = s[west]
		# 	flask.flash(nrules)
		return flask.redirect(flask.url_for('landing'))