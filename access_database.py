import psycopg2

dbconn = psycopg2.connect("dbname='StreetSweeper' user='postgres' password='Frederick1986!!!' host='localhost'")
cursor = dbconn.cursor()
cursor.execute("""
SELECT ID
FROM "SIGNS"
LIMIT 100
""")

for row in cursor.fetchall():
	print "Sign: " + row[0]
cursor.close()
dbconn.close()
