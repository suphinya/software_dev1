from check import checkdata
from tree import tree
#------------------------ package ------------------------------------------------
openfile = open('alltest.txt')
readfile = openfile.readlines()

listtree = []
for i in range(len(readfile)):
    data = readfile[i].rstrip('\n')
    classcheck = checkdata(data)
    listdata = classcheck.checkntrans()
    classtree = tree(listdata)
    treenode = classtree.maketree()
    listtree += [treenode]

for i in range(len(listtree)):
    print(listtree[i])


#------------------------- draw --------------------------------------------------

##--------------------- วาดทีละข้อมูลก่อนยังไม่ได้ใช้ข้อมูลด้านบนที่อ่านไฟล์ทีเดียว -------------------------

datainput = "(!(I0&I1))+(!(I1+I2))" 
inclassch = checkdata(datainput)
showlist = inclassch.checkntrans()
inclass = tree(showlist)
data = inclass.maketree()

import pygame,sys

width = 1200    #window size
height = 900

# position node ** node high 4 **
w_node = [600,300,900,150,450,750,1050,75,225,375,525,675,825,975,1125,38,112,188,262,338,412,488,562,638,712,788,862,938,1012,1088,1162]
h_node = [100,250,250,400,400,400,400,550,550,550,550,550,550,550,550,700,700,700,700,700,700,700,700,700,700,700,700,700,700,700,700]

# start pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Expresstion Tree")
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#colors
pink = (255,204,229)
blue = (102,178,255)
white = (255,255,255)

# list for check 
normal = ['I0','I1','I2','I3','+','&','0','1','!']
notnormal = ['!I0','!I1','!I2','!I3']

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.image.save( screen, 'expresstiontree.jpg' ) # save picture before close
            pygame.quit()
            sys.exit()

    font = pygame.font.SysFont("Cordia New",60) #font

    
    for i in range(len(data)):

        if data[i] != 'None' and data[i] != '':
            
            if data[i] in normal : # normal have ! but no not ex.>> !I0
                pygame.draw.circle(surface,blue,(w_node[i],h_node[i]),32)
                text = font.render(data[i], True, white)
                surface.blit(text,(w_node[i]-10,h_node[i]-20))
            
            elif data[i] in notnormal : # have not 
                pygame.draw.circle(surface,blue,(w_node[i],h_node[i]),35)
                text = font.render('!', True, white)
                surface.blit(text,(w_node[i]-10,h_node[i]-20))
                pygame.draw.circle(surface,blue,(w_node[i],h_node[i]+100),35)
                text = font.render(data[i].lstrip('!'), True, white)
                surface.blit(text,(w_node[i]-10,h_node[i]+80))
                pygame.draw.line(screen,pink,(w_node[i],h_node[i]),(w_node[i],h_node[i]+80),10)
            
            if i > 0 : # draw line to link with root

                root = int((i-1)/2)

                if i == ((root*2)+1) :  # left
                    pygame.draw.line(screen,pink,(w_node[root],h_node[root]),(w_node[i],h_node[i]),10)

                elif i == ((root*2)+2) : #right
                    pygame.draw.line(screen,pink,(w_node[root],h_node[root]),(w_node[i],h_node[i]),10)


    font2 = pygame.font.SysFont("Cordia New",40)
    textinput = font2.render("Input : " + datainput,True,(255,255,255))
    screen.blit(textinput,(500,850))
    screen.blit( surface, (0,0) )
    pygame.display.update()

#=========================================================================================================

#****** รอ update ต่อไปที่อ่านไฟล์แล้ววาดทีเดียว *********#