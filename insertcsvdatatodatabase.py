import csv
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "mydatabase"
)
mycursor = mydb.cursor()

csv_data = csv.reader(file('customers.csv'))
# import pdb;pdb.set_trace()
# next(csv_data)
count = 0
for row in csv_data:
    if count != 0:
        var1 = row[0]
        var2 = row[1]
        mycursor.execute("INSERT INTO customers VALUES (%s, %s)", (var1, var2))
    count += 1;

# close the connection to the database.
mydb.commit()
mycursor.close()
print "Done"

