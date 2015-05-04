''' Query players and their stats '''

from pywot.api import API
import json

class Player(API):

	def __init__(self, app_id):
		API.__init__(self,app_id)

	def search_players(self, lang='en', search='', fields=''):
		''' Player API methods require an account_id.  
			This method allows you to search for players if you don't know
			their exact username.  Once that is known, call get_account_id, sending it the player's nickname.'''
		
		endpoint = '/account/list/'

		if type(fields) is list:
			fields = self._format_fields(fields)		

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, search=search)

	def get_account_id(self, nickname=''):
		''' This method returns a user's account_id, which is needed for other Player API calls.'''
		return json.loads(self.search_players(search=nickname,fields='account_id'))['data'][0]['account_id']

	def personal_data(self, account_id='', lang='en', fields='', nickname=''):
		''' Returns player statistics '''

		endpoint = '/account/info/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		if nickname:			
			account_id = self.get_account_id(nickname=nickname)

		return self._api_call(endpoint=endpoint, 
							  fields=fields, 
							  language=lang, 
							  account_id=account_id)

	def player_vehicles(self, account_id='', lang='en', fields='', nickname=''):
		''' Returns details of player's tanks '''

		endpoint = '/account/tanks/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		if nickname:			
			account_id = self.get_account_id(nickname=nickname)

		return self._api_call(endpoint=endpoint, 
							  fields=fields, 
							  language=lang, 
							  account_id=account_id)

	def player_achievements(self, account_id='', lang='en', fields='', nickname=''):
		''' Returns player achievement details '''

		endpoint = '/account/achievements/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		if nickname:			
			account_id = self.get_account_id(nickname=nickname)

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, account_id=account_id)