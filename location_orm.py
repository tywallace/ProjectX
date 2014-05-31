import psycopg2
from word_to_num import convert_word_to_num

class Location:

	connection = False
	
	@classmethod
	def connect(self):
		self.connection = psycopg2.connect("dbname='StreetSweeper' user='postgres' password='Frederick1986!!!' host='localhost'") 
		return self.connection

	@classmethod
	def disconnect(self):
		return self.connection.close()

	@classmethod
	def all(self,street="",cross1="",cross2=""):
		print
		street = convert_word_to_num(street.upper()) + "%"
		print street
		cross1 = convert_word_to_num(cross1.upper()) + "%"
		cross2 = convert_word_to_num(cross2.upper()) + "%"
		self.connect()
		cursor = self.connection.cursor()
		cursor.execute("""
			SELECT * FROM streets
			WHERE street LIKE %s
			AND cross1 LIKE %s
			AND cross2 LIKE %s
			LIMIT 10
			""", (street,cross1,cross2,))
		for row in cursor.fetchall():
			return row
		cursor.close()
		self.disconnect()


	# def __init__(self):
	# 	self.data = []