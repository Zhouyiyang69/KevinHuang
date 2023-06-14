import variable
import interactive


def checkwin (list,point):
    y = 0
    x = 0
    player = 0
    times = 1
    point = list(map(int, point))
    center = [0,0]
    y = point[0]
    x = point[1]
    center[0] = y
    center[1] = x
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
            center[0] = y       #!!讓center保持在最左邊    
            center[1] = x
        else:
            break

    if times == 5:
        #!!center在最左邊
        center[1] = center[1] + 2
        return(player,2,center)
    else:
    #讓 x,y ＝ 原來的點 , center ＝ 原來的點
        y = point[0]
        x = point[1]
        center[0] = y
        center[1] = x
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
            center[0] = y        #!!讓center保持在最下邊
            center[1] = x
        else:
            break

    if times == 5:
        #!!center在最下邊
        center[0] = center[0] - 2
        return(player,1,center)
    else:
        #讓 x,y ＝ 原來的點 , center ＝ 原來的點
        y = point[0]
        x = point[1]
        center[0] = y
        center[1] = x
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
            center[0] = y       #!!讓center保持在最左下邊
            center[1] = x
        else:
            break

    if times == 5:
        #!!center在最左下邊
        center[0] = center[0] - 2
        center[1] = center[1] + 2
        return(player,4,center)
    else:
        #讓 x,y ＝ 原來的點 , center ＝ 原來的點
        y = point[0]
        x = point[1]
        center[0] = y
        center[1] = x
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
            center[0] = y         #!!讓center保持在最左上邊
            center[1] = x
        else:
            break
    if times == 5:
        #!!center在最左上邊
        center[0] = center[0] + 2
        center[1] = center[1] + 2
        return(player,3,center)
    else:
        center[0] = y
        center[1] = x
        return(0,0,center)













