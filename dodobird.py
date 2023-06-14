import init


def save_position(str1, str2):
    init.track.append([])
    i = len(init.track) - 1
    if (i % 2) == 0:  # player1
        init.chessboard[int(str1)][int(str2)] = 1
        init.track[i].append(str1)
        init.track[i].append(str2)
    elif (i % 2) == 1:  # player2
        init.chessboard[int(str1)][int(str2)] = 2
        init.track[i].append(str1)
        init.track[i].append(str2)


def checkinput(list1: list):
    if (len(list1) < 3) or (len(list1) > 5):
        print("Wrong input type!")
        return False, False, False
    if len(list1) == 3:
        if (str.isdigit(list1[0]) == False) or (str.isdigit(list1[2]) == False):
            print("Wrong input type!")
            return False, False, False
        else:
            str1 = list1[0]
            str2 = list1[2]
    elif len(list1) == 4:
        if list1[1] == " ":
            strA = list1[0]
            strB = list1[2] + list1[3]
            if (str.isdigit(strA) == False) or (str.isdigit(strB) == False):
                print("Wrong input type!")
                return False, False, False
            elif int(strB) > 10:
                print("Out of range!")
                return False, False, False
            else:
                str1 = strA
                str2 = strB
        elif list1[2] == " ":
            strA = list1[0] + list1[1]
            strB = list1[3]
            if (str.isdigit(strA) == False) or (str.isdigit(strB) == False):
                print("Wrong input type!")
                return False, False, False
            elif int(strA) > 10:
                print("Out of range!")
                return False, False, False
            else:
                str1 = strA
                str2 = strB
        else:
            print("Wrong input type!")
            return False, False, False
    elif len(list1) == 5:
        strA = list1[0] + list1[1]
        strB = list1[3] + list1[4]
        if (
            (list1[2] != " ")
            or (str.isdigit(strA) == False)
            or (str.isdigit(strB) == False)
        ):
            print("Wrong input type!")
            return False, False, False
        elif (int(strA) != 10) or (int(strB) != 10):
            print("Out of range!")
            return False, False, False
        else:
            str1 = strA
            str2 = strB
    if init.chessboard[int(str1)][int(str2)] != 0:
        print("This place already has a chess!")
        return False, False, False
    else:
        return True, str1, str2


# first version
