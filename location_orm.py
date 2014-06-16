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
		street = convert_word_to_num(street.upper()) + "%"
		cross1 = convert_word_to_num(cross1.upper()) + "%"
		cross2 = convert_word_to_num(cross2.upper()) + "%"
		self.connect()
		cursor = self.connection.cursor()
		cursor.execute("""
			SELECT DISTINCT * FROM streets
			WHERE street LIKE %s
			AND cross1 LIKE %s
			AND cross2 LIKE %s
			LIMIT 10
			""", (street,cross1,cross2,))
		results = []
		for row in cursor.fetchall():
			results.append(row[2])
		return results
		cursor.close()
		self.disconnect()

	@classmethod
	def main_streets(self,street=""):
		street = convert_word_to_num(street.upper()) + "%"
		self.connect()
		cursor = self.connection.cursor()
		cursor.execute("""
			SELECT DISTINCT street 
			FROM streets
			WHERE street LIKE %s
			ORDER BY street
			LIMIT 10
			""", (street,))
		results = []
		for row in cursor.fetchall():
			results.append(row[0])
		return results
		cursor.close()
		self.disconnect()