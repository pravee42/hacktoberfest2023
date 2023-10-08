import pygame
pygame.init()

color=(115,115,10)
#creating game window
window_length=900;
window_bredth=600;

gamewindow=pygame.display.set_mode((window_length,window_bredth))
pygame.display.set_caption("My First Game")
pygame.display.update()

exit_game=False
game_over=False

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
    gamewindow.fill(color)
    # pygame.draw.rect(gamewindow,red,[100,100,10,10])
    pygame.display.update()

#to quit the game window
pygame.quit()
quit()