import pygame
import random
pygame.init()

#importing music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

#creating game window
window_length=300;
window_bredth=700;

#creating colors
color=(139,131,25)
red=(255,0,0)
black=(0,0,0)

#variables of objects
score=10
car_x=150
car_y=650
vel=12
car_velocity_x=0
car_velocity_y=0

ob_x_1=random.randint(0,275)
ob_y_1=50

ob_x_2=random.randint(0,275)
ob_y_2=250

ob_x_3=random.randint(0,275)
ob_y_3=450



ob_velocity_y=10

#frame per second
fps=20

#gamewindow creation
gamewindow=pygame.display.set_mode((window_length,window_bredth))
pygame.display.set_caption("Car Crash")
pygame.display.update()

#setting game variables

exit_game=False
game_over=False

#clock for game
clock=pygame.time.Clock()

#creating a gameloop

while not exit_game:
    
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            exit_game=True
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                car_velocity_y=0
                car_velocity_x=-vel
            if event.key==pygame.K_RIGHT:
                car_velocity_y=0
                car_velocity_x=vel
            if event.key==pygame.K_UP:
                car_velocity_x=0
                car_velocity_y=-vel
            if event.key==pygame.K_DOWN:
                car_velocity_x=0
                car_velocity_y=vel

    #to increase speed after a particular score
    if score>300:
        ob_velocity_y=8+score//100
        vel=10+score//100



    car_x+=car_velocity_x
    car_y+=car_velocity_y
    ob_y_1+=ob_velocity_y
    ob_y_2+=ob_velocity_y
    ob_y_3+=ob_velocity_y

    #reiteration of object
    if (ob_y_1>670):
        ob_x_1=random.randint(0,275)
        ob_y_1=50
        score+=10
    if (ob_y_2>670):
        ob_x_2=random.randint(0,275)
        ob_y_2=50
        score+=10
    if (ob_y_3>670):
        ob_x_3=random.randint(0,275)
        ob_y_3=50
        score+=10
        
    



#TO ADD BOUNDARY EFFECT TO GAME
    if car_x<0:
        car_x=0
    if car_y<0:
        car_y=0
    if car_x>window_length-25:
        car_x=window_length-25
    if car_y>window_bredth-40:
        car_y=window_bredth-40
    
    #game over condition

    if abs((car_y-ob_y_1<20) and (car_y-ob_y_1>-20)):
        if (abs(car_x-ob_x_1<20) and abs(car_x-ob_x_1>-20)):
            exit_game=True
    if abs((car_y-ob_y_2<20) and (car_y-ob_y_2>-20)):
        if (abs(car_x-ob_x_2<20) and abs(car_x-ob_x_2>-20)):
            exit_game=True
    if abs((car_y-ob_y_3<20) and (car_y-ob_y_3>-20)):
        if (abs(car_x-ob_x_3<20) and abs(car_x-ob_x_3>-20)):
            exit_game=True

    gamewindow.fill(color)
    pygame.draw.rect(gamewindow,black,[car_x,car_y,35,40])
    pygame.draw.rect(gamewindow,red,[ob_x_1,ob_y_1,40,30])
    pygame.draw.rect(gamewindow,red,[ob_x_2,ob_y_2,40,30])
    pygame.draw.rect(gamewindow,red,[ob_x_3,ob_y_3,40,30])
    pygame.display.update()
    clock.tick(fps)

#to quit the game window
pygame.mixer.music.stop()
print("Your score is:",score)
pygame.quit()
quit()



