import pygame

window = pygame.display.set_mode(
(1000,650))

bg = pygame.transform.scale( pygame.image.load("background.png"),(1000,650))

clock = pygame.time.Clock()
sprite1 = pygame.transform.scale( pygame.image.load("sprite1.png"),(120,110))
sprite2 = pygame.transform.scale( pygame.image.load("sprite2.png"),(120,110))

sprite1_rect = pygame.Rect(10,10,120,110)
sprite2_rect = pygame.Rect(500,500,120,110)

x1,y1 = 10,10

x2,y2 = 500,500


game = True
while game:
    for evnt in pygame.event.get():
        if evnt.type ==pygame.QUIT:
            game = False
    window.blit(bg,(0,0))

    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))

    pygame.draw.rect(window,(255,0,0),sprite1_rect,2)
    pygame.draw.rect(window,(0,0,250),sprite2_rect,2)
    sprite1_rect.x = x1
    sprite1_rect.y = y1
    
    sprite2_rect.x = x2
    sprite2_rect.y = y2

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x1-=5

    if keys[pygame.K_d]:
        x1+=5
    if keys[pygame.K_w]:
        y1-=5

    if keys[pygame.K_s]:
        y1+=5
#-----------------------
    if keys[pygame.K_RIGHT]:
        x2-=5

    if keys[pygame.K_LEFT]:
        x2+=5
    if keys[pygame.K_UP]:
        y2-=5

    if keys[pygame.K_DOWN]:
        y2+=5

    pygame.display.update()

    clock.tick(60)