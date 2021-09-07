from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math


h = 3
v1 = []
v2 = []
r = 2
lados_min = 3
a = (2*math.pi)/lados_min 

for i in range(0,lados_min):
    x = r*math.cos(a*i)
    y = 0    
    z = r*math.sin(a*i)
    v1 += [[x,y,z]]

for i in range(0,lados_min):
    x = r*math.cos(a*i)
    y = h  
    z = r*math.sin(a*i)
    v2 += [[x,y,z]]


def prisma():

    #Base Inferior
    glColor3f(  1, 0, 0 ) 
    glBegin(GL_POLYGON)
    
    for vertex in v1:
        glVertex3fv(vertex)

    glEnd()

    # Meio
    glBegin(GL_QUAD_STRIP)
    glColor3f( 1, 0, 0 ) 
    i = 0
    for vertex in v1:
        glVertex3fv(vertex)
        glVertex3fv(v2[i])
        i += 1
    glVertex3fv(v1[0]) 
    glVertex3fv(v2[0]) 
    glEnd()

    #BaseSuperior
    glBegin(GL_POLYGON)
    glColor3f( 1,0, 0 ) 
    for vertex in v2:
        glVertex3fv(vertex)

    glEnd()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,0,1,0)
    glScalef(2,2,2)
    prisma()
    glPopMatrix()
    glutSwapBuffers()
    a += 1
    return

#Botei esse comando no mouse para aumentar e diminuir os lados conforme clicar nos botoes mas n sei porque n ta funcionando
def NumLados(button, state, x, y):
	global  lados_min

	if button == 0 and state == 0 and lados_min :
		lados_min += 1
	elif button == 2 and state == 0 and lados_min > 3:
		lados_min -= 1
	

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

if __name__ == '__main__':
    # PROGRAMA PRINCIPAL
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("PrismaNlados")
    glutDisplayFunc(desenha)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.,0.,0.,1.)
    gluPerspective(45,800.0/600.0,0.1,100.0)
    glTranslatef(0.0,0.0,-20)
    glutTimerFunc(50,timer,1)
    glutMouseFunc(NumLados)
    glutMainLoop()

