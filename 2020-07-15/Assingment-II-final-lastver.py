###############################
# code Assingment II
# student ID : 6201012630100
###############################

import pygame ,sys
from random import *

# ขนาด
width = 800
height = 600

# เฟรมเรท
fps = 20

# จำนวนรูป
N = 10

# ตั้งค่าเริ่มต้น
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))

# ที่เก็บค่าตัวแปรต่างๆ
## ตำแหน่ง x,y
position_x = []
position_y = []
## สี
allcolor = []
# รัศมี
radius =[]
# ความเร็วในการเคลื่อนที่ x,y
spd_x = []
spd_y = []
allrect = []
allradius = []

for i in range(N):

    r = randint(30,40)
    alpha = randint(50,255)
    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255)
    randomcolor = (R,G,B,alpha)
    x,y = randint(r,width-r), randint(r,height-r)
    runx = randint(5,15)
    runy = randint(5,15)
    
    
    position_x += [x]
    position_y += [y]
    spd_x += [runx]
    spd_y += [runy]
    allcolor += [randomcolor]
    radius += [r]
    allradius += [r]

allradius.sort(reverse=True)

# กำหนดค่าของรูป (x,y,width,height)  โดยในที่นี้เราต้องการจะใช้การวาดวงรีเป็นวาดวงกลม ดังนั้น width,height จึงเป็นรัศมีที่เท่ากัน
for i in range (N):
    cir_rect = pygame.Rect(position_x[i],position_y[i],radius[i],radius[i])
    allrect += [cir_rect]

# ฟังก์ชันการสร้างและกระทบ
def bouncing_rect():
    global spd_x , spd_y

    for i in range (N):
        allrect[i].x += spd_x[i]
        allrect[i].y += spd_y[i]

    # เด้งหน้าต่าง
    for i in range(N):
        if allrect[i].right >= width or allrect[i].right <= 50:
            spd_x[i] *= -1  
        if allrect[i].bottom >= height or allrect[i].top <= 10:
            spd_y[i] *= -1

        # เด้งกันเอง
        for j in range(N):
            if i<j:
                if allrect[i].colliderect(allrect[j]):
                    if abs(allrect[i].top - allrect[j].bottom) < (radius[i] + radius[j]) or abs(allrect[i].bottom - allrect[j].top) < (radius[i] + radius[j]):
                        spd_x[i] *= -1
                        spd_x[j] *= -1
                    
                    if abs(allrect[i].right - allrect[j].left) < (radius[i] + radius[j]) or abs(allrect[i].right - allrect[j].left) < (radius[i] + radius[j]):
                        spd_y[i] *= -1
                        spd_y[j] *= -1
        
        # วาดวงรีให้เป็นวงกลม
        pygame.draw.ellipse(screen,allcolor[i],allrect[i])

clickmouse = 0

while True:
    # click close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                (a,b) = pygame.mouse.get_pos()
                # การเลือกรัศมีใหญ่สุดในการคลิ๊ก
                for h in range(N):
                    if (allrect[h].x - 30) <= a <= (allrect[h].x + 30) and (allrect[h].y - 30) <= b <= (allrect[h].y + 30) :
                        
                        if radius[h] == allradius[clickmouse] : 
                            allrect[h].x = -1000
                            allrect[h].y = -1000  
                            clickmouse += 1 
                
                    
                    

    
    screen.fill((0,0,0))
    bouncing_rect()
    pygame.display.flip()
    clock.tick(fps)



# referrence
# https://www.youtube.com/watch?v=1_H7InPMjaY&t=1s
# http://apisit13411.blogspot.com/2018/09/pygamedraw.html