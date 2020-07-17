###############################
# code Assingment II
# student ID : 6201012630100
###############################


import pygame
from random import * 

# ขนาด
width = 800
height = 600

# เฟรมเรท
fps = 60

# จำนวนรูป
Numball = 10

# บันทึกค่าตำแหน่ง
position_x = []
position_y = []
allcolor = []
radius =[]
spd_x = []
spd_y = []

# setting เริ่มต้น

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bounce test")
Bounce = False
clock = pygame.time.Clock()

# สุ่มค่าตัวเลขในการทำรูป

for i in range(Numball):

    r = randint(10,20)
    alpha = randint(50,255)
    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255)
    randomcolor = (R,G,B,alpha)
    x,y = randint(r,width-r), randint(r,height-r)
    ranx = 2
    rany = 2

    position_x += [x]
    position_y += [y]
    spd_x += [ranx]
    spd_y += [rany]
    allcolor += [randomcolor]
    radius += [r]

    #print(position_x)
    #print(position_y)
    #print(spd_x)
    #print(spd_y)
    #print(allcolor)
    #print(radius)


# run โปรแกรม

while Bounce == False:

    # check การปิด

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Bounce = True
    
    screen.fill((0,0,0))

    # สร้างรูป

    for i in range (Numball):
        pygame.draw.circle(screen,allcolor[i],(position_x[i],position_y[i]),radius[i])
        position_x[i] += spd_x[i]
        position_y[i] += spd_y[i]

    # กำหนดสะท้อนกับขอบหน้าต่าง

    for po in range (Numball):
        if position_y[po] > 580 or position_y[po] < 20:
            spd_y[po] = spd_y[po] * -1
        if position_x[po] > 780 or position_x[po] < 20:
            spd_x[po] = spd_x[po] * -1
        
    # กำหนดสะท้อนกับรูปวงกลมด้วยกัน

    # 0
    if abs(position_x[0] - position_x[1]) < 12:
        spd_x[0] *= -1
        spd_x[1] *= -1
    if abs(position_y[0] - position_y[1]) < 12:
        spd_y[0] *= -1
        spd_y[1] *= -1

    if abs(position_x[0] - position_x[2]) < 12:
        spd_x[0] *= -1
        spd_x[2] *= -1
    if abs(position_y[0] - position_y[2]) < 10:
        spd_y[0] *= -1
        spd_y[2] *= -1

    if abs(position_x[0] - position_x[3]) < 10:
        spd_x[0] *= -1
        spd_x[3] *= -1
    if abs(position_y[0] - position_y[3]) < 10:
        spd_y[0] *= -1
        spd_y[3] *= -1

    if abs(position_x[0] - position_x[4]) < 10:
        spd_x[0] *= -1
        spd_x[4] *= -1
    if abs(position_y[0] - position_y[4]) < 10:
        spd_y[0] *= -1
        spd_y[4] *= -1

    if abs(position_x[0] - position_x[5]) < 10:
        spd_x[0] *= -1
        spd_x[5] *= -1
    if abs(position_y[0] - position_y[5]) < 10:
        spd_y[0] *= -1
        spd_y[5] *= -1

    if abs(position_x[0] - position_x[6]) < 10:
        spd_x[0] *= -1
        spd_x[6] *= -1
    if abs(position_y[0] - position_y[6]) < 10:
        spd_y[0] *= -1
        spd_y[6] *= -1

    if abs(position_x[0] - position_x[7]) < 10:
        spd_x[0] *= -1
        spd_x[7] *= -1
    if abs(position_y[0] - position_y[7]) < 10:
        spd_y[0] *= -1
        spd_y[7] *= -1

    if abs(position_x[0] - position_x[8]) < 10:
        spd_x[0] *= -1
        spd_x[8] *= -1
    if abs(position_y[0] - position_y[8]) < 10:
        spd_y[0] *= -1
        spd_y[8] *= -1

    if abs(position_x[0] - position_x[9]) < 10:
        spd_x[0] *= -1
        spd_x[9] *= -1
    if abs(position_y[0] - position_y[9]) < 10:
        spd_y[0] *= -1
        spd_y[9] *= -1

    # 1
    if abs(position_x[1] - position_x[2]) < 10:
        spd_x[1] *= -1
        spd_x[2] *= -1
    if abs(position_y[1] - position_y[2]) < 10:
        spd_y[1] *= -1
        spd_y[2] *= -1

    if abs(position_x[1] - position_x[3]) < 10:
        spd_x[1] *= -1
        spd_x[3] *= -1
    if abs(position_y[1] - position_y[3]) < 10:
        spd_y[1] *= -1
        spd_y[3] *= -1

    if abs(position_x[1] - position_x[4]) < 10:
        spd_x[1] *= -1
        spd_x[4] *= -1
    if abs(position_y[1] - position_y[4]) < 10:
        spd_y[1] *= -1
        spd_y[4] *= -1

    if abs(position_x[1] - position_x[5]) < 10:
        spd_x[1] *= -1
        spd_x[5] *= -1
    if abs(position_y[1] - position_y[5]) < 10:
        spd_y[1] *= -1
        spd_y[5] *= -1

    if abs(position_x[1] - position_x[6]) < 10:
        spd_x[1] *= -1
        spd_x[6] *= -1
    if abs(position_y[1] - position_y[6]) < 10:
        spd_y[1] *= -1
        spd_y[6] *= -1

    if abs(position_x[1] - position_x[7]) < 10:
        spd_x[1] *= -1
        spd_x[7] *= -1
    if abs(position_y[1] - position_y[7]) < 10:
        spd_y[1] *= -1
        spd_y[7] *= -1

    if abs(position_x[1] - position_x[8]) < 10:
        spd_x[1] *= -1
        spd_x[8] *= -1
    if abs(position_y[0] - position_y[8]) < 10:
        spd_y[1] *= -1
        spd_y[8] *= -1

    if abs(position_x[1] - position_x[9]) < 10:
        spd_x[1] *= -1
        spd_x[9] *= -1
    if abs(position_y[1] - position_y[9]) < 10:
        spd_y[1] *= -1
        spd_y[9] *= -1

    # 2
    if abs(position_x[2] - position_x[3]) < 10:
        spd_x[2] *= -1
        spd_x[3] *= -1
    if abs(position_y[2] - position_y[3]) < 10:
        spd_y[2] *= -1
        spd_y[3] *= -1

    if abs(position_x[2] - position_x[4]) < 10:
        spd_x[2] *= -1
        spd_x[4] *= -1
    if abs(position_y[2] - position_y[4]) < 10:
        spd_y[2] *= -1
        spd_y[4] *= -1

    if abs(position_x[2] - position_x[5]) < 10:
        spd_x[2] *= -1
        spd_x[5] *= -1
    if abs(position_y[2] - position_y[5]) < 10:
        spd_y[2] *= -1
        spd_y[5] *= -1

    if abs(position_x[2] - position_x[6]) < 10:
        spd_x[2] *= -1
        spd_x[6] *= -1
    if abs(position_y[2] - position_y[6]) < 10:
        spd_y[2] *= -1
        spd_y[6] *= -1

    if abs(position_x[2] - position_x[7]) < 10:
        spd_x[2] *= -1
        spd_x[7] *= -1
    if abs(position_y[2] - position_y[7]) < 10:
        spd_y[2] *= -1
        spd_y[7] *= -1

    if abs(position_x[2] - position_x[8]) < 10:
        spd_x[2] *= -1
        spd_x[8] *= -1
    if abs(position_y[2] - position_y[8]) < 10:
        spd_y[2] *= -1
        spd_y[8] *= -1

    if abs(position_x[2] - position_x[9]) < 10:
        spd_x[2] *= -1
        spd_x[9] *= -1
    if abs(position_y[2] - position_y[9]) < 10:
        spd_y[2] *= -1
        spd_y[9] *= -1

    # 3
    if abs(position_x[3] - position_x[4]) < 10:
        spd_x[3] *= -1
        spd_x[4] *= -1
    if abs(position_y[3] - position_y[4]) < 10:
        spd_y[3] *= -1
        spd_y[4] *= -1

    if abs(position_x[3] - position_x[5]) < 10:
        spd_x[3] *= -1
        spd_x[5] *= -1
    if abs(position_y[3] - position_y[5]) < 10:
        spd_y[3] *= -1
        spd_y[5] *= -1

    if abs(position_x[3] - position_x[6]) < 10:
        spd_x[3] *= -1
        spd_x[6] *= -1
    if abs(position_y[3] - position_y[6]) < 10:
        spd_y[3] *= -1
        spd_y[6] *= -1

    if abs(position_x[3] - position_x[7]) < 10:
        spd_x[3] *= -1
        spd_x[7] *= -1
    if abs(position_y[3] - position_y[7]) < 10:
        spd_y[3] *= -1
        spd_y[7] *= -1

    if abs(position_x[3] - position_x[8]) < 10:
        spd_x[3] *= -1
        spd_x[8] *= -1
    if abs(position_y[3] - position_y[8]) < 10:
        spd_y[3] *= -1
        spd_y[8] *= -1

    if abs(position_x[3] - position_x[9]) < 10:
        spd_x[3] *= -1
        spd_x[9] *= -1
    if abs(position_y[3] - position_y[9]) < 10:
        spd_y[3] *= -1
        spd_y[9] *= -1

    # 4
    if abs(position_x[4] - position_x[5]) < 10:
        spd_x[4] *= -1
        spd_x[5] *= -1
    if abs(position_y[4] - position_y[5]) < 10:
        spd_y[4] *= -1
        spd_y[5] *= -1

    if abs(position_x[4] - position_x[6]) < 10:
        spd_x[4] *= -1
        spd_x[6] *= -1
    if abs(position_y[4] - position_y[6]) < 10:
        spd_y[4] *= -1
        spd_y[6] *= -1

    if abs(position_x[4] - position_x[7]) < 10:
        spd_x[4] *= -1
        spd_x[7] *= -1
    if abs(position_y[4] - position_y[7]) < 10:
        spd_y[4] *= -1
        spd_y[7] *= -1

    if abs(position_x[4] - position_x[8]) < 10:
        spd_x[4] *= -1
        spd_x[8] *= -1
    if abs(position_y[4] - position_y[8]) < 10:
        spd_y[4] *= -1
        spd_y[8] *= -1

    if abs(position_x[4] - position_x[9]) < 10:
        spd_x[4] *= -1
        spd_x[9] *= -1
    if abs(position_y[4] - position_y[9]) < 10:
        spd_y[4] *= -1
        spd_y[9] *= -1

    # 5
    if abs(position_x[5] - position_x[6]) < 10:
        spd_x[5] *= -1
        spd_x[6] *= -1
    if abs(position_y[5] - position_y[6]) < 10:
        spd_y[5] *= -1
        spd_y[6] *= -1

    if abs(position_x[5] - position_x[7]) < 10:
        spd_x[5] *= -1
        spd_x[7] *= -1
    if abs(position_y[5] - position_y[7]) < 10:
        spd_y[5] *= -1
        spd_y[7] *= -1

    if abs(position_x[5] - position_x[8]) < 10:
        spd_x[5] *= -1
        spd_x[8] *= -1
    if abs(position_y[5] - position_y[8]) < 10:
        spd_y[5] *= -1
        spd_y[8] *= -1

    if abs(position_x[5] - position_x[9]) < 10:
        spd_x[5] *= -1
        spd_x[9] *= -1
    if abs(position_y[5] - position_y[9]) < 10:
        spd_y[5] *= -1
        spd_y[9] *= -1

    # 6
    if abs(position_x[6] - position_x[7]) < 10:
        spd_x[6] *= -1
        spd_x[7] *= -1
    if abs(position_y[6] - position_y[7]) < 10:
        spd_y[6] *= -1
        spd_y[7] *= -1

    if abs(position_x[6] - position_x[8]) < 10:
        spd_x[6] *= -1
        spd_x[8] *= -1
    if abs(position_y[6] - position_y[8]) < 10:
        spd_y[6] *= -1
        spd_y[8] *= -1

    if abs(position_x[6] - position_x[9]) < 10:
        spd_x[6] *= -1
        spd_x[9] *= -1
    if abs(position_y[6] - position_y[9]) < 10:
        spd_y[6] *= -1
        spd_y[9] *= -1

    # 7
    if abs(position_x[7] - position_x[8]) < 10:
        spd_x[7] *= -1
        spd_x[8] *= -1
    if abs(position_y[7] - position_y[8]) < 10:
        spd_y[7] *= -1
        spd_y[8] *= -1

    if abs(position_x[7] - position_x[9]) < 10:
        spd_x[7] *= -1
        spd_x[9] *= -1
    if abs(position_y[7] - position_y[9]) < 10:
        spd_y[7] *= -1
        spd_y[9] *= -1

    # 8
    if abs(position_x[8] - position_x[9]) < 10:
        spd_x[7] *= -1
        spd_x[9] *= -1
    if abs(position_y[8] - position_y[9]) < 10:
        spd_y[7] *= -1
        spd_y[9] *= -1


    # check การกดรูป

    if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                (a,b) = pygame.mouse.get_pos()
                
                for num in range(Numball):

                    if (position_x[num]-10) <= a <= (position_x[num]+10) and (position_y[num]-10) <= b <= (position_y[num]+10) :
                        position_x[num],position_y[num] = -1000,-1000
    

    clock.tick(fps)
    
    pygame.display.flip()
    

pygame.quit()





# References
# https://youtu.be/jI0uudhexLY
# https://www.pygame.org/docs/ref/surface.html
# https://www.youtube.com/watch?v=zaVJV8zIli4
# pygame_demo1 
# https://www.youtube.com/watch?v=1_H7InPMjaY