import single_player
import pygame
import colors
from single_player import size
size = 20
margin = 3
end = False
screen = single_player.screen
player1 = single_player.player.Player(10, 5)
sea1 = player1.sea
computer = single_player.player.Player(10, 5)
sea2 = computer.sea
grid1 = [[0 for i in range(10)] for i in range(10)]
grid2 = [[0 for i in range(10)] for i in range(10)]
def draw_board():
    screen.fill(colors.black)
    for row in range(10):
        for column in range(10):
            pygame.draw.rect(screen,
                             colors.colors[grid1[row][column]],
                             [(margin+size)*column+margin,
                              (margin+size)*row+margin,
                              size,
                              size])
    for row in range(10):
        for column in range(10):
            pygame.draw.rect(screen,
                             colors.colors[grid2[row][column]],
                             [(margin+size)*(column+13)+margin,
                              (margin+size)*row+margin,
                              size,
                              size])
def draw_put_ships_board(width, height):
    color = colors.blue
    draw_board()
    pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen,
                     colors.grey,
                     [pos[0] - size/2,
                     pos[1] - size/2,
                     width*(size+margin),
                     height*(size+margin)])
    pygame.display.flip()
def place_ship(player1):
    ships = [2, 3, 3, 4, 5]
    direction = 0
    while ships != []:
        ship_size = [ships[-1], 1]
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                direction = 1 - direction
            draw_put_ships_board(ship_size[direction], ship_size[1-direction])
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if single_player.put_one_ship(player1, pos, ships[-1], direction, grid1):
                        ships.pop()
def win_window(result):
    dimension = [600, 700]
    screen = pygame.display.set_mode(dimension)
    pygame.display.set_caption("Result")
    if result == player1:
        print("You turned to be victorious in the war!")
        image = pygame.image.load(".\images\you_won.jpg")
        screen.blit(image, (0,0))
        pygame.display.flip()
    else:
        print("sorry better luck next time!")
        image = pygame.image.load(".\images\you_lost.jpg")
        screen.blit(image, (0,0))
        pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
turn = True
place_ship(player1)
single_player.computer_ship(computer)
while True:
    draw_board()
    pygame.display.flip()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    while turn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                turn = single_player.player_make_move(pos, sea2, grid2, grid1)
                draw_board()
                if computer.check_ships():
                    win_window(player1)
    while not turn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            turn = single_player.comp_move(player1, sea1, grid1, grid2)
            draw_board()
            if player1.check_ships():
                win_window(computer)


pygame.quit()
