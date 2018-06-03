from RiotAPI import RiotAPI
import sqlite3 as sql 
import time

def main():
	keyPlayerID = 227488010
	keyPlayerName = 'Nixim'
	api = RiotAPI('RGAPI-79a6b045-fe59-4d49-9e1c-15e8e12e72ab')
	conn = sql.connect('test_table.db')
	c = conn.cursor()
	c.execute('CREATE TABLE IF NOT EXISTS samplePlayer (name TEXT PRIMARY KEY, accountID INTEGER)')	
	command = 'REPLACE INTO samplePlayer(name, accountID) VALUES (\'' + keyPlayerName + '\',' + str(keyPlayerID) + ')'
	c.execute(command)
	r = api.get_match_list_by_playerId (str(keyPlayerID))
	count = 1
	query_counter = 1
	pointer = 0
	start_time = time.time()
	print(r['totalGames'])
	while(pointer < r['endIndex'] and count < 1000):
		matchID = r['matches'][pointer]['gameId']
		game = api.get_match_by_matchId(matchID)
		query_counter = query_counter + 1
		for one in game['participantIdentities']:
			if(one['player']['accountId'] != keyPlayerID):
				command = 'REPLACE INTO samplePlayer(name, accountID) VALUES (\'' + one['player']['summonerName'] + '\',' + str(one["player"]["accountId"]) + ')'
				c.execute(command)
				#print(one['player']['summonerName'])
				count = count + 1
		pointer = pointer + 1
		print(query_counter)
		print(time.time() - start_time)
		if(query_counter == 100 or time.time() - start_time > 120 ):
			while(time.time() - start_time <= 120):
				time.sleep(0.25)
			query_counter = 0
			start_time = time.time()
	conn.commit()
	c.close()
	conn.close()


if __name__ == "__main__":
	main()	