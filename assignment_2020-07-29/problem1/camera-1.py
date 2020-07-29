###################################################################
# Name : Suphinya Wu
# ID : 6201012630100
###################################################################

import pygame
import pygame.camera
from pygame.locals import *
import sys

def open_camera( frame_size=(640,480),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

scr_w, scr_h = 640, 480

pygame.init()

camera = open_camera()
if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)

screen = pygame.display.set_mode((scr_w, scr_h))

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# draw (MxN) tiles of the images
M,N = 10,8
rw, rh = scr_w//M, scr_h//N
for i in range(M):
    for j in range(N):
        # draw a green frame (tile)
        rect = (i*rw, j*rh, rw, rh)
        black = pygame.draw.rect( screen, (0,0,0), rect)
        storke = pygame.draw.rect( screen, (0,255,0), rect, 1)
        surface.blit( screen , rect, rect )

img = None
is_running = True 
while is_running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )
                
    # try to capture the next image from the camera 
    img = camera.get_image()
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()

            
    for i in range(M):
        for j in range(N):
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    (a,b) = pygame.mouse.get_pos()
                    rect = (i*rw, j*rh, rw, rh)
                    if i*rw <= a <= (i+1)*rw:
                        if j*rh <= b <= (j+1)*rh:

                            print('here')
                            surface.blit( img, (i*rw,j*rh), rect)
                    

    # write the surface to the screen and update the display
    screen.blit( surface, (0,0) )
    pygame.display.update()

# close the camera
camera.stop()

print('Done....')
###################################################################