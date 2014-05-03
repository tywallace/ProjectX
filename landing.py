import flask, flask.views
import os

class Landing(flask.views.MethodView):
	def get(self):
		return flask.render_template('landing.html')