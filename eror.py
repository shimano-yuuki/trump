import random
#カード１枚引く関数
def draw(deck):
    card=deck.pop()
    return card #戻り値
#手札の合計
def calc(hand): #引数（）も好きに名前つけてよい
    s =0
    A =False   #元々はフォルスだが18行目のようになるとsがtrueになるのでそのぷろグラミングを実行する
    for card in hand: #for文のcardの部分は自分でつけた名前でおk
        if 10<card[1]:
            s+=10
        elif 1 == card[1]:
            A=True
            s+=11
        else:
            s+=card[1]
    if s >=22 and A==True:
        s-=10
    return s
#デッキの作成
deck =[]
marks =["H","S","D","C"]
for mark in marks:
    for kazu in range(1,14):
        deck.append([mark,kazu])
#デッキのシャッフル
random.shuffle(deck)
#手札の初期化
player =[]
dealer =[]
for i in range(2):
    player.append(draw(deck))
    dealer.append(draw(deck))
print("プレイヤー")
print(player)
print(calc(player))
print("ディーラー")
print(dealer[0])
while True:
    answer = input("もう一回引きますか(y/n)")
    if answer =="y":
        player.append(draw(deck))
        print(player)
        if calc(player)>=22:
            print("負け")
            exit()
    else: #スタンドの場合
        break
print("ここからディーラー")
print(dealer)
while True:
    if calc(dealer)<=18:
        dealer.append(draw(deck))
    else:
        break

print(dealer)
if calc(player)<calc(dealer):
    if 22<=calc(dealer):
        print("勝ち")
    elif calc(player)<calc(dealer):
        21>=calc(dealer)
        print("負け")
elif calc(player)==calc(dealer):
    print("引き分け")
else:
    print("勝ち")


