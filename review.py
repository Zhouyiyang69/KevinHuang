from typing import List
import interactive
import screen_change
import variable
from pynput import keyboard
from pynput.keyboard import Key
import os


def review(track_record: List[str]) -> None:
    interactive.show_table()
    while True:
        if variable.length == len(track_record):
            break
        else:
            current_track = [
                i for i in range(variable.length + 1)
            ]  # make a iterate list
            interactive.show_table()  # init chessboard

            for i in current_track:
                index1 = int(track_record[i][0])
                index2 = int(track_record[i][1])

                if i % 2 == 0:
                    interactive.print_piece_red(0, index1, index2)
                if i % 2 == 1:
                    interactive.print_piece_blue(0, index1, index2)

            detect_next()

    screen_change.screen_back()
    print("\x1bc")
    print("\x1b[0;0HReview Completed")
    os.system("sleep 2")


def detect_next() -> None:
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()


def on_key_release(key) -> bool:
    if key == Key.right:
        variable.length += 1
        return False
    elif key == Key.left:
        if variable.length >= 1:
            variable.length -= 1
        return False


# T = [['1','2'],['3','4'],['5','6'],['7','8'],['9','10']]
# review(T)