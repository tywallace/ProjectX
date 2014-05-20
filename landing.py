import flask, flask.views
import os

from location_dict import d
from identify_location import identify_location

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

		identify_location(boro,street,cross1,cross2,side_list)
		
		return flask.redirect(flask.url_for('landing'))