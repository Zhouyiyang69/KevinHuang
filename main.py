def Init():
    return


def Show():
    return


def BlinkBoard():
    return


def SavePosition():
    return


def Review():
    return


def CheckInpuit():
    return


def CheckWin():
    return


chessboard, track = Init()
Show()
while 1:
    position = input("")
    if CheckInpuit(position, chessboard) == False:
        continue
    chessboard, track = SavePosition(position, chessboard, track)
    Show(chessboard)
    Win = CheckWin(chessboard, position)
    if Win[0] == 0:
        continue
    BlinkBoard(Win)
    review = input('Review or no (Y/N)')
    if review == 'Y':
        Review()
    again = input('Play again? (Y/N)')
    if again == 'Y':
        Init()
        Show()
        continue
    else:
        break
