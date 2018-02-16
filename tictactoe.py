import random
class TicTacToe():
    
    def __init__(self):
        self.over = False
        self.board = [1,2,3,4,5,6,7,8,9]
        print("Welcome to Tic Tac Toe!")
        computer_rand = random.randint(0,10)
        player_rand = random.randint(0,10)
        
        if player_rand >= computer_rand:    
            print("You go first!")
            self.turn = "Player"            
        else:
            print("Computer goes first!")
            self.turn = "Computer"
    
    def get_board(self):
        
        for i in range(3):
            print(self.board[(i*3)], self.board[(i*3)+1], self.board[(i*3)+2])
        
    
    def ask_move(self):
        print("Where do you want to mark the board?.")
        self.get_board()
        try:
            n = int(input("My choice is: "))
        except:
            n = int(input("My choice is: "))
        
        if n not in range(1,10):
            print("A number between 1 and 9 please")
            self.ask_move()
        else:
            self.mark_cell(n, "X")
        
    def mark_cell(self, n, sign):
        
        if type(self.board[n-1]) is int:
            self.board[n-1] = sign
            print()
       
        else:
            print("Hey! That spot is already taken, try something different.")
            self.ask_move()
            
    def computer_choice(self):
        
        free = [c for c in self.board if c!="X" and c!="O"]
        self.mark_cell(random.choice(free),"O")
    
    def check_win(self):
        #solutions
        s1 = [self.board[0], self.board[1], self.board[2]] # - top
        s2 = [self.board[3], self.board[4], self.board[5]] # - middle
        s3 = [self.board[6], self.board[7], self.board[8]] # - bottom
        s4 = [self.board[0], self.board[3], self.board[6]] # | left
        s5 = [self.board[1], self.board[4], self.board[7]] # | middle
        s6 = [self.board[2], self.board[5], self.board[8]] # | right
        s7 = [self.board[0], self.board[4], self.board[8]] # \ 
        s8 = [self.board[2], self.board[4], self.board[6]] # /
        
        lines = [s1, s2, s3, s4, s5, s6, s7, s8]
            
        for s in lines:
            if s[0]== s[1] and s[1]==s[2] and s[2]==s[0]:
                print("GAME OVER!")
                self.get_board()
                self.over = True
                break
            
        if self.turn == "Computer":
            self.turn = "Player"
        else:
            self.turn = "Computer"

T =  TicTacToe()
for i in range(9):
    
    if T.turn == "Player":
        T.ask_move()
        T.check_win()     
    else:
        T.computer_choice()
        T.check_win()
    
    if T.over:
            break
if not T.over:
    print("GAME OVER! No winner this time")