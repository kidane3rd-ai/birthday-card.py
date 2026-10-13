import pygame
import time
pygame.init()
WIDTH=600
HEIGHT=600
display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
img=pygame.image.load("card.jpg")
best=pygame.image.load("choclate.jpg")
delicious=pygame.image.load("cake.jpg")
font=pygame.font.SysFont("Times New Roman",40)
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    display_surface.blit(img,(0,0))        

    text=font.render("I wish you the best",True,"green")
    display_surface.blit(text,(100,300))
    pygame.display.update()

