from sys import exit
import pygame


def main_setup(Main_x,Main_y,Main_name,):
    pygame.init() #Very Important to set pygame to initial
    
    screen = pygame.display.set_mode((Main_x,Main_y)) # setup display surface with tuple numbers
    pygame.display.set_caption(Main_name) # set title of window


    
    while True: #while loop to open game windows dispaly
        for event in pygame.event.get(): #pygame event funciton
            if event.type == pygame.QUIT:
                pygame.quit() #pygame quit
                exit()     #windows close to exit pygame program



    pygame.display.update()
    clock.tick(60)  #set max frame rate
    
