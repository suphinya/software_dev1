##############################################################
# Name : Suphinya Wu
# ID : 6201012630100
##############################################################


import threading
import time
import cmath
import pygame
from random import randint, randrange, random

print( 'File:', __file__ )

def mandelbrot(c,max_iters=100):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c
        i += 1 
    return i

# initialize pygame
pygame.init()

# create a screen of width=600 and height=400
scr_w, scr_h = 500, 500 
screen = pygame.display.set_mode( (scr_w, scr_h) )

# set window caption
pygame.display.set_caption('Fractal Image: Mandelbrot') 

# create a clock
clock = pygame.time.Clock()

# create a surface for drawing
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

w2, h2 = scr_w/2, scr_h/2 # half width, half screen


def thread_man(id,surface,lock,barrier):
    
        scale = 0.006
        offset = complex(-0.55,0.0)

        for i in range ((id-1)*5,500):
            
            for j in range (0,scr_h):

                re = scale*(i-w2) + offset.real
                im = scale*(j-h2) + offset.imag
                c = complex( re, im )
                color = mandelbrot(c, 63)
                r = (color << 6) & 0xc0
                g = (color << 4) & 0xc0
                b = (color << 2) & 0xc0

                with lock:
                    surface.set_at( (i, j), (255-r,255-g,255-b) )
                # pass the barrier
                try:
                    barrier.wait()
                except threading.BrokenBarrierError:
                    pass

                 
            
                
# set the number of threads to be created

N = 100

# create a thread lock 
lock = threading.Lock()

# create a barrier
barrier = threading.Barrier(N+1)

# a list for keeping the thread objects
list_threads = []

for i in range(N):
    id = (i+1)
    t = threading.Thread(target=thread_man, args=(id,surface,lock,barrier))
    t.setName( 'Thread-{:03d}'.format(id) )
    list_threads.append( t )

# start threads
for t in list_threads:
    t.start()


running = True

while running:
    
    # This limits the while loop to a max of 100 times per second.
    clock.tick(100) 
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    #------------------------------------------------
    try:
        barrier.wait()
    except threading.BrokenBarrierError:
        pass

    with lock:
        # draw the surface on the screen
        screen.blit( surface, (0,0) )
    
    pygame.display.flip()
    # update the display
    pygame.display.update()



barrier.reset()
pygame.quit()
print( 'PyGame done...')
################################################################


#refferance
# python_threading_demo-7
# python_threading_demo-8