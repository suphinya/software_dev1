###################################################################
# Name : Suphinya Wu
# ID : 6201012630100
###################################################################

import pygame
import pygame.camera
from pygame.locals import *
import sys

# size
scr_w = 640
scr_h = 480

def open_camera( frame_size=(640,480),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None

# open camera
camera = open_camera()
if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)

# try to capture the next image from the camera 
img = camera.get_image()
# save the current image into the output file
pygame.image.save( img, 'image.jpg' )
camera.stop()

# start
pygame.init()
screen = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption("Click Picture")
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# get the image size
#img_rect = img.get_rect()


# draw (MxN) tiles of the images
M,N = 10,8
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        # draw a green frame (tile)
        rect = (i*rw, j*rh, rw, rh)
        stroke = pygame.draw.rect( img, (0,255,0), rect, 1)
        surface.blit( img , rect, rect )
        
        
pos_a = None   
pos_b = None
pos_c = None
pos_d = None
rect_ab = None

is_running = True
while is_running:
    
    bg = screen.fill((255,255,255))

    # close programe
    for e in pygame.event.get():
        
        # switch picture on screen by click mouse
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                [a,b] = pygame.mouse.get_pos()
                print(a,b)

                for i in range(M):
                    for j in range(N):
                        allrect = (i*rw, j*rh, rw, rh)
                        # check position mouse 
                        if i*rw <= a <= (i+1)*rw and j*rh <= b <= (j+1)*rh:
                            print(i*rw,j*rh)
                            pos_a = i*rw
                            pos_b = j*rh
                            rect_ab = (i*rw, j*rh, rw, rh)

        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                [c,d] = pygame.mouse.get_pos()
                print(c,d)

                for i in range(M):
                    for j in range(N):
                        allrect = (i*rw, j*rh, rw, rh)
                        # check position mouse 
                        if i*rw <= c <= (i+1)*rw and j*rh <= d <= (j+1)*rh:
                            print(i*rw,j*rh)
                            print('Switch Here')
                            pos_c = i*rw
                            pos_d = j*rh
                            surface.blit( img , (pos_a,pos_b) , allrect )
                            surface.blit( img , (pos_c,pos_d) , rect_ab )
                            

                            
        
        # close program
        if e.type == pygame.QUIT:
            is_running = False 
            pygame.quit()
            sys.exit()


    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()

print(pos_a,pos_b,pos_c,pos_d)

print("Done...")
#####################################################

# refference
# https://www.pygame.org/docs/ref/surface.html