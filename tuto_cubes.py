import pygame
import random
from pygame.locals import *
from pygame import key
from OpenGL.GL import *
from OpenGL.GLU import *
print("import done.")

vertices= ( #x, y, z
	(1, 0, -1),
	(1, 2, -1),
	(-1, 2, -1),
	(-1, 0, -1),
	(1, 0, 1),
	(1, 2, 1),
	(-1, 0, 1),
	(-1, 2, 1)
	)
surfaces = ( #surfaces are defined by 4 vertices
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6)
	)
ground_vertices = ( #defined by 4 vertices
	(-10,-0.1,50),
	(10,-0.1,50),
	(-10,-0.1,-300),
	(10,-0.1,-300),
	)
ground_surfaces = (0,1,2,3)
edges = ( #vertex1, vertex2
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
	)
colors = ( #rgb between 0 and 1
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,1,0),
	(1,1,1),
	(0,1,1),
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(1,0,0),
	(1,1,1),
	(0,1,1),
	)
print("objects create.")

def Ground():
	glBegin(GL_QUADS)
	x = 0
	for vertex in ground_vertices:
		x+=1
		glColor3fv((0,1,1))
		glVertex3fv(vertex)
	glEnd()

def Cube(vertices):
	glBegin(GL_QUADS)
	for surface in surfaces:
		x = 0
		for vertex in surface:
			x+=1
			glColor3fv(colors[x]) #choisie la couleur de l'objet a crée
			glVertex3fv(vertices[vertex]) #appel glVertex3fv pour chaque angle 
	glEnd()
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()

def set_vertices(max_distance):
	x_value_change = random.randrange(-5,5)
	y_value_change = 0
	z_value_change = random.randrange(-1*max_distance,-20)
	new_vertices = []
	for vert in vertices:
		new_vert = []
		new_x = vert[0] + x_value_change
		new_y = vert[1] + y_value_change
		new_z = vert[2] + z_value_change
		new_vert.append(new_x)
		new_vert.append(new_y)
		new_vert.append(new_z)
		new_vertices.append(new_vert)
	return new_vertices

def main():
	print("START")
	#variable de deplacement
	x_move = 0
	rx_move = 0
	y_move = 0
	ry_move = 0
	z_move = 0
	rz_move = 0
	screen_size = (800,600)

	pygame.init()
	#initialise la matrice
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	pygame.display.set_mode(screen_size, DOUBLEBUF|OPENGL)
	pygame.key.set_repeat(100) #activer repetition auto
	
	gluPerspective(45, (screen_size[0]/screen_size[1]), 0.1, 50.0) #fov, aspect ration (width by height), znear, zfar (znear et zfar correspondent au valeur de proximité entre lesquel l'objet est visible )
	# glTranslatef(random.randrange(-3,3),0, random.randrange(-35, -25)) # recule de 5 unité (recule la camera?)

	max_distance = 100
	cube_dict = {}
	for x in range(20):
		cube_dict[x] = set_vertices(max_distance)
	object_passed = False

	##cylindre
	params = gluNewQuadric()
	gluQuadricDrawStyle(params,GLU_LINE)
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
					ry_move = -1
				elif event.key == pygame.K_RIGHT:
					ry_move = 1
				elif event.key == pygame.K_UP:
					y_move = 1
				elif event.key == pygame.K_DOWN:
					y_move = -1
				elif event.key == pygame.K_z:
					z_move = 1
				elif event.key == pygame.K_s:
					z_move = -1
				elif event.key == pygame.K_d:
					x_move = -1
				elif event.key == pygame.K_q:
					x_move = 1
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					ry_move = 0
				elif event.key == pygame.K_RIGHT:
					ry_move = 0
				elif event.key == pygame.K_UP:
					y_move = 0
				elif event.key == pygame.K_DOWN:
					y_move = 0
				elif event.key == pygame.K_z:
					z_move = 0
				elif event.key == pygame.K_s:
					z_move = 0
				elif event.key == pygame.K_d:
					x_move = 0
				elif event.key == pygame.K_q:
					x_move = 0
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,1.0)
				elif event.button == 5:
					glTranslatef(0,0,-1.0)
		#glRotatef(1, 3, 1, 1) #multiplie matrice par matrice de rotation (angle, x, y, z)
#		glRotated(45,0,0,1) 45° autour de Z
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear screen
		
		for each_cube in cube_dict:
			Cube(cube_dict[each_cube])		#print cube
	
#Deplacer la camera a un point et tourner la camera a ce meme point	
	
	# recupere position camera	
		# x = glGetDoublev ( GL_MODELVIEW_MATRIX )
		# camera_x = x [ 3 ] [ 0 ] 
		# camera_y = x [ 3 ] [ 1 ]
		# camera_z = x [ 3 ] [ 2 ]
		glTranslatef(x_move, y_move, z_move)
		if rx_move != 0 or ry_move != 0 or rz_move != 0:
			print("rx", rx_move, "ry", ry_move, "rz", rz_move)
			glRotatef(1, rx_move, ry_move, rz_move)
	#print ground
		Ground()
		pygame.display.flip() #refresh screen
		pygame.time.wait(20) #wait

main()