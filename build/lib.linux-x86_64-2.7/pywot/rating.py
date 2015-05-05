''' Query the WOT Ratings API '''

from pywot.api import API

class Rating(API):

	def __init__(self, app_id):
		API.__init__(self,app_id)

	def rating_types(self, lang='en', fields=''):
		endpoint = '/ratings/types/'

		if type(fields) is list:
			fields = self._format_fields(fields)		

		return self._api_call(endpoint=endpoint, fields=fields, language=lang)

	def rating_dates(self, lang='en', fields='', rating_type=''):

		endpoint = '/ratings/dates/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, type=rating_type)

	def player_ratings(self, lang='en', rating_type='', account_id=''):

		endpoint = '/ratings/accounts/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, type=rating_type, account_id=account_id)

	def neighbors(self, lang='en', rating_type='', account_id='', rank_field=''):

		endpoint = '/ratings/neighbors/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, type=rating_type, account_id=account_id, rank_field=rank_field)

	def top_players(self, lang='en', rating_type='', rank_field=''):

		endpoint = '/ratings/top/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, type=rating_type, rank_field=rank_field)