# from dodobird import save_position
from dodobird import checkinput
from dodobird import save_position
import init

init.init()
if __name__ == "__main__":
    while True:
        # init.init()
        # print(init.chessboard)
        # print(init.chessboard)
        # print((type(init.chessboard[0][1])))
        a = input("input: ")
        x = [i for i in a]
        # print(type(x))
        # print(len(x))
        # b, c, d = checkinput(x)
        # print(type(checkinput(x)))
        # print(str.isdigit(x[0]))
        b, str1, str2 = checkinput(x)
        save_position(str1, str2)
        # print(init.chessboard)
        # print(init.track)
        # print(type(init.track[0][0]))
        # print(init.track[0][1])
# need dodobird.py & init.py
