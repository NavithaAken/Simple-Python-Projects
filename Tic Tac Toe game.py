import tkinter as tk

class UltimateTicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Ultimate Tic Tac Toe")
        self.current_player = 'X'
        self.small_boards = [[' ']*3 for _ in range(9)]
        self.large_board = [' ']*9

        self.buttons = []
        for i in range(9):
            row = []
            for j in range(9):
                btn = tk.Button(master, text=' ', width=4, height=2, font=('Arial', 24), command=lambda i=i, j=j: self.click(i, j))
                btn.grid(row=i//3*3 + j//3, column=i%3*3 + j%3)
                row.append(btn)
            self.buttons.append(row)

        self.status_label = tk.Label(master, text='Player X\'s turn', font=('Arial', 16))
        self.status_label.grid(row=9, columnspan=3)

    def click(self, row, col):
        if self.large_board[row // 3 * 3 + col // 3] != ' ' or self.small_boards[row][col] != ' ':
            return

        self.small_boards[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)

        if self.check_small_board_win(row // 3 * 3 + col // 3):
            self.large_board[row // 3 * 3 + col // 3] = self.current_player
            self.update_large_board_button(row // 3 * 3 + col // 3)

        if self.check_large_board_win():
            self.status_label.config(text=f'Player {self.current_player} wins!')
            for row in self.buttons:
                for btn in row:
                    btn.config(state=tk.DISABLED)
        elif ' ' not in [cell for board in self.small_boards for cell in board]:
            self.status_label.config(text='It\'s a draw!')
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.status_label.config(text=f'Player {self.current_player}\'s turn')

    def check_small_board_win(self, board_idx):
        board = self.small_boards[board_idx]
        for row in board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                return True
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return True
        return False

    def check_large_board_win(self):
        for row in range(3):
            if self.large_board[row * 3] == self.large_board[row * 3 + 1] == self.large_board[row * 3 + 2] != ' ':
                return True
            if self.large_board[row] == self.large_board[row + 3] == self.large_board[row + 6] != ' ':
                return True
        if self.large_board[0] == self.large_board[4] == self.large_board[8] != ' ':
            return True
        if self.large_board[2] == self.large_board[4] == self.large_board[6] != ' ':
            return True
        return False

    def update_large_board_button(self, board_idx):
        for i in range(3):
            for j in range(3):
                self.buttons[board_idx // 3 * 3 + i][board_idx % 3 * 3 + j].config(state=tk.DISABLED)

root = tk.Tk()
game = UltimateTicTacToe(root)
root.mainloop()
