class Item(object):
	"""docstring for Item"""
	def __init__(self, Item_ID, name, description, bid_info, item_type):
		self._Item_ID = Item_ID
		self._name = name
		self._description = description
		self._bid_info = bid_info
		self._type = item_type

class furniture(object):
	def __init__(self, material, age):
		self._material = material
		self._age = age


class book(object):
	def __init__(self, author, publication_date):
		self._author = author
		self._publication_date = publication_date

class electronics(object):
	def __init__(self, voltage, brand):
		self._voltage = voltage
		self._brand = brand

class customer(object):
	def __init__(self, customer_id, name, items = [], bids = []):
		self._customer_id = customer_id 
		self._name = name
		self._items = items
		self._bids = bids

class bids(object):
	def __init__(self, price, time, bidder_id):
		self._price = price
		self._time = time
		self._bidder_id = bidder_id

class bid_info
	def __init__(self, bids = [], remaining_time):
		self._bids = bids
		self._remaining_time = remaining_time