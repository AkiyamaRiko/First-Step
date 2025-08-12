inp=input('>>>rating? ')
while int(inp)>0:
    if int(inp)>16600:
        print ('不对劲，重新输入')
        inp = input('>>>rating? ')
    if int(inp) >= 14000:
        if int(inp)<15000:
            print('加油，你一定能拿下彩框~')
        else :
            print ('太强啦') # 写个注释试试
    elif int(inp)<14000:
        print('加油，你一定能拿下金框~')
    song = int(inp) / 50
    x = song / 22.512
    y = song / 22.2
    print('你的单曲平均得分是', song)
    print('试着把',x,'推到100.5，把',y,'推到100.0吧。')
    print('')
    inp = input('>>>rating? ')


