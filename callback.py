import flask, flask.views
import os
import utils

class Callback(flask.views.MethodView):
	def get(self):
		return flask.render_template('contact.html')