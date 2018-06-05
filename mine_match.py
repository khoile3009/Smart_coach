from RiotAPI import RiotAPI
import sqlite3 as sql 
import time
import role

def main():
	start_time = time.time()
	api = RiotAPI('RGAPI-6e7a32f4-6884-4e35-8230-e11e602b2425')
	conn = sql.connect('new_table.db')
	player = sql.connect('test_table.db')
	c1 = player.cursor()
	c = conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS matches(gameID INTEGER pr, firstChamp INTEGER, secondChamp INTEGER, thirdChamp INTEGER, forthChamp INTEGER, fifthChamp INTEGER, sixthChamp INTEGER, seventhChamp INTEGER, eigthChamp INTEGER, ninthChamp INTEGER, tenthCghamp INTEGER, winner INTEGER)')
	c1.execute('SELECT accountID FROM samplePlayer')
	rows = c1.fetchall()
	count = 0
	pointer = 0
	query_counter = 1
	match_list = api.get_match_list_by_playerId(rows[0][0])
	while(pointer < match_list['endIndex']):
		if(match_list['matches'][pointer]['queue'] == 420 or match_list['matches'][pointer]['queue'		] == 440):
			game = api.get_match_by_matchId(match_list['matches'][pointer]['gameId'])
			query_counter = query_counter + 1
			command = 'REPLACE INTO matches VALUES(' + str(game['gameId'])
			for one in game['participants']:
				if(one['timeline']['lane'] == 'BOTTOM'):
					roleID = role.ID[one['timeline']['role']]
				else:
					roleID = role.ID[one['timeline']['lane']]
				command = command + ',' + str(one['championId']) + str(roleID)
			if (game['teams'][0]['win'] == 'Win'):
				winner = 0
			else:
				winner = 1
			command = command + ',' + str(winner) + ')'
			#c.execute(command)
			print(command)
			if(query_counter == 100 or time.time() - start_time > 120 ):
				while(time.time() - start_time <= 120):
					time.sleep(0.25)
				query_counter = 0
				start_time = time.time()
		pointer = pointer + 1
	player.commit()
	c1.close()
	player.close()
	conn.commit()
	c.close()
	conn.close()
if __name__ == '__main__':
	main()
