# This is where you can start you python file for your week1 web app
# Name: Tyler Wallace

import flask
import settings
import os

# Views
from main import Main
from login import Login
from remote import Remote
from music import Music
from landing import Landing
from callback import Callback

app = flask.Flask(__name__, static_url_path='/static')
app.secret_key = settings.secret_key
main_view_func = Main.as_view('main')

# Routes
app.add_url_rule('/',
                 view_func=Landing.as_view('landing'),
                 methods=["GET"])
app.add_url_rule('/<page>/',
                 view_func=main_view_func,
                 methods=["GET"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/remote/',
                 view_func=Remote.as_view('remote'),
                 
                 methods=['GET', 'POST'])
app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=['GET'])
app.add_url_rule('/callback/',
                view_func=Callback.as_view('callback'),
                methods=['GET'])

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
