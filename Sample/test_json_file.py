import json

def main():
	with open ('test_data.json') as f:
		data = json.load(f)
	i = 0
	while(data['participantIdentities'][i]['player']['summonerName'] != 'albiner5'):
		i = i + 1
	participantID = data['participantIdentities'][i]['participantId']
	gamecs

if __name__ == "__main__":
	main()	