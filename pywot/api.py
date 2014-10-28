''' A library providing a python interface to Wargaming.net's World of Tanks API '''

import requests
import json

class API(object):

	BASE_URL = 'https://api.worldoftanks.com/wot'	# no trailing slash

	def __init__(self, app_id):
		self.app_id = app_id

	def _api_call(self, url, **kwargs):
		''' Initiates an API call '''
		
		payload = kwargs
		
		# add the application id to our payload
		payload['application_id'] = self.app_id
		r = requests.get(url, params=payload)
		
		# return pretty-printed json
		return json.dumps(r.json(), sort_keys=True, indent=4)
				
