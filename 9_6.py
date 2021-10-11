from typing_extensions import ParamSpec


def isreipier(seireki):
    if seireki%400==0:
        return True
    elif seireki %4 ==0 and seireki%100 !=0:#!=０は０にならないいう意味
        return True
    else:
        return False



seireki = input("西暦を入力してください、閏年かどうか判断します")
flag = isreipier(seireki)
print("西暦は{}年は、"format(seireki),end=" ")
if flag:
    print("うるう年です")
else:
    print("閏年ではありません")

def take_bus():
    print("バスに乗ります")

def run():
    print("走ります")

def walk():
    print("ちょっと歩きます")

print("行ってきます")
walk();take_bus();run();run()
print("ただいま")

def int_input(message):
    return int(input("{}をにゅうりょくしてください".fomat(message)))

def calc_payment(amount,people =2):
    dnum =amount /people
    pay =dnum//100*100
    if dnum > pay:
        pay =int(pay+100)
    payorg =amount -pay*(people-1)
    
    return[int(pay),int(payorg]

def sho_payment(pay,pyorg,people=2):
    print("*** 支払い額　***")
    print("一人当たり{}円({}人)、幹事は{}円です".fomat(pay,people-1,payorg))

amount = int_input("支払い額")
people = int_input("参加人数")
pay_list =calc_payment(amount,people)
show_payment(pay_list[0],pay_list[1],people)