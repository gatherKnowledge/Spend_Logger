from TelegramBot import TelegramBot as t_bot
from models.Product import Product

# 입출력
# 사용한 금액
# 투자금
# 회수금

## 파일로 만드는 부분을 공통으로 뽑아낼 수 있음
## 텔레그램에 업로드하는 부분을 공통으로

count = 0
# fund 구매 케이스
def buy_fund():
	jongmok = input('종목명?')
	yongdo = input('용도?')

	while True:
		price = input('가격?')
		if price.isdigit():
			break

	while True:
		yang = input('개수는?')
		if yang.isdigit():
			break
	dec = input('기타 추가 설명을 입력해주세요.')
	obj = Product(jongmok, yongdo, yang, dec, price)
	obj.print_obj()
	bot.send_msg(obj.make_str())


def make_memo():
	string = input('메모 입력해주세요.')
	bot.send_msg(string)


#프로그램을 켰을때, 파일로 만들지, 텔레그램으로 전송 할지 선택
def make_choice():
	print('메뉴를 선택해주십시오')
	print(' 1. 펀드 \n 2. 소비 \n 3. 기록 \n 0. 메모')
	while True :
		c = input()
		if c.isdigit() :
			menu_switch(c)
			break


def call_logs():
	bot.req_msg()



def menu_switch(c):
	if c is '1' :
		buy_fund()
	elif c is '3':
		call_logs()

	elif c is '0' :
		make_memo()
class datavalue:
	def __init__(self):
		self.value = 0
		self.year = 0

while True :

	# global variable
	bot = t_bot()
	make_choice()
	condition = input('중단하시려면 quit을 입력해주세요.')
	if condition == 'quit' :
		break
