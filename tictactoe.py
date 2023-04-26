import random

"""

"""

class TicTacToe:
    
    def __init__(self):

        #board will be 3x3 matrix
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]

        #X will start
        self.turn = "X"

        #server will be X
        self.you = "X"

        #client will be O
        self.opponenet = "O"

        #check who is the winner
        self.winner = None

        #check if game is over
        self.game_over = False

        #check how many moves have been played.
        #if all 9 moves have been played there are no more moves and it's a tie.
        self.counter = 0

        self.handle_connection()

    #function that handles game play
    def handle_connection(self):

        #as long as game is not over a player can make a move
        while not self.game_over:

            #if it's your turn you can make a move
            #else, wait for opponnent (computer) to make a move
            if self.turn == self.you:
                move = input("Enter a move (row, column):")
                if self.check_valid_move(move.split(",")):
                    self.apply_move(move.split(","), self.you)
                    self.turn = self.opponenet
                else:
                    print("Invalid move, spot on baord already taken")
            else:
                move = [random.randint(0,2), random.randint(0,2)]
                if self.check_valid_move(move):
                    self.apply_move(move, self.opponenet)
                    self.turn = self.you

        #if game is over end the program
        quit()

    #execute a player's move
    #note: the move argument is transformed into a list[] via move.split(",")
    def apply_move(self, move, player):

        if self.game_over:
            return
        
        #increase counter by 1 to track how many moves have been made
        self.counter += 1

        #put player's move at indicated spot on board and display board
        self.board[int(move[0])][int(move[1])] = player
        self.print_board()

        #check if there's a winner or if it's a tie
        if self.check_if_won():
            if self.winner == self.you:
                print("You win")
                exit()
            elif self.winner == self.opponenet:
                print("You lose")
                exit()
        else:
            if self.counter == 9:
                print("It is a tie")
                exit()
                
    #check if move is valid
    #note: move argument tranformed into list[] via move.split(",")
    def check_valid_move(self, move):
        
        try:
            int(move[0])
            return self.board[int(move[0])][int(move[1])] == " "
        except ValueError:
            print("Input needs to be two integers 0-2 in the format of: row, column")
        except IndexError:
            print("Input needs to be two integers 0-2 in the format of: row, column")

    """
    #check if move is valid
    #note: move argument tranformed into list[] via move.split(",")
    def check_valid_move(self, move):
        if (move[0] and move[1]) and self.board[int(move[0])][int(move[1])] == " ":
            return self.board[int(move[0])][int(move[1])] == " "
        else:
            self.handle_connection()
        #return self.board[int(move[0])][int(move[1])] == " "
    """
    
    #check for a winner
    def check_if_won(self):

        #check for a winning row
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winner = self.board[row][0]
                self.game_over = True
                return True
            
        #check for a winning column
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.winner = self.board[0][col]
                self.game_over = True
                return True
        
        #check for the first diagnal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner = self.board[0][0]
            self.game_over = True
            return True

        #check for the second diagnal    
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.winner = self.board[0][2]
            self.game_over = True
            return True

        #if no winners, return False  
        return False
    
    #display board in the console
    def print_board(self):
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("--------------")
            if row == 2:
                print("\n\n_____________\n\n")

game = TicTacToe()
#game.host_game("localhost", 9999)
