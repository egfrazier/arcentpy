import requests
import configparser
import json

from model import Selector

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

	# Helper Methods

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

	def __post_request(self, endpoint, headers, data=None):
		"""Helper function for sending request to the Arcentry API

			:param endpoint: The complete endpoint for the Arcetry REST resource
			:type: str
			:param headers: A dictionary of key/value HTTP header pairs
			:type: dict
			:return: Returns a response from the Arcentry API
			:rtype: Requests Response object
		"""
		headers.update({f'Content-Type': f'application/json'})
		return requests.post(endpoint, data, headers=headers).json()

	def __create_selector(self, key, operator, value):
		selector = Selector(key, operator, value)
		return selector

	# Document Methods

	def list_docs(self):
		"""Returns a list of all documents in the Arcentry account"""
		endpoint = f'{self.endpoint_base}doc/'
		return self.__get_request(endpoint, self.header_base)

	def create_doc(self, title):
		"""Creates a new document"""
		endpoint = f'{self.endpoint_base}doc/create'
		data = {
			"title": title
		}
		data = json.dumps(data)
		return self.__post_request(endpoint, self.header_base, data)

	def describe_doc(self, doc_id):
		"""Returns user, folder creation and change dates on a given document."""
		endpoint = f'{self.endpoint_base}doc/{doc_id}'
		return self.__get_request(endpoint, self.header_base)

	def empty_doc(self,doc_id):
		"""Deletes all objects from a given document"""
		endpoint = f'{self.endpoint_base}doc/empty'
		data = {
			"docId": doc_id
		}
		data = json.dumps(data)
		return self.__post_request(endpoint, self.header_base, data)

	def add_collaborator(self,doc_id,collab_email):
		"""Add another Arcentry account as a collaborator
			to a given document"""
		endpoint = f'{self.endpoint_base}doc/add-collaborator'
		data = {
			"docId": doc_id,
			"email": collab_email
		}
		data = json.dumps(data)
		return self.__post_request(endpoint, self.header_base)

	def update_doc_title(self,doc_id,title):
		"""Update title of a given document"""
		endpoint = f'{self.endpoint_base}doc/change-title'
		data = {
			"docId": doc_id,
			"title": title
		}
		data = json.dumps(data)
		return self.__post_request(endpoint, self.header_base, data)

	def clone_doc(self,doc_id,title):
		"""Clone new document from an existing one"""
		endpoint = f'{self.endpoint_base}doc/clone'
		data = {
			"docId": doc_id,
			"title": title
		}
		data = json.dumps(data)
		return self.__post_request(endpoint, self.header_base, data)

	def delete_doc(self,doc_id):
		"""Delete a document with a given ID"""
		endpoint = f'{self.endpoint_base}doc/delete'
		data = {
			"docId": doc_id
		}
		data = json.dumps(data)
		return self.__post_request(endpoint, self.header_base, data)

	# Object Methods

	def list_objects(self,doc_id):
		"""Lists the id and type of all objects for a given document."""
		endpoint = f'{self.endpoint_base}doc/{doc_id}/obj/'
		return self.__get_request(endpoint, self.header_base)

	def describe_objects(self,doc_id):
		"""List all objects and their properties for a given document."""
		endpoint = f'{self.endpoint_base}doc/{doc_id}/obj/all'
		return self.__get_request(endpoint, self.header_base)

	def describe_object(self,doc_id, obj_id):
		"""Describe all data for a given object in a given document"""
		endpoint = f'{self.endpoint_base}doc/{doc_id}/obj/{obj_id}'
		return self.__get_request(endpoint, self.header_base)

	def list_by_selector(self, doc_id, key, operator, value):
		"""List all objects that match the given selector"""
		selector_obj = self.__create_selector(key, operator, value)
		selector_obj.set_selector()
		selector_str = selector_obj.selector
		endpoint = f'{self.endpoint_base}doc/{doc_id}/obj/where/{selector_str}'
		return self.__get_request(endpoint, self.header_base)

	def put_object(self,doc_id, obj_type, props={}, ):
		"""Lists the id and type of all objects for a given document."""
		endpoint = f'{self.endpoint_base}doc/{doc_id}/obj/'
		data = {
			"type": obj_type,
			"props": props
		}
		data = json.dumps(data)
		return self.__post_request(endpoint, self.header_base, data)

	def update_object(self,doc_id, obj_id, props):
		"""Updates one or more properties for an object."""
		endpoint = f'{self.endpoint_base}doc/{doc_id}/obj/{obj_id}'
		data = {
			"props": props
		}
		data = json.dumps(data)
		return self.__post_request(endpoint, self.header_base, data)

	def delete_object(self,doc_id, obj_id):
		"""Deletes an object from the document given its object ID"""
		endpoint = f'{self.endpoint_base}doc/{doc_id}/obj/{obj_id}/delete'
		return self.__post_request(endpoint, self.header_base)

	# TODO: Bulk Delete