import random
hand = ["グー","チョキ","パー"]
face = ["上","左","右","下"]
finger = ["↑","←","→","↓"]
print("あっち向いてホイをしよう！")
n = int(input("何試合しますか？"))
def play():
    print("0:上 1:左 2:右 3:下")
    a = int(input("あっち向いて・・・"))
    z=random.randint(0,3)
    print("プレイヤー {0} モンスター {1}".format(finger[a],face[z]))
    if a==z:
        print("プレイヤーの勝ち")
        global n
        n -= 1
    else:
       print("ハズレ！")
       main()
def play1():
    print("0:上 1:左 2:右 3:下")
    b = int(input("どっちに向く？"))
    z=random.randint(0,3)
    print("モンスター　{0} プレイヤー　{1}".format(finger[z],face[b]))
    if b==z:
        print("プレイヤーの負け")
        global n
        n -=1
    else:
        print("お前の負け！")
        main()
def janken():
    y=random.randint(0,2)
    print("0:グー　1:チョキ　2:パー")
    p = int(input("じゃんけん・・・"))
    player = hand[p]
    print("プレイヤー{0} モンスター{1}".format(hand[p],hand[y]))
    if p==y:
        print("あいこ")
    elif p==0 and y==1 or p==1 and y==2 or p==2 and y==0:
        print("プレイヤーの勝ち")
        play()
    else:
        print("相手の勝ち")
        play1()
def main():
    for i in range(n):
        janken()
if __name__ == '__main__':
    main()


