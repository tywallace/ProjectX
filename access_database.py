import psycopg2

dbconn = psycopg2.connect("dbname='StreetSweeper' user='postgres' password='Frederick1986!!!' host='localhost'")
cursor = dbconn.cursor()
cursor.execute("""
SELECT *
FROM signs
LIMIT 100
""")

for row in cursor.fetchall():
	print row
cursor.close()
dbconn.close()
