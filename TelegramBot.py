import telegram
import keys
from time import localtime, strftime
import json


class TelegramBot:

	def __init__(self):
		self.TOKKEN = keys.telegram_tokken
		self.CHATID = '452265838'
		# self.CHATID = '@money_log'
		self.bot = telegram.Bot(token = self.TOKKEN)

	def send_msg(self, string):
		self.bot.sendMessage(self.CHATID, text=string)

	def req_msg(self):
		updates = self.bot.getUpdates()  # 업데이트 내역을 받아옵니다.
		# for u in updates:
		# 	print(u.message)
		# print(type(updates))
		return updates

if __name__ == '__main__':
	tb = TelegramBot()
	# print(type(tb.req_msg()[0]))
	# print(tb.req_msg()[0].message)
	# print(type(json.dumps(tb.req_msg()[0])))
	# tb.send_msg(string='mesage')
	# tb.send_msg('PROGRAM MESSAGE')
	for msg in tb.req_msg() :
		if msg.message is not None:
			print(msg.message.text)


