import psycopg2

class Sign:

	connection = False
	
	@classmethod
	def connect(self):
		self.connection = psycopg2.connect("dbname='StreetSweeper' user='postgres' password='Frederick1986!!!' host='localhost'") 
		return self.connection

	@classmethod
	def disconnect(self):
		return self.connection.close()

	@classmethod
	def get(self,sign_id=""):
		sign_array = []
		self.connect()
		cursor = self.connection.cursor()
		cursor.execute("""
			SELECT * FROM signs
			WHERE id LIKE %s
			LIMIT 10
			""", (sign_id,))
		for row in cursor.fetchall():
			return row
		cursor.close()
		self.disconnect()

		

	# def __init__(self):
	# 	self.data = []

