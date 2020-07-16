#######################################
# code Assingment I
# student ID : 6201012630100
#######################################

import pygame
from random import * 

#ขนาดของหน้าต่าง
width = 800
height = 600

# เฟรมเรท
fps = 15

# จำนวนรูป
Numball = 10

# เก็บค่าตำแหน่งx,y สีและรัศมีที่สุ่ม
position_x = []
position_y = []
allcolor = []
radius =[]

# setting เริ่มแรก
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ball click")
Bounce = False
clock = pygame.time.Clock()

# สร้างรูปวงกลมแบบสุ่ม
for i in range(Numball):

    r = randint(10,20)
    alpha = randint(50,255)
    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255)
    randomcolor = (R,G,B,alpha)
    x,y = randint(r,width-r), randint(r,height-r)
    
    position_x += [x]
    position_y += [y]
    allcolor += [randomcolor]
    radius += [r]

    #print(position_x)
    #print(position_y)
    #print(allcolor)
    #print(radius)
    

    


running = True

while running:
    # check การกดปิด
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))

    for i in range (Numball):
        pygame.draw.circle(screen,allcolor[i],(position_x[i],position_y[i]),radius[i])
        
    
    if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                (a,b) = pygame.mouse.get_pos()
                
                for num in range(Numball):

                    if (position_x[num]-10) <= a <= (position_x[num]+10) and (position_y[num]-10) <= b <= (position_y[num]+10) :
                        position_x[num],position_y[num] = -20 , -20
    

    clock.tick(fps)
    
    pygame.display.flip()
    

pygame.quit()


# refferance
# https://www.youtube.com/watch?v=A1nm2nl-8ig&t=221s
# https://www.pygame.org/docs/ref/surface.html
# pygame_demo1 