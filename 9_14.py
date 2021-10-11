import random

def draw(deck):
    card=deck.pop()
    return card

def calc(hand): 
    s =0
    for card in hand: 
        if 9<card[1]:
            s+=0
        else:
            s+=card[1]
    return s

def make_deck():
    deck =[]
    marks =["♡","♤","♢","♧"]
    for mark in marks:
        for kazu in range(1,14):
            deck.append([mark,kazu])
        
    random.shuffle(deck)
    return deck

deck = make_deck()
player =[]
banker =[]

money = 1000

while True :
    print("現在の所持金は"+str(money)+"円です。")
    if money<=0:
        print("所持金は０円になりました。")
        break
    predict = int(input("[誰に賭けますか？プレイヤー；０、バンカー；１、引き分け；２]2"))
    bet = int(input("いくら賭けますか？"))
    if money<bet:
        bet = money
        print("全財産を賭け金とします。")
    money-=bet
    if len(deck)<=10:
        deck = make_deck()
    #プレーヤー・バンカーの順番で2枚ずつ交互に配布
    for i in range(2):
        player.append(draw(deck))
        banker.append(draw(deck))
    print(player)
    print(banker)

    pghyouka = (int(str(calc(player))[-1]))
    bghyouka = (int(str(calc(banker))[-1]))
    print(pghyouka)
    print(bghyouka)


    #プレーヤーの合計 (1の位のみ)がどれに当てはまるかを見て2枚または3枚のプレーヤーの値を決める。
    if  8<=pghyouka<10 or 8<=bghyouka<10:  #プレーヤーの合計　8・9　勝負判定 
        if pghyouka>bghyouka:
            result="player"
        elif pghyouka<bghyouka:
            result="banker"
        elif pghyouka==bghyouka:
            result="tie"
        else:
            if pghyouka>bghyouka:
                result="player"
            elif pghyouka<bghyouka:
                result="banker"
            elif pghyouka==bghyouka:
                result="tie"
    elif 6<=pghyouka<8 and bghyouka<6:  #プレーヤーの合計6・7 もう引かない
        banker.append(draw(deck))  #プレーヤーが2枚目で終了の場合、バンカーが、0~5の場合はバンカーはもう一枚引く。
        print("バンカーの２枚での合計が、0~5でバンカーはもう一枚引く。")  
        print(banker)
        print((int(str(calc(banker))[-1])))
        if pghyouka>(int(str(calc(banker))[-1])):
            result="player"
        elif pghyouka<(int(str(calc(banker))[-1])):
            result="banker"
        elif pghyouka==(int(str(calc(banker))[-1])):
            result="tie"
        else:
            if pghyouka>(int(str(calc(banker))[-1])):
                result="player"
            elif pghyouka<(int(str(calc(banker))[-1])):
                result="banker"
            elif pghyouka==(int(str(calc(banker))[-1])):
                result="tie"
    elif pghyouka<6: #プレーヤーの２枚での合計が0~5
        player.append(draw(deck))#もう一枚引く、プレーヤーが3枚目で終了の場合
        print("プレーヤーの２枚での合計が0~5でプレイヤーはもう一枚引く")
        print(player)
        print((int(str(calc(player))[-1])))
        if bghyouka<3:  #バンカー０〜２
            banker.append(draw(deck))
            print("バンカーの２枚での合計が０〜２で、バンカーはもう一枚引く")
            print(banker)
            print((int(str(calc(banker))[-1])))
            if (int(str(calc(player))[-1]))>(int(str(calc(banker))[-1])):
                result="player"
            elif (int(str(calc(player))[-1]))<(int(str(calc(banker))[-1])):
                result="banker"
            elif (int(str(calc(player))[-1]))==(int(str(calc(banker))[-1])):
                result="tie"
        elif bghyouka ==3 and 0<=pghyouka<8:  #バンカー３（プレイヤーの３枚目が０〜７の時はバンカーはもう一枚引く）
            banker.append(draw(deck))
            print("banker3のルールでバンカーがもう一枚引く")
            print(banker)
            print((int(str(calc(banker))[-1])))
            if (int(str(calc(player))[-1]))>(int(str(calc(banker))[-1])):
                result="player"
            elif (int(str(calc(player))[-1]))<(int(str(calc(banker))[-1])):
                result="banker"
            elif (int(str(calc(player))[-1]))==(int(str(calc(banker))[-1])):
                result="tie"
        elif bghyouka ==4 and 2<=pghyouka<8:  #バンカー４（プレイヤー３枚目が２〜７の時はバンカーはもう一枚引く）
            banker.append(draw(deck))
            print("バンカー３のルールでバンカーがもう一枚引く")
            print(banker)
            print((int(str(calc(banker))[-1])))
            if (int(str(calc(player))[-1]))>(int(str(calc(banker))[-1])):
                result="player"
            elif (int(str(calc(player))[-1]))<(int(str(calc(banker))[-1])):
                result="banker"
            elif (int(str(calc(player))[-1]))==(int(str(calc(banker))[-1])):
                result="tie"
        elif bghyouka ==5 and 4<=pghyouka<8:  #バンカ−５（プレイヤーの３枚目が４〜７の時はバンカーはもう一枚引く）
            banker.append(draw(deck))
            print("バンカー５のルールでバンカーがもう一枚引く")
            print(banker)
            print(((int(str(calc(banker))[-1]))))
            if (int(str(calc(player))[-1]))>((int(str(calc(banker))[-1]))):
                result="player"
            elif (int(str(calc(player))[-1]))<((int(str(calc(banker))[-1]))):
                result="banker"
            elif (int(str(calc(player))[-1]))==((int(str(calc(banker))[-1]))):
                result="tie"
        elif bghyouka ==6 and 6<=pghyouka<8:  #バンカー６(プレイヤー３枚目が６、７の時バンカーはもう一枚引く)
            banker.append(draw(deck))
            print("バンカー６のルールでバンカーがもう一枚引く")
            print(banker)
            print(((int(str(calc(banker))[-1]))))
            if (int(str(calc(player))[-1]))>((int(str(calc(banker))[-1]))):
                result="player"
            elif (int(str(calc(player))[-1]))<((int(str(calc(banker))[-1]))):
                result="banker"
            elif (int(str(calc(player))[-1]))==((int(str(calc(banker))[-1]))):
                result="tie"
        else:
            if (int(str(calc(player))[-1]))>bghyouka:
                result="player"
            elif (int(str(calc(player))[-1]))<bghyouka:
                result="banker"
            elif (int(str(calc(player))[-1]))==bghyouka:
                result="tie"
    else:
        if pghyouka>bghyouka:
            result="player"
        elif pghyouka<bghyouka:
            result="banker"
        elif pghyouka==bghyouka:
            result="tie"

    if result =="player":
        print("プレイヤーの勝ち")
        if predict==0:
            print("賭けに勝しました。")
            money+=bet*2
            print("現在の所持金"+str(money))
    elif result =="banker":
        print("バンカーの勝ち")
        if predict==1:
            print("賭けに勝しました。")
            money+=bet*1.95
            print("現在の所持金"+str(money))
    else:
        print("引き分けでした。")
        if predict==2:
            print("賭けに勝しました。")
            money+=bet*9
            print("現在の所持金"+str(money))


        
    