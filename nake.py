# 주식게임
# 기본 지급금 : 100000원
# 상장 회사 : 삼성, LG, 하이마트, 이마트, 구글
# 랜덤함수를 사용해 자동으로 주식값이 오르내리게 할 생각

from random import *

class Company :
    def __init__(self, name) :
        self.name = name
    money = 9999
    upDown = 0.0
    mose = ""
    def change(self) :
        upDown = randrange(0, 201)
        mosechoice = randint(0, 2)
        if mose == 0 : 
            self.money = self.money - upDown
            mose = "-" + upDown
        else :
            self.money = self.money + upDown
            mose = "+" + upDown
    buyCheck = 0
    buyCompany = 0
    def Buy(self, buyCompany) :
        self.buyCheck = self.upDown
        self.buyCompany = buyCompany
    

companys = []
companys.append(Company("삼성"))
companys.append(Company("LG"))
companys.append(Company("하이마트"))
companys.append(Company("이마트"))
companys.append(Company("구글"))

mymoney = 100000

# 튜토리얼 출력
def tutorial():
    print("< 주식게임을 시작합니다 >")
    print("< 기본 지급금액 1000000원 입니다 >")
    print("< 자산이 0원이 되면 파산으로 게임이 끝납니다 >")
    print("< companys 명령을 입력하시면 각 회사들의 주식현황을 볼 수 있습니다 >")
    print("< buy 명령을 입력하시면 회사 선택창이 나오고 선택하시면 회사의 주식을 사실 수 있습니다 >")
    print("< sell 명령을 입력하시면 회사 선택창이 나오고 선택하시면 회사의 주식을 판매 하실 수 있습니다 >")
    answer = input("* 게임을 시작하시겠습니까?(y/n) >> ")
    try :
        if answer == 'n' :
            raise ValueError
        elif answer != 'y' :
            raise ValueError
        
    except ValueError :
        print("< 이용해 주셔서 감사합니다 >")

def Companys() :
    print()
    print("< 현재 회사 정보 >")
    for i in range(5) :
        companys[i].change()
        print(companys[i].name + " 현재 주식 : " + companys[i].money + " 증감률 : " + companys[i].mose)

def Buy() :
    print()
    global mymoney
    print("< 살 회사를 선택하여 주세요 >")
    for i in range(5) :
        print(i+1 + " : " + companys[i].name)
    choose = input(">>")
    if choose <=0 and choose >5 :
        print("< 지정되지 않은 회사입니다 >")
    else :
        if choose == '1' :
            buyMoney = int(input("사실 금액을 적어주세요 >> "))
            if mymoney < buyMoney :
                print("< 보유 금액이 부족합니다 >")
            else :
                mymoney = mymoney - buyMoney
                companys[0].Buy(buyMoney)
                print("< 주식 구매가 성공적으로 이루어 졌습니다 >")
        elif choose == '2' :
            buyMoney = input("사실 금액을 적어주세요 >> ")
            if buyMoney > mymoney :
                print("< 보유 금액이 부족합니다 >")
            else :
                mymoney = mymoney - buyMoney
                companys[1].Buy(buyMoney)
                print("< 주식 구매가 성공적으로 이루어 졌습니다 >")
        elif choose == '3' :
            buyMoney = input("사실 금액을 적어주세요 >> ")
            if buyMoney > mymoney :
                print("< 보유 금액이 부족합니다 >")
            else :
                mymoney = mymoney - buyMoney
                companys[2].Buy(buyMoney)
                print("< 주식 구매가 성공적으로 이루어 졌습니다 >")
        elif choose == '4' :
            buyMoney = input("사실 금액을 적어주세요 >> ")
            if buyMoney > mymoney :
                print("< 보유 금액이 부족합니다 >")
            else :
                mymoney = mymoney - buyMoney
                companys[3].Buy(buyMoney)
                print("< 주식 구매가 성공적으로 이루어 졌습니다 >")
        elif choose == '5' :
            buyMoney = input("사실 금액을 적어주세요 >> ")
            if buyMoney > mymoney :
                print("< 보유 금액이 부족합니다 >")
            else :
                mymoney = mymoney - buyMoney
                companys[4].Buy(buyMoney)
                print("< 주식 구매가 성공적으로 이루어 졌습니다 >")

