
#This is the grid of the game map: 4 in a row

MAP = [
    ['.', '.', '.', '.', '.','.', '.'],
    ['.', '.', '.', '.', '.','.', '.'],
    ['.', '.', '.', '.', '.','.', '.'],
    ['.', '.', '.', '.', '.','.', '.'],
    ['.', '.', '.', '.', '.','.', '.'],
    ['.', '.', '.', '.', '.','.', '.'],
]


class Actions:

    def turns(self):
        """
        prints out whose turn it is right now
        :return: None
        """
        print("It's {0}'s turn".format(self.player_name))



    def get_grid(self):

        """
        Method that returns displays the game's grid.
        :return: None
        """

        for row in MAP:
            print(" ".join(row))

    def drop_piece_player(self, column):

        """
        The method used for the game action, performed by either players

        :param column: User's choice of column
        :return: True if a mark was inserted, False if column was full; False repeats the user's turn
        """

        column -= 1  # user inputs 1-7, Python is 0-6
        if column < 0 or column > 6:
            raise ValueError

        for row in range(5, -1, -1):  # start from bottom row
            if MAP[row][column] == '.':
                MAP[row][column] = self.player_mark
                return True  # If the slot is vacant the dot is replaced with an X; We start iterating over the lists from bottom to top

        print("Column is full!")  # In case the return doesn't trigger the while loop continues
        return False


    def victory(self):
        for row in MAP:
            if self.player_mark * 4 in "".join(row):   # row victory
                print(f"{self.player_name} wins! Row victory obtained!")
                return True

        for col in range(7):  # columns 0 → 6           #column victory
            count = 0
            for row in range(6):  # rows 0 → 5
                if MAP[row][col] == self.player_mark:    #row changes more often then col; exactly what we want!
                    count += 1
                    if count == 4:
                        print(f"{self.player_name} wins! Column victory!")
                        return True
                else:
                    count = 0  # reset streak



        # ---- Diagonal down-right check ----
        for row in range(3):  # row 0..2, enough space for 4 in a row; Only rows 0,1 and 2 can provide a diagonal victory
            for col in range(4):  # col 0..3;  If the diagonal is from the left
                if all(MAP[row + i][col + i] == self.player_mark for i in range(4)):
                    print(f"{self.player_name} wins! Diagonal down-right victory!")
                    return True

        # ---- Diagonal down-left check ----
        for row in range(3):  # row 0..2
            for col in range(3, 7):  # col 3..6; If the diagonal is from the left
                if all(MAP[row + i][col - i] == self.player_mark for i in range(4)):
                    print(f"{self.player_name} wins! Diagonal down-left victory!")
                    return True



        return False




class Player1(Actions):
    def __init__(self, player_name):
        self.player_name = player_name   #Haven't used this yet
        self.player_mark = "X"



class Player2(Actions):
    def __init__(self, player_name):
        self.player_name = player_name   #Haven't used this yet
        self.player_mark = "O"


play1 = Player1(input("Enter your name: "))
play2 = Player2(input("Enter your name: "))




while True:

    # ---- PLAYER 1 ----
    while True:
        try:
            play1.turns()
            print()
            col = int(input("Choose a column from 1 to 7: "))
            if play1.drop_piece_player(col):
                break
        except ValueError:
            print("Invalid input. Try again.")

    play1.get_grid()
    print()

    if play1.victory():
        break
    if all(MAP[0][c] != '.' for c in range(7)):
        print("Draw!")
        break


    # ---- PLAYER 2 ----


    while True:
        try:
            play2.turns()
            print()
            col = int(input("Choose a column from 1 to 7: "))
            if play2.drop_piece_player(col):
                break
        except ValueError:
            print("Invalid input. Try again.")

    play2.get_grid()
    print()

    if play2.victory():
        break
    if all(MAP[0][c] != '.' for c in range(7)):
        print("Draw!")
        break


