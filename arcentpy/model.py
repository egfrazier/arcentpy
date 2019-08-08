class Selector():
	def __init__(self, key, operator, value):
		self.key = key
		self.operator = operator
		self.value = value
		self.selector = []

	def set_selector(self):
		self.selector = str([self.key, self.operator, self.value])
		self.selector = self.selector.replace(f' ', f'')
		self.selector = self.selector.replace(f'[', f'%5B')
		self.selector = self.selector.replace(f']', f'%5D')
		self.selector = self.selector.replace(f'\'', f'%22')