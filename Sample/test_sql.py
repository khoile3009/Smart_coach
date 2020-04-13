import sqlite3

conn = sqlite3.connect('new_table.db')
c = conn.cursor()
conn.commit()
c.close()
conn.close()
