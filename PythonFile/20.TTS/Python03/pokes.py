#模拟斗地主发牌
import random
def pokes():
    kinds = ['\u2660','\u2663','\u2665','\u2666']
    numbers = ['A'] + list('JQK') + list(map(str,range(2,11)))
    pokes = ['king','queen'] + [x+y for x in kinds
                                for y in numbers]
    #print(pokes)
    #print(len(pokes))
    return pokes

def send_poker(pokes):
    random.shuffle(pokes)
    num = 1
    start =0
    end =17
    while num <= 3:
        input('输入回车之后开始发牌：')
        print('第%d个人的牌是:' % num, pokes[start:end])
        start += 17
        end += 17
        num += 1
    print('底牌是', pokes[51:])

def happyfightrichpeople():
    allpokes = pokes()
    send_poker(allpokes)


if __name__ == '__main__':
    happyfightrichpeople()
