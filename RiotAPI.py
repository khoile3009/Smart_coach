import Riot_Const as Consts
import requests
class RiotAPI(object):
	def __init__(self,api_key,region = Consts.REGIONS['North_America']):
		self.api_key = api_key
		self.region = region

	def _request(self, api_url, params = {}):
		args = {'api_key' : self.api_key}
		for key, value in params.items():
			if key not in args:
				args[key] = value
		response = requests.get(
			Consts.URL['base'].format(
				proxy = self.region,
				request_type = api_url
				),
			params = args
			)	
		print(response.url)
		return response.json()

	def get_summoner_by_name (self, names):
		api_url = Consts.URL['summoner_by_name'].format(
			version = Consts.api_version,
			player_name = names
			)
		return self._request(api_url)

	def get_match_list_by_playerId (self, account_id, params = {}):
		api_url = Consts.URL['matches_by_account'].format(
			version = Consts.api_version,
			player_id = account_id
			)
		return self._request(api_url,params)

	def get_match_by_matchId (self, match_id, params = {}):
		api_url = Consts.URL['match_by_matchId'].format(
			version = Consts.api_version,
			match = match_id
			)
		return self._request(api_url,params)

	def get_league_by_playerId (self, player_id, params = {}):
		api_url = Consts.URL['league_by_Id'].format(
			version = Consts.api.version,
			sumID = player_id
			)
		return self._request(apo_url,params)
	
