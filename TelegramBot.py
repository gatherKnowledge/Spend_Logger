import telegram
import keys


class TelegramBot:

	def __init__(self):
		tokken = keys.telegram_tokken
		self.bot = telegram.Bot(token = tokken)

	def send_msg(self, string):
		self.bot.sendMessage(chat_id='@money_log', text=string)

	def req_msg(self):
		updates = self.bot.getUpdates()  #업데이트 내역을 받아옵니다.
		for u in updates :   # 내역중 메세지를 출력합니다.
			print(u.message)