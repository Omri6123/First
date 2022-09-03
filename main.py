from cProfile import run
from cmath import rect
import os
from pickle import FALSE
from re import X
from tkinter import font
from turtle import Screen, speed
import pygame, sys, random

pygame.init()

#Game Physics
FPS = 60
player_speed = 6
enemy_speed = 5.5
ball_speed_X = 7
ball_speed_Y = 7
Round_Num = 1
score_time = True
text_font = pygame.font.SysFont('Arial', 24, False, False)

#Game Settings
Game_Delay_Time = 4000

player_score = 0
enemy_score = 2

width = 1000
height = 600

grey_line = (77, 77, 77)
background = (0, 0, 0)
players_color = (255, 255, 255)
ball_color = (0, 157, 196)

startX = width / 2; endX = width / 2 # draw board
startY = 0; endY = height

win = pygame.display.set_mode((width , height))

pygame.display.set_caption("Game")


player = pygame.Rect(width - 20, height / 2 - 70, 5, 100)
enemy = pygame.Rect(10, height / 2 - 70, 5, 100)
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)


#Function that byilds the Game Board
def Set_Window(): 
    win.fill(background) 
    pygame.draw.line(win, grey_line, (startX , startY), (endX , endY))
    pygame.draw.rect(win, players_color, player)
    pygame.draw.rect(win, players_color, enemy)
    pygame.draw.ellipse(win, ball_color, ball)
    pygame.display.update()

#Display a 4 sec timer
def Round_Start():
    font_size = 40
    font = pygame.font.SysFont('Arial', font_size, False, False)
    seconds = float((Game_Delay_Time - pygame.time.get_ticks()) / 1000)

    if seconds >= 0:
       time_left = "Round " + str(Round_Num) + " starts in " + str(seconds)
       text = font.render(time_left, True, (255, 255, 255))
       win.blit(text, (width / 2 - 150, height / 13))
       pygame.display.update()


#Displays the score
def Display_Score():
    global player_score, enemy_score, IsWinner, Round_Num
     
    if player_score > 2 or enemy_score > 2:
        IsWinner = True

    Enemy = text_font.render(str(enemy_score), True, (240,248,255))
    Player = text_font.render(str(player_score), True, (240,248,255))
    Round = text_font.render("Round: " + str(Round_Num), True, (240,248,255))

    win.blit(Enemy, (width / 2 - 30 , height / 2 - 40))
    win.blit(Player, (width / 2 + 20 , height / 2 - 40))
    win.blit(Round, (5, 0))

    pygame.display.update()

    
def Round_Reset():
    global Round_Num, ball_speed_Y, ball_speed_X, score_time, player, enemy
    current_time = pygame.time.get_ticks()
    ball.center = (width / 2, height / 2)

    if current_time - score_time < 700:
        text = text_font.render("3", True, (255, 255, 255))
        win.blit(text, (width / 2 - 6 , height / 2 + 20))

    elif 700 < current_time - score_time < 1400:
        text = text_font.render("2", True, (255, 255, 255))
        win.blit(text, (width / 2 - 6 , height / 2 + 20))

    else:
        text = text_font.render("1", True, (255, 255, 255))
        win.blit(text, (width / 2 - 6, height / 2 + 20))

    player.top = height / 2 - 70
    enemy.top = height / 2 - 70
    
        
    pygame.display.update()

    

    if current_time - score_time < 2100:
        ball_speed_X, ball_speed_Y = 0,0

    else:
      ball_speed_Y = 7 * random.choice((1, -1))
      ball_speed_X = 7 * random.choice((1, -1))
      score_time = None
    
    
def Enemy_Ai():

    if enemy.top < ball.y:
        enemy.top += enemy_speed

    elif enemy.bottom  > ball.y:
        enemy.bottom -= enemy_speed 

    if (enemy.top <= 5):
        enemy.top = 5
    
    elif (enemy.bottom >= height - 5):
        enemy.bottom = height - 5


def Ball_Movement():
    global ball_speed_X, ball_speed_Y, player_score, enemy_score, score_time, Round_Num
    ball.x += ball_speed_X
    ball.y += ball_speed_Y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_Y *= -1

    if ball.left <= 0:
        player_score += 1; Round_Num += 1
        score_time = pygame.time.get_ticks()
        Round_Reset()

    if ball.right >= width:
        enemy_score += 1; Round_Num += 1
        score_time = pygame.time.get_ticks()
        Round_Reset()

    if ball.colliderect(player) or ball.colliderect(enemy):
        ball_speed_Y += 0.6
        ball_speed_X *= -1

#Player Movement
def Player_Movement(keys_pressed, player):

    if keys_pressed[pygame.K_UP]:
        player.y -= player_speed

    elif keys_pressed[pygame.K_DOWN]:
        player.y += player_speed
    
    if (player.top <= 5):
        player.top = 5
    
    elif (player.bottom >= height - 5):
        player.bottom = height - 5

def Game():
    Display_Score()

    if score_time:
        Round_Reset()

    else:
        Ball_Movement()
        keys_pressed = pygame.key.get_pressed()

        Player_Movement(keys_pressed, player)
        Enemy_Ai()

def Winner_Celebration():
    global player_score, enemy_score, IsWinner, Run
    
    if player_score > enemy_score:
        text = text_font.render("Congratulation, you have won", True, (255, 255, 255))
        win.blit(text, (width / 3 + 20, 40))
    
    else:
        text = text_font.render("Congratulation, you suck", True, (255, 255, 255))
        win.blit(text, (width / 3 + 20, 40))

    retry = text_font.render("press Enter to Play Again", True, (255, 255, 255))
    win.blit(retry, (width / 3 + 30, 20))
            
IsWinner = False
Run = True

#Game loop
while Run:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()


    if IsWinner:
        Winner_Celebration()
       

    else:
        Set_Window()
        Game()
