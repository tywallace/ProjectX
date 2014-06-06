import flask, flask.views
import os

from sign_orm import Sign
from location_orm import Location

class Landing(flask.views.MethodView):
	def get(self):
		return flask.render_template('landing.html')