def Sell():
    print()
    print("< 판매할 회사를 선택하여 주세요 >")
    for i in range(5) :
        print(i+1 + " : " + companys[i].name)
    choose = int(input(">> "))
    if choose <= 0 and choose > 5 :
        print("< 지정되지 않은 회사입니다 >")
    else :
        if choose == 1 :
            if companys[0].buyCheck == 0 :
                print("< 해당 회사를 사지 않았습니다 >")
            else :
                companys[0].change()
                temp = 0
                global mymoney 
                if companys[0].money > companys[0].buyCheck:
                    temp = companys[0].money - companys[0].buyCheck
                    mymoney = mymoney - temp
                    print("< 총 " + temp + "만큼의 손해를 입얻습니다 >")
                else :
                    temp = companys[0].buyCheck - companys[0].money
                    
                    mymoney = mymoney + temp + companys[0].buyCompany
                    print("< 총 " + temp + companys[0].buyCompany + "만큼의 수익을 얻었습니다 >")
                    
        elif choose == 2:
            if companys[1].buyCheck == 0 :
                print("< 해당 회사를 사지 않았습니다 >")
            else :
                companys[1].change()
                temp = 0
                if companys[1].money > companys[1].buyCheck:
                    temp = companys[1].money - companys[1].buyCheck
                    global mymoney 
                    mymoney = mymoney - temp
                    print("< 총 " + temp + "만큼의 손해를 입얻습니다 >")
                else :
                    temp = companys[0].buyCheck - companys[1].money
                    global mymoney
                    mymoney = mymoney + temp + companys[1].buyCompany
                    print("< 총 " + temp + companys[1].buyCompany + "만큼의 수익을 얻었습니다 >")
        elif choose == 3 :
            if companys[2].buyCheck == 0 :
                print("< 해당 회사를 사지 않았습니다 >")
            else :
                companys[2].change()
                temp = 0
                if companys[2].money > companys[2].buyCheck:
                    temp = companys[2].money - companys[2].buyCheck
                    global mymoney 
                    mymoney = mymoney - temp
                    print("< 총 " + temp + "만큼의 손해를 입얻습니다 >")
                else :
                    temp = companys[2].buyCheck - companys[2].money
                    global mymoney
                    mymoney = mymoney + temp + companys[2].buyCompany
                    print("< 총 " + temp + companys[2].buyCompany + "만큼의 수익을 얻었습니다 >")
        elif choose == 4 :
            if companys[3].buyCheck == 0 :
                print("< 해당 회사를 사지 않았습니다 >")
            else :
                companys[3].change()
                temp = 0
                if companys[3].money > companys[3].buyCheck:
                    temp = companys[3].money - companys[3].buyCheck
                    global mymoney 
                    mymoney = mymoney - temp
                    print("< 총 " + temp + "만큼의 손해를 입얻습니다 >")
                else :
                    temp = companys[3].buyCheck - companys[3].money
                    global mymoney
                    mymoney = mymoney + temp + companys[3].buyCompany
                    print("< 총 " + temp + companys[3].buyCompany + "만큼의 수익을 얻었습니다 >")
        else :
            if companys[4].buyCheck == 0 :
                print("< 해당 회사를 사지 않았습니다 >")
            else :
                companys[4].change()
                temp = 0
                if companys[4].money > companys[4].buyCheck:
                    temp = companys[4].money - companys[4].buyCheck
                    global mymoney 
                    mymoney = mymoney - temp
                    print("< 총 " + temp + "만큼의 손해를 입얻습니다 >")
                else :
                    temp = companys[4].buyCheck - companys[4].money
                    global mymoney
                    mymoney = mymoney + temp + companys[4].buyCompany
                    print("< 총 " + temp + companys[4].buyCompany + "만큼의 수익을 얻었습니다 >")




def main():
    tutorial()
    print("< 주식 게임을 시작합니다 >")
    print()
    while True:
        print("현재 나의 자산 : " + mymoney)
        order = input("명령을 입력해주세요 >> ")
        if order == "companys" :
            Companys()
        elif order == "buy" :
            Buy()
        elif order == "sell" :
            Sell()
        else:
            print("< 정해지지 않은 명령입니다 >")
    

main()