from RiotAPI import RiotAPI
import sqlite3 as sql 
import time

def main():
	api = RiotAPI('RGAPI-79a6b045-fe59-4d49-9e1c-15e8e12e72ab')
	conn = sql.connect('new_table.db')
	player = sql.connect('test_table.db')
	c1 = player.cursor()
	c = conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS matches(gameID INTEGER, firstChamp INTEGER, secondChamp INTEGER, thirdChamp INTEGER, forthChamp INTEGER, fifthChamp INTEGER, sixthChamp INTEGER, seventhChamp INTEGER, eigthChamp INTEGER, ninthChamp INTEGER, tenthCghamp INTEGER, winner INTEGER)')
	c1.execute('SELECT accountID FROM samplePlayer')
	rows = c1.fetchall()
	for row in rows:
		
	player.commit()
	c1.close()
	player.close()
	conn.commit()
	c.close()
	conn.close()
if __name__ == '__main__':
	main()
