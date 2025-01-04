from player import RandomComputerPlayer , HumanPlayer
import time


class TicTacToe:
    def __init__(self):
        # we will use a single list to rep 3x3 board        
        self.board = [' ' for _ in range(9)] 
        self.current_winner = None # keep track of winner

    def print_board(self):
        #this is just getting the rows
        for row in [self.board[i*3 :(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number correspods to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        #This is list comprehension method
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for(i,spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0,'x'), (1,'x') , (2,'o')]
        #     if spot == ' ':
        #         moves.append(i)
        #     return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move, then make the move (assign square to letter)
        # then return True if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square , letter):
                self.current_winner = letter
            return True
        return False

    def winner(self , square , letter):
        # winner if 3 in a row anywhere we have to check all of these!!
        # first lets check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        # but only if the square is an even number (0,2,4,6,8)
        # but these are the only moves possible to win a diagonal
        if square % 2 == 0:
            #left to right diagonal
            diagonal1 = [self.board[i] for i in [0,4,8]] 
            if all([spot == letter for spot in diagonal1]):
                return True             
            #right to left digonal
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if all checks fail
        return False


def play(game, x_player , o_player , print_game = True):
    # returns the winner of the game(the letter) or None for a tie
    if print_game:
        game.print_board_nums()
    #Staring letter
    #Iterate while the game still has empty squares
    # (We don't have to worry about winner because we will just return that which breaks loop)
    letter = 'X'

    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Define a function to make moves
        if game.make_move(square , letter):
            if print_game:
                print(letter + f' makes move to square {square}')
                game.print_board()
                print('') # just empty line

            if game.current_winner:
                if print_game:
                   print(letter + ' wins..!! \n') 
                return letter


            #after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
            # if letter == 'X':
            #     letter = 'o'
            # else:
            #     letter = 'X'
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t , x_player , o_player , print_game=True)