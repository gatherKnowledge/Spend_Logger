import datetime
import json


class Product:
	def __init__(self, product, yongdo, yang, dec, price):
		self.product = product
		self.yongdo = yongdo
		self.yang = yang
		self.dec = dec
		self.date = datetime.datetime.now()
		self.price = price
		self.total_price = int(self.yang) * int(self.price)

	def make_str(self):
		strn = '\n\n'
		strn += self.date.strftime('%Y-%m-%d %H:%M:%S')
		strn += '\n\''+self.product + '\'을/를 '+ self.price+'에 ' + self.yang + '개 ' + self.yongdo + '했습니다.'
		strn += '\n비고 : '+ self.dec
		strn += '\n총 ' + str(self.total_price) + '원'
		return strn

	def print_obj(self):
		strn = self.make_str()
		print(strn)

	# json style object data
	def getInstanceJson(self):
		test = vars(self)
		return json.dumps(test)