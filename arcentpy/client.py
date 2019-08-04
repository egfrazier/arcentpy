import requests
import configparser

# TODO: Offload the API Key to a config file so
# that is does not have to be explicity passed in
# in the client creation.
class ArcentpyClient():
	"""Client for interacting with Arcentry."""
	def __init__(self):
		"""Initializes the Arcentry client
		
			:param api_key: Key for authenticating to the Arcentry API
			:type api_key: str
		"""
		config = configparser.ConfigParser()
		config.read('../etc/config.ini')
		self.key = config['Arcentry']['api_key']
		self.endpoint_base = f'https://arcentry.com/api/v1/'
		self.header_base = {f'Authorization': f'Bearer {self.key}'}

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

	def list_docs(self):
		"""Returns a list of all documents in the Arcentry account"""
		endpoint = f'{self.endpoint_base}doc/'
		return self.__get_request(endpoint, self.header_base)

	def describe_doc(self, doc_id):
		"""Returns user, folder creation and change dates on a given document."""
		endpoint = f'{self.endpoint_base}doc/{doc_id}'
		return self.__get_request(endpoint, self.header_base)

	def list_objects(self,doc_id):
		"""Lists the id and type of all objects for a given document."""
		endpoint = f'{self.endpoint_base}doc/{doc_id}'
		return self.__get_request(endpoint, self.header_base)