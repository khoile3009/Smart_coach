import sqlite3
import champ_id as champ

conn = sqlite3.connect('test_table.db')
c = conn.cursor()
data = champ.champID['data']
for key,value in data:
	name = value['name']
	championId = value['id']
	command = 'INSERT INTO  ChampionID VALUES(\'' + name + '\',' + str(championID) + ')'
	c.execute(command)
conn.commit()
c.close()
conn.close()