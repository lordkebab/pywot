''' Query the Tankopedia API '''

from api import API

class Tankopedia(API):

	def list_of_vehicles(self, fields='', language='en'):
		endpoint = '/encyclopedia/tanks/'	

		if type(fields) is list:
			fields = self._format_fields(fields)

		print self._api_call(endpoint=endpoint, fields=fields, language=language)


