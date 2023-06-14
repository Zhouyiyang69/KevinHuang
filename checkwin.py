import variable
import interactive


def checkwin (list,point):
    y = 0
    x = 0
    player = 0
    times = 1
    point = list(map(int, point))
    y = point[0]
    x = point[1]
    player = list[point]

    # 右
    for i in range(1,5):
        x = x + 1
        if list[y][x] == player and x <= 11:
            times += 1
        else:
            break

    #讓 x,y ＝ 原來的點
    y = point[0]
    x = point[1]

    #左
    for i in range(1,5):
        x = x - 1
        if list[y][x] == player and x >= 0:
            times += 1
        else:
            break

    if times == 5:
        return(player,2,point)
    else:
        #讓 x,y ＝ 原來的點
        y = point[0]
        x = point[1]
        times = 1

    #上
    for i in range(1,5):
        y = y - 1
        if list[y][x] == player and y >= 0:
            times += 1
        else:
            break

    #讓 x,y ＝ 原來的點
    y = point[0]
    x = point[1]

    # 下
    for i in range(1,5):
        y = y + 1
        if list[y][x] == player and y <= 11:
            times += 1
        else:
            break

    if times == 5:
        return(player,1,point)
    else:
        #讓 x,y ＝ 原來的點
        y = point[0]
        x = point[1]
        times = 1
    
    #右上
    for i in range(1,5):
        x = x + 1
        y = y - 1
        if list[y][x] == player and x <= 11 and y >= 0:
            times += 1
        else:
            break

    #讓 x,y ＝ 原來的點
    y = point[0]
    x = point[1]

    #左下
    for i in range(1,5):
        x = x - 1
        y = y + 1
        if list[y][x] == player and x >= 0 and y <= 11:
            times += 1
        else:
            break

    if times == 5:
        return(player,4,point)
    else:
        #讓 x,y ＝ 原來的點
        y = point[0]
        x = point[1]
        times = 1
    
    #右下
    for i in range(1,5):
        x = x + 1
        y = y + 1
        if list[y][x] == player and x <= 11 and y <= 11:
            times += 1
        else:
            break

    #讓 x,y ＝ 原來的點
    y = point[0]
    x = point[1]

    #左上
    for i in range(1,5):
        x = x - 1
        y = y - 1
        if list[y][x] == player and x >= 0 and y >= 0:
            times += 1
        else:
            break
    if times == 5:
        return(player,3,point)
    else:
        return(0,0,point)












##if __name__ == "__main__":
    interactive.init()
    list1 = variable.chessboard
    #checkwin(list1,list2)
    #print (list1)
    print(list1)
    print(list1)
    #print(interactive.show(list1))
