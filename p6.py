#Guys do you think Mouoruso is getting banged by Reims
import sqlite3

#Connection lets us connect python to a SQL database
connection = sqlite3.connect("./database.db") #relatively, in my current location is the period. "From my location"
cursor = connection.cursor()
#Lets us interact with sql

query = """
SELECT AVG(price) FROM Products;
"""

result = cursor.execute(query).fetchall()
print(result)
#End of code
connection.commit() #Commits changes
connection.close() #disconnects the connection