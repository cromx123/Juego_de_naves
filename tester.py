#programa creado por CromxDev 15.11.2024

import pygame
import numpy as np
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Definir vértices del cubo
vertices = np.array([
    [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1],      #cara de atras
    [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1]   #cara adelante
])
balas = []
direccion_nave = np.array([0, 0, 1]) 
class Bala:
    def __init__(self, x, y, z, direccion, velocidad=0.5):
        self.x = x
        self.y = y
        self.z = z
        self.direccion = direccion  # Dirección en la que se mueve la bala
        self.velocidad = velocidad

    def mover(self):
        # Mueve la bala en la dirección constante
        self.x -= self.direccion[0] * self.velocidad
        self.y -= self.direccion[2] * self.velocidad
        self.z -= self.direccion[1] * self.velocidad

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glColor3ub(255, 0, 0)  # Color de la bala
        sphere = gluNewQuadric()
        gluQuadricDrawStyle(sphere, GLU_FILL)
        gluSphere(sphere, 0.1, 16, 16)
        glPopMatrix()
        
def actualizar_balas():
    for bala in balas[:]:
        bala.mover()
        bala.dibujar()
        if bala.y > 10:  # Si la bala sale de la pantalla, eliminarla
            balas.remove(bala)

def disparar(nave_x, nave_y, nave_z):
    nueva_bala = Bala(nave_x, nave_y, nave_z, direccion_nave)
    balas.append(nueva_bala)

# Función para dibujar un hexágono
def dibujar_fondo_ala():
    glColor3ub(40, 40, 40)
    glBegin(GL_TRIANGLES)
    # Parte superior
    glVertex3f(0.9, -0.1, 0.9) 
    glVertex3f(0.6, -0.1, 0.6)
    glVertex3f(0.55, -1.6, 0.55)
    
    glVertex3f(0.9, 0.1, 0.9)  
    glVertex3f(0.9, 0.9, 0.9) 
    glVertex3f(0.6, 1.6, 0.6)
    
    glVertex3f(0.9, 0.1, 0.9)  
    glVertex3f(0.6, 0.1, 0.6)
    glVertex3f(0.6, 1.6, 0.6)
    # Parte Inferior
    glVertex3f(0.9, -0.1, -0.9) 
    glVertex3f(0.6, -0.1, -0.6)
    glVertex3f(0.55, -1.6, -0.55)
    
    glVertex3f(0.9, 0.1, -0.9)  
    glVertex3f(0.9, 0.9, -0.9) 
    glVertex3f(0.6, 1.6, -0.6)
    
    glVertex3f(0.9, 0.1, -0.9)  
    glVertex3f(0.6, 0.1, -0.6)
    glVertex3f(0.6, 1.6, -0.6)
    
    # parte central
    glVertex3f(0.5, 1.9, 0.4) 
    glVertex3f(0.5, 1.9, -0.4)
    glVertex3f(0.5, 0.1, 0.4)
    
    glVertex3f(0.5, 1.9, -0.4) 
    glVertex3f(0.5, 0.1, 0.4)
    glVertex3f(0.5, 0.1, -0.4)
    
    glEnd()
    
def dibujar_ala():
    glColor3ub(210, 210, 210)
    # No se aplica ninguna transformación, por lo tanto se dibuja la ala original
    glBegin(GL_LINES)
    glVertex3fv(vertices[0])  # Linea superior
    glVertex3f(1, 0, 1)
    
    glVertex3fv(vertices[4])  # Linea inferior
    glVertex3f(1, 0, -1)

    glVertex3fv(vertices[0])  # linea fondo A
    glVertex3f(0.5, 2.0, 0.5)
    
    glVertex3fv(vertices[4])  # Linea fondo B
    glVertex3f(0.5, 2.0, -0.5)
    
    glVertex3f(0.5, 2.0, 0.5)  # Linea union fondo
    glVertex3f(0.5, 2.0, -0.5)
    
    glVertex3f(0.5, 2.0, 0.5)  # Linea centro arriba
    glVertex3f(0.5, -2.0, 0.5)
    
    glVertex3f(0.5, 2.0, -0.5)  # Linea centro abajo
    glVertex3f(0.5, -2.0, -0.5)
    
    glVertex3f(1, 0, 1)  # Union Linea superio - centro
    glVertex3f(0.5, -2.0, 0.5)
    
    glVertex3f(1, 0, -1)  # Union Linea Inferior -centro
    glVertex3f(0.5, -2.0, -0.5)
    
    glVertex3f(1, 0, 1)
    glVertex3f(0.5, 0, 0.5)
    
    glVertex3f(1, 0, -1)
    glVertex3f(0.5, 0, -0.5)
    
    glVertex3f(0.5, 0, 0.5)
    glVertex3f(0.5, 0, -0.5)
    glEnd()
    
    dibujar_fondo_ala()

