import flask, flask.views
from word_to_num import convert_word_to_num
from fuzzywuzzy import fuzz

def identify_location(string):
	