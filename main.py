import random

# 初始化一个空的9x9数独盘
board = [[0]*9 for _ in range(9)]

def is_valid(board, row, col, num):
    # 检查行是否有重复
    for x in range(9):
        if board[row][x] == num:
            return False
    # 检查列是否有重复
    for x in range(9):
        if board[x][col] == num:
            return False
    # 检查3*3方块是否有重复
    start_row, start_col = row - row%3, col - col%3
    for i in range(3):
        for j in range(3):
            if board[i+start_row][j+start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()

# 首先，我们生成一个完整的数独解答
solve_sudoku(board)

# 然后，我们随机去掉一些数字来生成题目
# Easy: 30
# Medium: 70
# Challenging: 100
# Difficult: 150
# 🤔: 300
for _ in range(70):
    i, j = random.randint(0, 8), random.randint(0, 8)
    board[i][j] = 0

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            print('_', end=' ')
        else:
            print(int(board[i][j]), end=' ')
        if (j + 1) % 3 == 0 and j < 8:
            print('|', end=' ')
    print()
    if (i + 1) % 3 == 0 and i < 8:
        print('-'*21)
