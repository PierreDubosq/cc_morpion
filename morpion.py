import pygame
import math

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_board(screen, bg):
    circle = pygame.image.load("./images/circle.jpg")
    cross = pygame.image.load("./images/cross.jpg")
    for i in range(len(board)):
        print(board[i])
    print("\n")
    screen.blit(bg, (0, 0))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'x':
                screen.blit(cross, (j * 100, i * 100))
            if board[i][j] == 'o':
                screen.blit(circle, (j * 100, i * 100))
    pygame.display.flip()

def is_win(c):
    for i in range(len(board)):
        if board[i][0] == c and board[i][1] == c and board[i][2] == c:
            return (True)
        if board[0][i] == c and board[1][i] == c and board[2][i] == c:
            return (True)
    if board[0][0] == c and board[1][1] == c and board[2][2] == c:
        return (True)
    if board[0][2] == c and board[1][1] == c and board[2][0] == c:
        return (True)
    return (False)

def game(screen, bg):
    player = 0
    played = False
    while (1):
        pos = [-1, -1]
        print_board(screen, bg)
        while not played:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        pos = pygame.mouse.get_pos()
                        pos = [math.floor(pos[1] / 100), math.floor(pos[0] / 100)]
                        if board[pos[0]][pos[1]] == ' ':
                            played = True
        if player:
            board[pos[0]][pos[1]] = 'x'
            player = 0
            if is_win('x'):
                print_board(screen, bg)
                print("Player " + str(player + 1) + " won !")
                return
        else:
            board[pos[0]][pos[1]] = 'o'
            player = 1
            if is_win('o'):
                print_board(screen, bg)
                print("Player " + str(player + 1) + " won !")
                return
        if board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ':
            print("Equality !")
            return
        played = False
        print_board(screen, bg)

screen = pygame.display.set_mode((300, 300))
bg = pygame.image.load("./images/background.jpg")
game(screen, bg)
pygame.quit()