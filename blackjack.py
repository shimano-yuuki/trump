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

deck =[]
marks =["♡","♤","♢","♧"]
for mark in marks:
    for kazu in range(1,14):
        deck.append([mark,kazu])
    
random.shuffle(deck)

player =[]
banker =[]
for i in range(2):
    player.append(draw(deck))
    banker.append(draw(deck))
print(player)
print(banker)
p2hyouka = (int(str(calc(player))[-1]))
b2hyouka = (int(str(calc(banker))[-1]))
print(p2hyouka)
print(b2hyouka)

if p2hyouka<6:
    player.append(draw(deck))
elif 6<=p2hyouka<8 and b2hyouka<6:
    banker.append(draw(deck))
elif 8<=p2hyouka<10:
    if p2hyouka>b2hyouka:
        print("勝利")
    elif p2hyouka<b2hyouka:
        print("敗北")
    elif p2hyouka==b2hyouka:
        print("引き分け")