import requests

# TODO: Offload the API Key to a config file so
# that is does not have to be explicity passed in
# in the client creation.
class ArcentpyClient():
	"""Client for interacting with Arcentry."""
	def __init__(self, api_key=None):
		"""Initializes the Arcentry client
		
			:param api_key: Key for authenticating to the Arcentry API
			:type api_key: str
		"""
		self.api_key = api_key
		self.endpoint_base = f"https://arcentry.com/api/v1/"
		self.header_base = {f"Authorization": f"Bearer {self.api_key}"}

	def __get_request(self, endpoint, headers):
		"""Helper function for sending request to the Arcentry API

			:param endpoint: The complete endpoint for the Arcetry REST resource
			:type: str
			:param headers: A dictionary of key/value HTTP header pairs
			:type: dict
			:return: Returns a response from the Arcentry API
			:rtype: Requests Response object
		"""
		return requests.get(endpoint,headers=headers).json()

	def get_docs(self):
		"""Returns a list of all documents in the Arcentry account"""
		endpoint_stub = f"doc"
		endpoint = f"{self.endpoint_base}{endpoint_stub}"
		print(endpoint)
		headers = self.header_base
		print(headers)
		return self.__get_request(endpoint,headers)
