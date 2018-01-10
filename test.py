import json


class test:
	def __init__(self, attr):
		self.test_attribute = attr
		self.test_attribute2 = 'test'

	def method1(self):
		print('method1')

	def method2(self):
		print('method2')

	# Class method를 반환
	def getMethodList(self):
		method_list = [func for func in dir(self) if callable(getattr(self, func))]
		m_list = list()
		for method in method_list:
			if not method.startswith('__'):
				# print(method)
				m_list.append(method)
		return m_list

	# Class attr을 반환
	def getAttrList(self):
		return self.__dict__.keys()

	# json style string
	def getInstanceJsonString(self):
		attrs = vars(self)
		string = '{'
		string += ', '.join("%s: %s" % item for item in attrs.items())
		string += '}'
		return string

	# json return
	def getInstanceJson(self):
		test = vars(self)
		return json.dumps(test)
