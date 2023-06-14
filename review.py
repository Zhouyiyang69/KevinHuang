from typing import List
from interactive import show
import variable
import time

# track = [["1", "3"], ["3", "5"], ["4", "7"], ["7", "10"], ["3", "7"]]


def review(track_record: List[str]) -> None:
    variable.chessboard = [
        [0 for i in range(0, 11)] for j in range(0, 11)
    ]  # init chessboard
    lens_of_track = [i for i in range(len(track_record))]  # make a iterate list

    for i in lens_of_track:
        index1 = int(track_record[i][0])
        index2 = int(track_record[i][1])

        if i % 2 == 0:
            variable.chessboard[index1][index2] = 1
            show(variable.chessboard)
            time.sleep(3)

        if i % 2 == 1:
            variable.chessboard[index1][index2] = 2
            show(variable.chessboard)
            time.sleep(3)

    print("Review Completed")


# if __name__ == "__main__":
#     review(track)
