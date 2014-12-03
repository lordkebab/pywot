.. _main_page:

PyWOT: Python World of Tanks API Wrapper
========================================

.. begin_description

A library providing a python interface to Wargaming.net's World of Tanks API.  In order to use this API, you must register as a developer and add an application for free at `Wargaming.net <https://na.wargaming.net/developers`_.  You will then be given an application ID that you will use when making API calls.  

As of this release the API only works with the North American servers.

All results are returned as JSON documents.

.. end_description

.. begin_installation:

Installation
------------

PyWOT works with Python 2.6 and 2.7 as of this release.  It can be installed using pip:

.. code-block:: bash

	$ pip install pywot

.. end_installation

.. begin_usage

Usage
-----

Once you obtain your Application ID, instantiate a new instance of pywot.  The following will get a list of all the tanks in the game:

.. code-block:: pycon

	>>> from pywot.api import API
	>>> from pywot.tankopedia import Tankopedia
	>>> app = API('your-app-id')
	>>> t = Tankopedia(app.app_id)
	>>> print t.list_of_vehicles()

You can get the details of a particular tank with the vehicle_details method.  Here is how you would get the details of the KV-1S:

.. code-block:: pycon
	
	>>> print t.vehicle_details(tank_id=18689)

Or, just get a few fields:

.. code-block:: pycon

	>>> print t.vehicle_details(
		tank_id=18689, 
		fields=['tank_id', 'nation', 'speed_limit', 'engines.module_id'])

The field names can be obtained from the `API Reference <https://na.wargaming.net/developers/api_reference/wot/account/list/>`_.  They can be passed in as a comma-delimited string or a python list of string values, as shown above.  You can also pass in multipe tank_id's the same way:

.. code-block:: pycon

	>>> print t.vehicle_details(
		tank_id=['18689','33'], 
		fields=['tank_id', 'nation', 'speed_limit', 'engines.module_id'])

PyWOT also supports specifying different languages for the response:

.. code-block:: pycon

	>>> print t.vehicle_details(
		language='ko', 
		tank_id=['18689','33'], 
		fields=['tank_id', 'nation', 'speed_limit', 'engines.module_id'])

In order to see the publicly available player statistics, first use the search_players method, sending it an un-wildcarded search string of a user's nickname. Once you have the player's exact nickname, use the get_account_id method to retrieve that player's account_id which will be used in subsequent methods.  You can also chain those method calls together as in the example below.

To get all the achievements of a player with the nickname "lulz_man" do the following:

.. code-block:: pycon

	>>> from pywot.api import API
	>>> from pywot.player import Player
	>>> app = API('your-app-id')
	>>> p = Player(app.app_id)
	>>> print p.player_achievements(account_id=p.get_account_id(nickname='lulz_man'))

.. end_usage

.. begin_license

License
-------

All of the code contained here is licensed by
`the Apache 2.0 License <https://github.com/mattselph/pywot/blob/master/LICENSE>`_.

.. end_license