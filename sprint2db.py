import mysql.connector
import os
vantage = mysql.connector.connect(user = "", password = "", host = "localhost", database = "db9")
mycursor = vantage.cursor()  
#mycursor.execute("CREATE TABLE location (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("ALTER TABLE location ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
print("Type in the name of the file you want to search")
inputname = input()
for root, dirs, files in os.walk(r'C:\Program Files'):
    for name in files:
        if name == inputname:
            filelocation = os.path.abspath(os.path.join(root, name))
            sql = "INSERT INTO location (name, address) VALUES (%s, %s)"
            val = [(name,filelocation)]
            mycursor.executemany(sql, val)
            vantage.commit()

mycursor.execute("SELECT * FROM location")

table = mycursor.fetchall()

for x in table:
  print(x)
