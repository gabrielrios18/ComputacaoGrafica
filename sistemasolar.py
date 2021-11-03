from __future__ import division
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

year = 0
day = 0

def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)

import time

start_time = time.time()

def display():

    t = time.time() - start_time
    year_period = 60.0                  # 60 seconds for simulating one year 
    year     = (t / year_period)
    day      = 365 * year
    moon_sid = (365 / 27.3) * year

    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glEnable( GL_DEPTH_TEST )

    glColor4f (1.0, 1.0, 0, 1)
    glPushMatrix()
    sun=glutSolidSphere(1.0, 20, 16)             

    glRotatef(year*360.0, 0.0, 1.0, 0.0)      
    glTranslatef(3.0, 0.0, 0.0)              

    glPushMatrix()                            

    glPushMatrix()
    glRotatef(1.0, 0.0, 1.0, 0.0)      
    glRotatef(90-23.4, 1.0, 0.0, 0.0)        
    glColor3f (0, 0, 1)                      
    earth=glutWireSphere(0.3, 10, 8)               
    glPopMatrix()

    glPushMatrix()
    glRotatef(moon_sid*360.0, 0.0, 1.0, 0.0) 
    glTranslatef(1.0, 0.0, 0.0)             
    glRotatef(1, 1.0, 0.0, 0.0)
    glColor4f (0.4, 0.5, 0.6, 1)                         
    moon=glutWireSphere(0.1, 10, 8)               
    glPopMatrix()

    glPopMatrix() 

    glPopMatrix()
    glutSwapBuffers()

def reshape(w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   gluPerspective(70.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition (100, 100)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow("Sistema solar")
init ()
glutDisplayFunc(display)
glutIdleFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()