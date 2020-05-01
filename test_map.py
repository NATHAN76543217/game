import pygame
from pygame.locals import *
from pygame import key
from pygame import mouse
from OpenGL.GL import *
from OpenGL.GLU import *
from pywavefront import visualization, Wavefront
print("import done.")

screen_size = LARGEUR_ECRAN, HAUTEUR_ECRAN = 500, 300
ORANGE = (255, 165, 0)

#OBJ
vbase = ((0, 0, 1),
		(100, 0, 1),
		(100, 50, 1),
		(0, 50, 1))
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
def draw_rect(vertices):
	glBegin(GL_QUADS)
	for vertex in vertices:
		glVertex3iv(vertex)
	glEnd()
def main():
	#pygame
	pygame.init()
	pygame.display.set_mode(screen_size, DOUBLEBUF|OPENGL)
	pygame.key.set_repeat(100) #activer repetition auto

	#pywave
	scene = Wavefront('graphism/maison.obj')
	scene.parse()  # Explicit call to parse() needed when parse=False
	#opengl
	glEnable(GL_DEPTH_TEST)
	glMatrixMode(GL_PROJECTION) #choisie la matrice PROJECTION
	glLoadIdentity()
	gluPerspective(45, (screen_size[0]/screen_size[1]), 0.1, 350.0) #fov, aspect ration (width by height), znear, zfar (znear et zfar correspondent au valeur de proximité entre lesquel l'objet est visible )
	
	angleY = 10
	mouse_pos = [0, 0]
	mouse_rel = [0, 0]
	offset_cam = [0, 0]
	pos_map = [0, 0, 0]
	clik = 0
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
			elif event.type == pygame.MOUSEMOTION:
				if clik:
					print("\n\nPOS =", pygame.mouse.get_pos())

					pos = pygame.mouse.get_pos()
					rel = pygame.mouse.get_rel()
					print("rell", rel)
					cnt = 0
					for coord in pos:
						mouse_pos[cnt] = coord
						cnt += 1
					cnt = 0
					for coord in rel:
						offset_cam[cnt] += coord/100
						cnt += 1
					print("OFFSET:", offset_cam)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				clik = 1
			elif event.type == pygame.MOUSEBUTTONUP:
				clik = 0
				mouse_pos[0] = -1
		if mouse_pos[0] > 0:
			print("mouse_rel", mouse_rel)
			print("offset_cam", offset_cam)
			glTranslatef(-offset_cam[0], offset_cam[1], 0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #efface le taampon d'affichage
		glMatrixMode(GL_MODELVIEW) #choisi la matrice MODELVIEW
		glLoadIdentity()		
		
		gluLookAt(4,2,8, 0, 0, 0,0,1,0)

		angleY += 1
		glRotated(angleY, 0, 1, 0)
		# glBegin(GL_QUADS)

		# glColor3ub(255,0,0) #face rouge
		# glVertex3d(1,1,1)
		# glVertex3d(1,1,-1)
		# glVertex3d(-1,1,-1)
		# glVertex3d(-1,1,1)

		# glColor3ub(0,255,0) #face verte
		# glVertex3d(1,-1,1)
		# glVertex3d(1,-1,-1)
		# glVertex3d(1,1,-1)
		# glVertex3d(1,1,1)

		# glColor3ub(0,0,255) #face bleue
		# glVertex3d(-1,-1,1)
		# glVertex3d(-1,-1,-1)
		# glVertex3d(1,-1,-1)
		# glVertex3d(1,-1,1)
		# glEnd()
		glRotated(-angleY, 0, 1, 0)
		glTranslatef(-offset_cam[0], -offset_cam[1], 0)
		visualization.draw(scene)

		#refresh screen
		pygame.display.flip() #refresh screen
		pygame.time.wait(20) #wait

#debut programme
if __name__ == "__main__":
	main()