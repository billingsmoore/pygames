#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random

pygame.init()
width = 600
height = 400
snake_block = 10
dis = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game by Jake")
pygame.display.update()
red = (255,100,0)
black = (0,0,0)
blue = (0,0, 255)
grey = (230,230,230)
white = (255,255,255)
dis.fill(grey)
game_over = False
x = 300
y = 200
x_change = 0
y_change = 0
clock = pygame.time.Clock()
game_close = False
font_style = pygame.font.SysFont("freesans", 25)
lost_img = font_style.render("You Lost! Press P-Play Again or Q-Quit", True, white)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, (x[0], x[1], snake_block, snake_block))

def thescore(score):
    value = font_style.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0,0])
        
def game_loop():
    game_over = False
    game_close = False
    frame_rate = 30
    x = int(width / 2)
    y = int(height / 2)
    x_change = 0
    y_change = 0
    speed = 5
    foodx = snake_block * random.randint(0, (width / snake_block - 1))
    foody = snake_block * random.randint(0, (height / snake_block - 1))
    snake_list = []
    length_of_snake = 1
    while(game_over == False):
        while(game_close == True):
            dis.fill(red)
            dis.blit(lost_img, [100,100])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -10
                
                if event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 10
                
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        dis.fill(grey)
        #pygame.draw.rect(dis, blue, (x, y, 10, 10))
        pygame.draw.rect(dis, red, (foodx, foody, snake_block, snake_block))
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True
        our_snake(snake_block, snake_list)
        if x == foodx and y == foody:
            length_of_snake += 1
            speed += 1
            foodx = snake_block * random.randint(0, (width / snake_block - 1))
            foody = snake_block * random.randint(0, (height / snake_block - 1))
        thescore((length_of_snake - 1) * 10)
        pygame.display.update()
        clock.tick(frame_rate)
    
    pygame.quit()
game_loop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




