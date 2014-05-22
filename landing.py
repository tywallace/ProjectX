import flask, flask.views
import os

from location_dict import d
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
		side_list = ["N","S","E","W"]

		location = identify_location(boro,street,cross1,cross2,side_list)
		
		for x in ["N","S","E","W"]:
			if x in location:
				a = location[x]
				if a in s:
					b = s[a]
					flask.flash(b)
				else:
					flask.flash(a + " not a location with street cleaning")
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