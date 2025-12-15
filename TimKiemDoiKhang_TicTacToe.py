import tkinter as tk
import math

# game constants
EMPTY = 0
HUMAN = 1
AI = -1


class TicTacToe:
    def __init__(self, n):
        self.n = n #nxn
        self.board = [[EMPTY for _ in range(n)] for _ in range(n)]
        self.current_player = HUMAN #nguoi first
    #selcet or remove nuoc di
    def make_move(self, r, c, player):
        self.board[r][c] = player

    def undo_move(self, r, c):
        self.board[r][c] = EMPTY
    #board full yes or no
    def is_full(self):
        for row in self.board:
            if EMPTY in row:
                return False
        return True

    def check_winner(self):
        n = self.n

        # rows
        for i in range(n):
            s = sum(self.board[i])
            if s == n:
                return HUMAN
            if s == -n:
                return AI

        # columns
        for j in range(n):
            s = sum(self.board[i][j] for i in range(n))
            if s == n:
                return HUMAN
            if s == -n:
                return AI

        # duong cheo chinh
        s = sum(self.board[i][i] for i in range(n))
        if s == n:
            return HUMAN
        if s == -n:
            return AI

        # duong cheo phu
        s = sum(self.board[i][n - i - 1] for i in range(n))
        if s == n:
            return HUMAN
        if s == -n:
            return AI

        return None

    def available_moves(self):
        moves = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == EMPTY:
                    moves.append((i, j))
        return moves


def minimax(game, depth, maximizing):
    winner = game.check_winner()
    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if game.is_full() or depth == 0:
        return 0
    #AI (MAX)
    if maximizing:
        best = -math.inf
        #check all nuoc di
        for r, c in game.available_moves():
            game.make_move(r, c, AI) #AI danh (r,c)
            val = minimax(game, depth - 1, False) #giam depth, toi luot human
            game.undo_move(r, c)#return board ve vi tri cu
            best = max(best, val) #chon nuoc di tot nhat trong (-1,1,0)
        return best
    else:
        best = math.inf
        for r, c in game.available_moves():
            game.make_move(r, c, HUMAN)
            val = minimax(game, depth - 1, True)
            game.undo_move(r, c)
            best = min(best, val)
        return best


def alphabeta(game, depth, alpha, beta, maximizing):
    winner = game.check_winner()
    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if game.is_full() or depth == 0:
        return 0

    if maximizing:
        value = -math.inf
        for r, c in game.available_moves():
            game.make_move(r, c, AI)
            value = max(value, alphabeta(game, depth - 1, alpha, beta, False))
            game.undo_move(r, c)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        for r, c in game.available_moves():
            game.make_move(r, c, HUMAN)
            value = min(value, alphabeta(game, depth - 1, alpha, beta, True))
            game.undo_move(r, c)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


class TicTacToeGUI:
    def __init__(self, root, n, use_alpha_beta=True):
        self.game = TicTacToe(n)
        self.n = n
        self.use_alpha_beta = use_alpha_beta

        self.buttons = []
        for i in range(n):
            row = []
            for j in range(n):
                btn = tk.Button(
                    root,
                    text=" ",
                    width=4,
                    height=2,
                    font=("Arial", 40),
                    command=lambda r=i, c=j: self.human_move(r, c) #khi bam ,goi human
                )
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

        self.info = tk.Label(root, text="your turn")
        self.info.grid(row=n, column=0, columnspan=n)

    def human_move(self, r, c):
        if self.game.board[r][c] != EMPTY: #o da chon thi ko cho chon
            return

        self.game.make_move(r, c, HUMAN)
        self.buttons[r][c].config(text="X", state="disabled")

        if self.check_end():
            return

        self.info.config(text="ai thinking...")
        self.ai_move()

    def ai_move(self):
        best_val = -math.inf
        best_move = None
        #borad > 3 thi depth=9
        depth = 9 if self.n <= 3 else 3

        for r, c in self.game.available_moves():
            self.game.make_move(r, c, AI)
            #so sanh
            if self.use_alpha_beta:
                val = alphabeta(self.game, depth, -math.inf, math.inf, False)
            else:
                val = minimax(self.game, depth, False)
            self.game.undo_move(r, c)

            if val > best_val:
                best_val = val
                best_move = (r, c)

        if best_move:
            r, c = best_move
            self.game.make_move(r, c, AI)
            self.buttons[r][c].config(text="O", state="disabled")

        self.check_end()

    def check_end(self):
        winner = self.game.check_winner()
        if winner == HUMAN:
            self.info.config(text="END: human wins")
            self.disable_all()
            return True
        if winner == AI:
            self.info.config(text="END: ai wins")
            self.disable_all()
            return True
        if self.game.is_full():
            self.info.config(text="END: draw")
            return True

        self.info.config(text="your turn")
        return False

    def disable_all(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")


def main():
    n = int(input("nhap kich thuoc ban co: "))
    algo = input("chon thuat toan (1=minimax, 2=alpha-beta): ")

    root = tk.Tk()
    root.title("tictactoe vs ai")

    use_alpha_beta = (algo == "2")
    TicTacToeGUI(root, n, use_alpha_beta)

    root.mainloop()


if __name__ == "__main__":
    main()

