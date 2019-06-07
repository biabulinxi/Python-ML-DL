# @Project:AID1810
# @Author:biabu
# @Date:2018-11-19 22:16
# @File_name:exercise2_poker.py 
# @IDE:PyCharm

import random as R


def fun1(a,L):
    lst = []
    for i in L:
        b = a + str(i)
        lst.append(b)
    return lst

def deal(lst):
    pokers = []
    count = 0
    while True:
        count += 1
        poker = R.choice(lst)
        pokers.append(poker)
        lst.remove(poker)
        if count == 17:
            break
    return pokers


def main():
    spade = '\u2660'
    hearts = '\u2666'
    plum = '\u2663'
    diamonds = '\u2665'
    poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    spade_poker = fun1(spade, poker)
    hearts_poker = fun1(hearts, poker)
    plum_poker = fun1(plum, poker)
    diamonds_poker = fun1(diamonds, poker)
    list1 = spade_poker + hearts_poker + plum_poker + diamonds_poker + ["大王","小王"]
    #洗牌
    R.shuffle(list1)
    #发牌
    first = list1[:17]
    secend = list1[17:34]
    third = list1[34:51]
    dipai = list1[51:]
    # secend = deal(list1)
    # third = deal(list1)

    input()
    print('第一个人的牌为：',first)
    input()
    print('第二个人的牌为：',secend)
    input()
    print('第三个人的牌为：',third)
    input()
    print("底牌为：",dipai)

main()

