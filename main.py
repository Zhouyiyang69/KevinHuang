import checkwin
import interactive
import review
import dodobird
import variable
import os
import screen_change

if __name__ == "__main__":
    os.system("clear")
    interactive.init()
    interactive.show_table()
    while 1:
        
        player = len(variable.track) % 2
        if player == 0:
            
            num1, num2 = interactive.show_input(1)
            input_list = [num1,num2]
            if dodobird.checkinput(input_list) == False:
                interactive.show_input_back(num1,num2,3)
                continue
            dodobird.save_position(num1, num2)
            os.system("sleep 1")
            interactive.print_piece_red(0,int(num1),int(num2))
            winner, direction, pos = checkwin.checkwin(input_list)
            if winner == 0:
                interactive.show_input_back(num1,num2,3)
                continue
        else:
            num1, num2 = interactive.show_input(2)
            input_list = [num1,num2]
            if dodobird.checkinput(input_list) == False:
                interactive.show_input_back(num1,num2,3)
                continue
            dodobird.save_position(num1, num2)
            os.system("sleep 1")
            interactive.print_piece_blue(0,int(num1),int(num2))
            winner, direction, pos = checkwin.checkwin(input_list)
            if winner == 0:
                interactive.show_input_back(num1,num2,3)
                continue
        interactive.show_input_back(num1,num2,3)
        interactive.print_line(winner, direction, pos)
        os.system("sleep 5")
        if interactive.print_review() == 1:
            review.review(variable.track)
        if interactive.print_replay() == 1:
            interactive.init()
            interactive.show_table()
            continue
        else:
            break
