from typing import List
import variable


def init() -> List[int]:
    variable.chessboard = [[0 for i in range(0, 11)] for j in range(0, 11)]
    variable.track = []
    # global track
    # global chessboard
    # chessboard = [[0 for i in range(0, 11)] for j in range(0, 11)]
    # track = []


def show(bb):
    print("\033[2J")
    for i in range(0,11):
        for j in range(0,11):
            if bb[i][j] == 0:
                if j < 10:
                    print("+", end=" ")
                else:
                    print("+")
            if bb[i][j] == 1:
                if j < 10:
                    print("\033[31mO"+"\033[0m", end=" ") #重置顏色
                else:
                    print("\033[31mO"+"\033[0m")
            if bb[i][j] == 2:
                if j < 10:
                    print("O", end=" ")
                else:
                    print("O")


if __name__ == "__main__":
    init()
    # print(chessboard)
    # print(track)
    show(variable.chessboard)
