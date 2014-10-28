''' Query the Tankopedia API '''

from api import API

class Tankopedia(API):

	def list_of_vehicles(self, fields='', language='en'):
		endpoint = '/encyclopedia/tanks/'	

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language)

	def vehicle_details(self, tank_id=None, fields='', language='en'):
		endpoint = '/encyclopedia/tankinfo/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, tank_id=tank_id, fields=fields, language=language)




