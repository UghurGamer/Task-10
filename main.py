import sqlite3

connection = sqlite3.connect("weather.DB.sl3")
cur = connection.cursor()

# cur.execute("CREATE TABLE first_table(date_time TEXT, temperature REAL);")
# cur.execute("INSERT INTO first_table (date_time, temperature) VALUES ('12.12.2025', '12°C')")
cur.execute("SELECT * FROM first_table")
connection.commit()
res = cur.fetchall()
for i in res:
    print(i)
connection.close()
