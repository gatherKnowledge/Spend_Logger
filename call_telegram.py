import telegram   #텔레그램 모듈을 가져옵니다.

class telegram_instance:
    def __init__(self):
        tokken = '528277663:AAFilePFjxkKhTGHbl45THWcGlsn4wvCqOc'   #토큰을 변수에 저장합니다.
        self.bot = telegram.Bot(token = tokken)   #bot을 선언합니다.
        self.chat_id = self.bot.getUpdates()[-1].message.chat.id #가장 최근에 온 메세지의 chat id를 가져옵니다

    def send_msg(self, string):
        self.bot.sendMessage(chat_id = self.chat_id, text=string)

    def recieve_msg(self):
        updates = self.bot.getUpdates()  #업데이트 내역을 받아옵니다.
        for u in updates :   # 내역중 메세지를 출력합니다.
            print(u.message)
