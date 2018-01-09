import datetime
import call_telegram
# now = datetime.datetime.now()


# nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')#
# print(nowDatetime)  # 2015-04-19 12:11:32

# 입출력
# 사용한 금액
# 투자금
# 회수금
#

# 차이가 나는 부분, obj를 만드는 부분.

## 파일로 만드는 부분을 공통으로 뽑아낼 수 있음
## 텔레그램에 업로드하는 부분을 공통으로

#프로그램을 켰을때, 파일로 만들지, 텔레그램으로 전송 할지 선택
#

def make_choice():

    print('메뉴를 선택해주십시오')
    print(' 1. 지출 \n 2. 펀드 매수 \n 3. 펀드매도 \n 4. asdfasf')
    c = input()
    menu_switch(c)

def menu_switch(c):
    if c is '1' :
        jongmok = input('종목명?')
        yongdo = input('용도?')

        while True:
            price = input('가격?')
            if price.isdigit() :
               break

        while True:
            yang = input('개수는?')
            if yang.isdigit() :
               break

        dec = input('기타 추가 설명을 입력해주세요.')

        mObj = MoneyObject(jongmok, yongdo, yang, dec, price)
        mObj.print_obj()
        bot.send_msg(mObj.make_str())


class MoneyObject:
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


while True :
    bot = call_telegram.telegram_instance()
    make_choice()
    condition = input('중단하시려면 quit을 입력해주세요.')
    if condition == 'quit' :
        break
