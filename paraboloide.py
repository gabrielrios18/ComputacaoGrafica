from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

#aproveitando o paraboloide feito em aula pelos alunos com a ajuda do professor só botei a malha

r = 1
n = 50
halfpi = math.pi/2

def f(u, v):
    theta = (v*2*math.pi)/(n-1)
    w = ((u * 4) / (n - 1)) - 2
    x = ( w*math.cos(theta))
    y = w**3
    z = w*math.sin(theta)
    return x, y, z

def desenhaEsfera():
    glBegin(GL_POINTS)
    for i in range(n):
        for j in range(n):
            glVertex3fv(f(i,j))
    glEnd()

a = 0

def desenhaMalha():
    
    for i in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n):   
            glVertex3fv(f(i,j))
            glVertex3fv(f(i - 1,j))
        glEnd()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,0,1,0)
    desenhaEsfera()    
    glPopMatrix()
    glPushMatrix()
    glRotatef(a,0,1,0)
    desenhaMalha()    
    glPopMatrix()
    glutSwapBuffers()
    a += 1
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Paraboloide")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-8)
glutTimerFunc(50,timer,1)
glutMainLoop()

