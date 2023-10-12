import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 1000
ventana_alto = 700
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Blackjack")

# Cargar imágenes de cartas
cartas = []
for valor in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
    for palo in ['corazones', 'diamantes', 'picas', 'treboles']:
        imagen = pygame.image.load(f'{valor}{palo}.png')
        cartas.append((valor, palo, imagen))
        
        
# Cargar imágenes de cartas
cartas = []
for valor in ['2', '3', '4', '5', '6', '7', '8', '9', 'sota', 'caballo', 'rey', 'as']:  # Cambia los valores para las cartas españolas
    for palo in ['oros', 'copas', 'espadas', 'bastos']:  # Cambia los palos para las cartas españolas
        imagen = pygame.image.load(f'{valor}{palo}.png')
        cartas.append((valor, palo, imagen))

# Función para mostrar una carta en la ventana
def mostrar_carta(ventana, carta, x, y):
    ventana.blit(carta[2], (x, y))

# Repartir dos cartas a cada jugador
jugador = [random.choice(cartas), random.choice(cartas)]
crupier = [random.choice(cartas), random.choice(cartas)]

# Ciclo principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill((0, 128, 0))  # Fondo verde

    # Mostrar cartas de jugador y crupier
    mostrar_carta(ventana, jugador[0], 100, 100)
    mostrar_carta(ventana, jugador[0], 200, 200)
    mostrar_carta(ventana, crupier[1], 300, 300)
    mostrar_carta(ventana, crupier[1], 400, 400)

    pygame.display.update()