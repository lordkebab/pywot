''' A library providing a python interface to Wargaming.net's World of Tanks API '''

import requests

class API(object):

	BASE_URL = 'https://api.worldoftanks.com/wot'	# no trailing slash

	def __init__(self, app_id):
		self.app_id = app_id

	def _api_call(self, **kwargs):
		''' Initiates an API call '''
		r = requests.get('https://api.worldoftanks.com/wot/encyclopedia/tanks', params=kwargs)
		return r.json()
