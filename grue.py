import pygame
import random
from pygame.locals import *
from pygame import key
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 248, 220)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)

screen_size = LARGEUR_ECRAN, HAUTEUR_ECRAN = 500, 300
#OBJ
vbase = ((0, 0),
		(100, 0),
		(100, 50),
		(0, 50))
vbarm = ((-10, 0),
		(10, 0),
		(10, 150),
		(-10, 150)
		)
vlarm = ((-10, 0),
		(10, 0),
		(10, 100),
		(-10, 100))
ebase = ((0, 1),
		(1, 2),
		(2, 3),
		(3, 0))
thread = [[0, 0],
		[0, 0]]
box = ((-10, 0),
		(10, 0),
		(10, -20),
		(-10, -20))

#fonctions
def draw_line(vertices):
	glBegin(GL_LINES)
	for vertex in vertices:
		glVertex2iv(vertex)
	glEnd()
def draw_rect(vertices):
	glBegin(GL_QUADS)
	for vertex in vertices:
		glVertex2iv(vertex)
	glEnd()
def dessinerRepere(echelle = 1):
	glPushMatrix()
	glScalef(echelle,echelle,echelle)
	glLineWidth(3)
	glBegin(GL_LINES)
	glColor3ub(0,0,255)
	glVertex2i(0,0)
	glVertex2i(1,0)
	glColor3ub(0,255,0)
	glVertex2i(0,0)
	glVertex2i(0,1)
	glEnd()
	glPopMatrix()

def main():
	#init
	pygame.init()
	pygame.display.set_mode(screen_size, DOUBLEBUF|OPENGL)
	pygame.key.set_repeat(100) #activer repetition auto
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,LARGEUR_ECRAN,0,HAUTEUR_ECRAN)
	#variables
	angle1 = -45
	angle2 = -30
	thread_size = 50
	thread_up = 0
	thread_down = 0
	lright = 0
	lleft = 0
	bright = 0
	bleft = 0
	#Loop
	while True:
		#gestion des evenements	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				print("STOP")
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					print("STOP")
					quit()
				elif event.key == pygame.K_LEFT:
					if (pygame.key.get_mods() & pygame.KMOD_SHIFT):
						bleft = 1
						lleft = 0
					else:
						bleft = 0
						lleft = 1
				elif event.key == pygame.K_RIGHT:
					if (pygame.key.get_mods() & pygame.KMOD_SHIFT):
						bright = 1
						lright = 0
					else:
						bright = 0
						lright = 1
				elif event.key == pygame.K_UP:
					thread_up = 1
				elif event.key == pygame.K_DOWN:
					thread_down = 1
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
						bleft = 0
						lleft = 0
				elif event.key == pygame.K_RIGHT:
						bright = 0
						lright = 0
				elif event.key == pygame.K_UP:
					thread_up = 0
				elif event.key == pygame.K_DOWN:
					thread_down = 0
			elif event.type == pygame.MOUSEBUTTONDOWN:
				thread_up = 1
			elif event.type == pygame.MOUSEBUTTONUP:
				thread_up = 0
		#prepare
		glClear(GL_COLOR_BUFFER_BIT) #efface le taampon d'affichage
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		if thread_up:
			if thread_size < 75:
				thread_size += 2
		if thread_down:
			if thread_size > 1:
				thread_size -= 2
		if bright:
			if angle1 > -89:
				angle1 -= 2
		if bleft:
			if angle1 < 89:
				angle1 += 2
		if lright:
			if angle2 > -89:
				angle2 -= 2
		if lleft:
			if angle2 < 89:
				angle2 +=2

		#dessine
		dessinerRepere(50)
		#base
		glTranslated(30, 0, 0)
		glColor3ubv((ORANGE))
		draw_rect(vbase)
	#barm
		glTranslated(50, 50, 0)
		glRotated(angle1, 0, 0, 1)
		glColor3ubv(RED)
		draw_rect(vbarm)
		#larm
		glTranslated(0, 150, 0)
		glRotated(angle2, 0, 0, 1)
		glColor3ubv(BLUE)
		draw_rect(vlarm)
		#thread
		thread[1][1] = -thread_size
		glTranslated(0, 100, 0)
		glRotated(-angle1-angle2, 0, 0, 1)
		glColor3ubv(WHITE)
		draw_line(thread)
		#box
		glTranslated(0, -thread_size, 0)
		glColor3ubv(BROWN)
		draw_rect(box)
		
	#refresh screen
		pygame.display.flip() #refresh screen
		pygame.time.wait(20) #wait

#debut programme
if __name__ == "__main__":
	main()