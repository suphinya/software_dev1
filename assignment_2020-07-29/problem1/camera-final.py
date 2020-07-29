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
img_rect = img.get_rect()


# draw (MxN) tiles of the images
M,N = 10,8
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        # draw a green frame (tile)
        rect = (i*rw, j*rh, rw, rh)
        stroke = pygame.draw.rect( screen, (0,255,0), rect, 1)
        surface.blit( screen , rect, rect )
    

is_running = True
while is_running:
    
    bg = screen.fill((0,0,0))

    # close programe
    for e in pygame.event.get():
        
        # draw picture on screen by click mouse
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                [a,b] = pygame.mouse.get_pos()
                
                for i in range(M):
                    for j in range(N):
                        allrect = (i*rw, j*rh, rw, rh)
                        # check position mouse is in stroke i
                        if i*rw <= a <= (i+1)*rw :
                            if j*rh <= b <= (j+1)*rh :
                                surface.blit( img, (i*rw,j*rh) , allrect )
                                print('Show Picture Here')
        # close program
        if e.type == pygame.QUIT:
            is_running = False 
            pygame.quit()
            sys.exit()


    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()

print("Done...")
#####################################################

# refference
# https://www.pygame.org/docs/ref/surface.html