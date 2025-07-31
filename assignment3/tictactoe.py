# Task 6: More on Classes
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

    def __str__(self):
        return f"{self.board_array[0][0]}|{self.board_array[0][1]}|{self.board_array[0][2]}\n------\n{self.board_array[1][0]}|{self.board_array[1][1]}|{self.board_array[1][2]}\n------\n{self.board_array[2][0]}|{self.board_array[2][1]}|{self.board_array[2][2]}"

    def move(self, move_string):
        if not move_string in self.valid_moves:
            raise TictactoeException("That's not a valid move.")
        
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3  # row
        column = move_index % 3  # column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")
        win = False
        for i in range(3):  # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
        if not win:
            for i in range(3):  # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] and self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
        if not win:
            if self.board_array[1][1] != " ":  # check diagonals
                if self.board_array[0][0] ==  self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                    win = True
                if self.board_array[0][2] ==  self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                    win = True
        if not win:
            if self.turn == "X": 
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")


# Create game board instance
board = Board()

# Continually prompt until break is hit
while True:
    # Check for True value in tuple, indicating a win or cat game
    next = board.whats_next()

    # If game over print the result and stop the game
    if next[0]:
        print(f"{next[1]}")
        break
    # If game continues, tell which turn it is and prompt for move
    else:
        move = input(f"{next[1]} What's your move: ")

    # Attempt the given move
    try:
        board.move(move)
    except TictactoeException as e:
        print(e.message)

    # Print current board state
    print(board)
