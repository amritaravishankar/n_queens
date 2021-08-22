"""
    @Author: Amrita Ravishankar
    @Publication-Date: 20/8/21
    @Description:
    A visualiser tool to solve the famous Backtracking problem of N-Queens. 
    The problem requires n non-attacking queens to be placed on a n x n chessboard
    for which solutions exist for all natural numbers other than n=2 and n=3.
    
    The algorithm implements the backtracking approach.
"""
import pygame


# get user input for n
def get_input():
    n = int(input("Enter the desired n (n must be a natural number and not be equal to 2 or 3): "))
    if n == 2 or n == 3:
        print("Invalid input. n must not be 2 or 3")
        exit()
    return n


# create the board
def create_board(n):
    board = []

    for i in range(n):
        row = [0] * n
        board.append(row)

    return board


# if queen exists on board position, board value = 1 else value = 0
def solve_n_queens(board):

    if not problem_util(board, 0):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True


# check if queen can be placed in the position
def is_safe(board, row, col):
    n = len(board)
    clock = pygame.time.Clock()

    # check the row on left side
    for i in range(col):
        if board[row][i] == 1:
            for j in range(col):
                if board[row][j] == 2:
                    board[row][j] = 0
            return False
        board[row][i] = 2
        draw(board, n)
        clock.tick(2)

    # check for queens in upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[x][y] == 2:
                    board[x][y] = 0
            return False
        board[i][j] = 2
        draw(board, n)
        clock.tick(2)

    # check for queens in lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[x][y] == 2:
                    board[x][y] = 0
            return False
        board[i][j] = 2
        draw(board, n)
        clock.tick(2)

    return True


def problem_util(board, col):
    n = len(board)
    clock = pygame.time.Clock() # to delay display

    # if all queens are placed
    if col >= n:
        return True

    # for given column, try placing queens in each row
    for i in range(n):
        if is_safe(board, i, col):
            # place the queen on board[i][col] if it is safe to place it
            board[i][col] = 1

            draw(board, n)
            clock.tick(2)

            # recursively place the rest of the queens
            if problem_util(board, col + 1):
                return True

            # if placing the queen at board[i][col] does not provide a solution, remove it
            board[i][col] = 0

            draw(board, n)
            clock.tick(2)

    # if the queen cannot be placed in any row in this column
    return False


def draw(board, n):
    win = pygame.display.set_mode((800, 800))
    size = 800 // n
    queen_image = pygame.transform.scale(pygame.image.load('queen.jpg'), (size, size))

    # fill the window white
    win.fill((255, 255, 255))

    for i in range(n):
        for j in range(n):
            if board[j][i] == 0:
                pygame.draw.rect(win, (255, 255, 255), [i*size, j*size, size, size])
                pygame.display.update()

            elif board[j][i] == 1:
                pygame.draw.rect(win, (0, 0, 0), [i*size, j*size, size, size])
                win.blit(queen_image,(i*size,j*size))
                pygame.display.update()

            elif board[j][i] == 2:
                pygame.draw.rect(win, (255, 0, 0), [i*size, j*size, size, size])
                pygame.display.update()


# Print the solution and draw it on the board
def print_solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0
            print(board[i][j], end="  ")
        print()

    draw(board, n)


# main function
def main():
    pygame.init()
    n = get_input()
    board = create_board(n)
    solve_n_queens(board)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve_n_queens(board)


main()
