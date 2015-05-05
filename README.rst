.. _main_page:

PyWOT: Python World of Tanks API Wrapper
========================================

.. begin_description

.. image:: https://travis-ci.org/mattselph/pywot.svg?branch=master
		   :target: https://travis-ci.org/mattselph/pywot

A library providing a python interface to Wargaming.net's World of Tanks API.  In order to use this API, you must register as a developer and add an application for free at `Wargaming.net <https://na.wargaming.net/developers>`_.  You will then be given an application ID that you will use when making API calls.  

As of this release the API only works with the North American servers.

All results are returned as JSON documents.

.. end_description

.. begin_installation:

Installation
------------

PyWOT works with Python 2.6 and Python 2.7. Install using pip:

.. code-block:: bash

	$ pip install pywot

.. end_installation

.. begin_usage

Usage
-----

Once you obtain your Application ID, you can use it to instantiate new instances of the various classes (Tankopedia, Player, Rating, Vehicles).  The following will get a list of all the tanks in the game:

.. code-block:: pycon
	
	>>> from pywot.tankopedia import Tankopedia	
	>>> t = Tankopedia('your-app-id')
	>>> print(t.list_of_vehicles())

You can get the details of a particular tank with the vehicle_details method.  Here is how you would get the details of the KV-1S:

.. code-block:: pycon
	
	>>> print t.vehicle_details(tank_id=18689)

Or, just get a few fields:

.. code-block:: pycon

	>>> print t.vehicle_details(
		tank_id=18689, 
		fields=['tank_id', 'nation', 'speed_limit', 'engines.module_id'])

The field names can be obtained from the `API Reference <https://na.wargaming.net/developers/api_reference/wot/account/list>`_.  They can be passed in as a comma-delimited string or a python list of string values, as shown above.  You can also pass in multipe tank_id's the same way:

.. code-block:: pycon

	>>> print(t.vehicle_details(tank_id=18689, 	fields=['tank_id','nation','speed_limit','engines.module_id']))

PyWOT also supports specifying different languages for the response:

.. code-block:: pycon

	>>> print(t.vehicle_details(
		language='ko', 
		tank_id=['18689','33'], 
		fields=['tank_id', 'nation', 'speed_limit', 'engines.module_id']))

Querying for player statistics can be done by supplying either an account_id or a nickname.

To get all the achievements of a player with the nickname "lulz_man" do the following:

.. code-block:: pycon

	>>> from pywot.player import Player
	>>> p = Player('your-app-id')
	>>> print(p.player_achievements(nickname='lulz_man'))

The wrapper will handle figuring out what the account_id is.  

If you aren't sure what the player's nickname is, you can use the search_players method to find it.

If you already have an account_id, you can supply that as well.  Here's how to get all the vehicles from a player if his or her account_id is known:

.. code-block:: pycon

	>>> from pywot.player import Player
	>>> p = Player('your-app-id')
	>>> print(p.player_vehicles(1008273454))

.. end_usage

.. begin_license

License
-------

All of the code contained here is licensed by
`the Apache 2.0 License <https://github.com/mattselph/pywot/blob/master/LICENSE>`_.

.. end_license