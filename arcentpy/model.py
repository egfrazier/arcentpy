class Selector():
	def __init__(self, key, operator, value):
		self.key = key
		self.operator = operator
		self.value = value
		self.selector = []

	# TODO: Verify under what (if any) circumstances
	# a select should be set to a string and
	# when it should be kept as a list. May need to
	# reintroduct an "encoding" method.
	def set_selector(self):
		self.selector = [self.key, self.operator, self.value]
		#self.selector = self.selector.replace(f' ', f'')
		#self.selector = self.selector.replace(f'[', f'%5B')
		#self.selector = self.selector.replace(f']', f'%5D')
		#self.selector = self.selector.replace(f'\'', f'%22')