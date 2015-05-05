''' Query the Tankopedia API '''

from pywot.api import API

class Tankopedia(API):

	def __init__(self, app_id):
		API.__init__(self,app_id)

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

	def engines(self, fields='', language='en', module_id='', nation=''):
		endpoint = '/encyclopedia/tankengines/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language)

	def turrets(self, fields='', language='en', module_id='', nation=''):
		endpoint = '/encyclopedia/tankturrets/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language)

	def radios(self, fields='', language='en', module_id='', nation=''):
		endpoint = '/encyclopedia/tankradios/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language)
	
	def suspensions(self, fields='', language='en', module_id='', nation=''):
		endpoint = '/encyclopedia/tankchassis/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language)

	def guns(self, fields='', language='en', module_id='', nation='usa', turret_id='', tank_id=''):		
		endpoint = '/encyclopedia/tankguns/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language,
			module_id=module_id, nation=nation, turret_id=turret_id, tank_id=tank_id)

	def info(self, fields='', language='en'):
		endpoint = '/encyclopedia/info/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language)

	def maps(self, fields='', language='en'):
		endpoint = '/encyclopedia/arenas/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language)