# Esfera 
def dibujar_esfera():
    glColor3ub(80, 80, 80)  # Color de la esfera (puedes cambiarlo)
    sphere = gluNewQuadric()
    gluQuadricDrawStyle(sphere, GLU_FILL)
    gluSphere(sphere, 0.7, 32, 32)
    
    glColor3ub(20, 20, 20)  # Color de la esfera (puedes cambiarlo)
    sphere = gluNewQuadric()
    gluQuadricDrawStyle(sphere, GLU_LINE)
    gluSphere(sphere, 0.7, 32, 32)

def dibujar_esfera2():
   # Guardar el estado de la transformación actual
    glPushMatrix()
    glTranslatef(0, 0, -5)
    glColor3ub(80, 80, 80)  # Color de la esfera (puedes cambiarlo)
    sphere = gluNewQuadric()
    gluQuadricDrawStyle(sphere, GLU_FILL)
    gluSphere(sphere, 1, 16, 16)
    
    glColor3ub(20, 20, 20)  # Color de la esfera (puedes cambiarlo)
    sphere = gluNewQuadric()
    gluQuadricDrawStyle(sphere, GLU_LINE)
    gluSphere(sphere, 1, 16, 16)
    glPopMatrix()
 # Restaurar el estado de la transformación
    
def generar_puntos_circulo(radio, segmentos, eje_z=0, eje_x=0):
    """Genera los puntos de un círculo en el plano ZY en una lista."""
    puntos = []
    for i in range(segmentos):
        theta = 2.0 * math.pi * i / segmentos
        z = radio * math.cos(theta) + eje_z
        y = radio * math.sin(theta)
        puntos.append((eje_x, y, z))
    return puntos

def dibujar_circulo_con_puntos(puntos):
    """Dibuja un círculo utilizando una lista de puntos."""
    glBegin(GL_LINE_LOOP)
    for punto in puntos:
        glVertex3fv(punto)
    glEnd()

def unir_circulos(puntos1, puntos2):
    """Une dos círculos conectando los vértices correspondientes."""
    glColor3ub(210, 210, 210)
    glBegin(GL_LINES)
    for p1, p2 in zip(puntos1, puntos2):
        glVertex3fv(p1)
        glVertex3fv(p2)

    # Cerrar la última conexión entre el último y el primer punto
    glVertex3fv(puntos1[0])
    glVertex3fv(puntos2[0])
    glEnd()
    
def nave():
    glPushMatrix()
    glTranslatef(-1.5, 0, 0)
    dibujar_esfera()
    glTranslatef(-2, 0, 0)
    dibujar_fondo_ala()
    dibujar_ala()
    glTranslatef(4, 0, 0)
    glScalef(-1, 1, 1)
    dibujar_ala() 
    glColor3ub(210, 210, 210)
    glTranslatef(0.5, 0, 0)
    # Generar y dibujar el primer círculo
    puntos_circulo1 = generar_puntos_circulo(0.3, 25, eje_x=0)
    dibujar_circulo_con_puntos(puntos_circulo1)
    puntos_circulo2 = generar_puntos_circulo(0.5, 25, eje_x=1)
    dibujar_circulo_con_puntos(puntos_circulo2)
    unir_circulos(puntos_circulo1, puntos_circulo2)
    glScalef(-1, 1, 1)
    glTranslatef(-3, 0, 0)
    # Generar y dibujar el primer círculo
    puntos_circulo1 = generar_puntos_circulo(0.3, 10, eje_x=0)
    dibujar_circulo_con_puntos(puntos_circulo1)

    puntos_circulo2 = generar_puntos_circulo(0.5, 10, eje_x=1)
    dibujar_circulo_con_puntos(puntos_circulo2)

    unir_circulos(puntos_circulo1, puntos_circulo2)
    
    glPopMatrix()

def girar_nave_al_punto(angulo, eje='z', punto=(0, 0, 0)):
    angulo_rad = math.radians(angulo)  # Convierte el ángulo a radianes
    px, py, pz = punto  # Punto alrededor del cual queremos girar
    
    # Traslada la nave al origen
    glTranslatef(-px, -py, -pz)
    
    # Define la matriz de rotación en función del eje
    if eje == 'x':
        rotacion = np.array([
            [1, 0, 0, 0],
            [0, math.cos(angulo_rad), -math.sin(angulo_rad), 0],
            [0, math.sin(angulo_rad), math.cos(angulo_rad), 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
    elif eje == 'y':
        rotacion = np.array([
            [math.cos(angulo_rad), 0, math.sin(angulo_rad), 0],
            [0, 1, 0, 0],
            [-math.sin(angulo_rad), 0, math.cos(angulo_rad), 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
    elif eje == 'z':
        rotacion = np.array([
            [math.cos(angulo_rad), -math.sin(angulo_rad), 0, 0],
            [math.sin(angulo_rad), math.cos(angulo_rad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
        
        global direccion_nave
        cos_a = math.cos(angulo_rad)
        sin_a = math.sin(angulo_rad)
            
        # Actualiza el vector de dirección en función del ángulo de rotación
        nueva_direccion = np.array([
            direccion_nave[0] * cos_a - direccion_nave[1] * sin_a,
            direccion_nave[0] * sin_a + direccion_nave[1] * cos_a,
            direccion_nave[2]
        ])
            
        direccion_nave = nueva_direccion
        
    # Aplica la matriz de rotación
    glMultMatrixf(rotacion)
    
    glTranslatef(px, py, pz)

def escalar_nave_al_punto(escalar, punto=(0, 0, 0)): 
    px, py, pz = punto
    
    #la nave al origen
    glTranslatef(-px, -py, -pz)
    # Matriz de escalado
    escalado = np.array([
        [escalar, 0, 0, 0],
        [0, escalar, 0, 0],
        [0, 0, escalar, 0],
        [0, 0, 0, 1]
    ], dtype=np.float32)
    
    glMultMatrixf(escalado)
    glTranslatef(px, py, pz)


def Shearing_nave(eje, S_x, S_y, S_z):
    if eje == 'x':
        shear_matrix = np.array([
            [1, 0, 0, 0],
            [S_z, 1, 0, 0],
            [S_y, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
        glMultMatrixf(shear_matrix)
    elif eje == 'y':
        shear_matrix = np.array([
            [1, S_x, 0, 0],
            [0, 1, 0, 0],
            [0, S_y, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
        glMultMatrixf(shear_matrix)
    elif eje == 'z':
        shear_matrix = np.array([
            [1, 0, S_x, 0],
            [0, 1, S_z, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float32)
        glMultMatrixf(shear_matrix)

def draw_floor():
    tile_size = 5.0  # Tamaño de cada cuadro del piso de ajedrez
    grid_size = 10   # Número de cuadros por lado (ajustable)

    # Empezar el ciclo para crear los cuadros
    for i in range(-grid_size, grid_size):
        for j in range(-grid_size, grid_size):
            # Alternar color
            if (i + j) % 2 == 0:
                glColor3f(1.0, 1.0, 1.0)  # Blanco
            else:
                glColor3f(0.0, 0.0, 0.0)  # Negro

            # Dibujar cada cuadro del piso
            glBegin(GL_QUADS)
            glVertex3f(i * tile_size, j * tile_size, -5.0)
            glVertex3f((i + 1) * tile_size, j * tile_size, -5.0)
            glVertex3f((i + 1) * tile_size, (j + 1) * tile_size, -5.0)
            glVertex3f(i * tile_size, (j + 1) * tile_size, -5.0)
            glEnd()
    
def main():
    # Configuración de la ventana de Pygame
    pygame.init()
    display = (800, 680)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -15, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

    # Variables de control
    angulo_giro = 'z'
    angulo_reflexion = 'z'
    angulo_nave = 0 
    velocidad_giro = 1
    forma_nave = 0 
    velocidad_shearing = 0.1
    escalar = 1.0
    velocidad_escalado = 0.1
    
    simetria_ON = 0
    origen_ON = False
    run = True 
    initial_viewMatrix = np.copy(viewMatrix)
    Estrella_position = [1.5, 0, 0]
    punto = (0, 0, 0)
    
    while run:  # Usamos `run` como condición para el bucle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Salimos del bucle al cerrar la ventana
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False  # Salimos del bucle al presionar ESC o ENTER
                if event.key == pygame.K_g:
                    simetria_ON = not simetria_ON
                if event.key == pygame.K_r:
                    viewMatrix = np.copy(initial_viewMatrix)
                if event.key == pygame.K_p:
                    if punto == (0, 0, 0):
                        punto = (2, 3, 4)
                    else:
                        punto = (0, 0, 0)
                        
                if event.key == pygame.K_o: 
                    origen_ON = not origen_ON
                # Aumentar o Reducir el escalado  
                if event.key == pygame.K_PLUS:
                    escalar += velocidad_escalado
                if event.key == pygame.K_MINUS:
                    escalar -= velocidad_escalado   
                if event.key == pygame.K_LCTRL:
                    balas.append(Bala(Estrella_position[0], Estrella_position[2], Estrella_position[1], direccion_nave))
                    
        keypress = pygame.key.get_pressed()
        
        
        glLoadIdentity()
        # init the view matrix
        glPushMatrix()
        
    
        # Movimiento Giratorio EJE's 
        if keypress[pygame.K_w]:  
            Estrella_position[2] += 0.1
        if keypress[pygame.K_s]:  
            Estrella_position[2] -= 0.1
        if keypress[pygame.K_a]: 
            Estrella_position[0] -= 0.1
        if keypress[pygame.K_d]: 
            Estrella_position[0] += 0.1
        if keypress[pygame.K_SPACE]: 
            Estrella_position[1] += 0.1
        if keypress[pygame.K_LSHIFT]:  
            Estrella_position[1] -= 0.1
            
        # Aumentar o Reducir el giro
        if keypress[pygame.K_q]:
            angulo_nave += velocidad_giro
        if keypress[pygame.K_e]:
            angulo_nave -= velocidad_giro
        
        # Aumentar o Reducir el shear
        if keypress[pygame.K_h]:
            forma_nave += velocidad_shearing
        if keypress[pygame.K_j]:
            forma_nave -= velocidad_shearing
    
        # Eje de rotación 
        if keypress[pygame.K_1]:
            angulo_giro = 'x'
        if keypress[pygame.K_2]:
            angulo_giro = 'y'
        if keypress[pygame.K_3]:
            angulo_giro = 'z'
            
        # Eje de Simetria
        if keypress[pygame.K_4]:
            angulo_reflexion = 'x'
        if keypress[pygame.K_5]:
            angulo_reflexion = 'y'
        if keypress[pygame.K_6]:
            angulo_reflexion = 'z'
        
        if escalar < 0.1:  
            escalar = 0.1
        if escalar > 5.0:  
            escalar = 5.0
            
        
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #Sección sin movimiento
        draw_floor()
        dibujar_esfera2()
        
        
        #Sección con movimiento
        glPushMatrix()
        if origen_ON:
            escalar_nave_al_punto(escalar, (0, 0, 0))
        else:
            escalar_nave_al_punto(escalar, (5, 5, 5))
        glTranslatef(Estrella_position[0], Estrella_position[2], Estrella_position[1])
        if angulo_giro == 'x':
            girar_nave_al_punto(angulo_nave, 'x', punto)
            Shearing_nave('x', forma_nave, forma_nave, forma_nave)
        if angulo_giro == 'z':
            girar_nave_al_punto(angulo_nave, 'z', punto)
            Shearing_nave('z', forma_nave, forma_nave, forma_nave)
        if angulo_giro == 'y':
            girar_nave_al_punto(angulo_nave, 'y', punto)
            Shearing_nave('y', forma_nave, forma_nave, forma_nave)
        actualizar_balas()     
        
        nave()

        if simetria_ON:
            # Plano XY
            if angulo_reflexion == 'x':
                glPushMatrix()
                glTranslatef(2, 0, 0)
                glScalef(-1, 1, 1)
                nave()
                glPopMatrix()
             # Plano XZ
            if angulo_reflexion == 'z':
                glPushMatrix()
                glTranslatef(0, -5, 0)
                glScalef(1, -1, 1)
                nave()
                glPopMatrix() 
            # Plano YZ
            if angulo_reflexion == 'y':
                glPushMatrix()
                glTranslatef(0, 0, -3)
                glScalef(1, 1, -1)
                nave()
                glPopMatrix() 
        
        glPopMatrix()
        
        
        pygame.display.flip()
        pygame.time.wait(10)
    pygame.quit()
    
if __name__ == "__main__":
    main()