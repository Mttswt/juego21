import pygame
import random
import sys
from carta import *
from juego import Juego

# Initialize Pygame
pygame.init()

# Configuration for the window
ventana_ancho = 1000
ventana_alto = 700
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Blackjack")

# Tamaño fijo para las imágenes de las cartas
carta_ancho = 100
carta_alto = 150

# Load card images
def cargar_cartas(mazo):
    cartas = []
    for valor, palo in mazo:
        imagen = pygame.image.load(f'{valor}{palo}.png')
        imagen = pygame.transform.scale(imagen, (carta_ancho, carta_alto))  # Ajustar tamaño
        cartas.append((valor, palo, imagen))
    return cartas

# Define the French and Spanish decks
mazo_frances = [(str(x), p) for x in range(2, 11) for p in ['corazones', 'diamantes', 'picas', 'treboles']] + \
               [('A', p) for p in ['corazones', 'diamantes', 'picas', 'treboles']] + \
               [('J', p) for p in ['corazones', 'diamantes', 'picas', 'treboles']] + \
               [('Q', p) for p in ['corazones', 'diamantes', 'picas', 'treboles']] + \
               [('K', p) for p in ['corazones', 'diamantes', 'picas', 'treboles']]

mazo_espanol = [(str(x), p) for x in range(2, 8) for p in ['oros', 'copas', 'espadas', 'bastos']] + \
               [('as', p) for p in ['oros', 'copas', 'espadas', 'bastos']] + \
               [('sota', p) for p in ['oros', 'copas', 'espadas', 'bastos']] + \
               [('caballo', p) for p in ['oros', 'copas', 'espadas', 'bastos']] + \
               [('rey', p) for p in ['oros', 'copas', 'espadas', 'bastos']]

# Function to display a card on the window
def mostrar_carta(ventana, carta, x, y):
    ventana.blit(carta[2], (x, y))

# Function to let the player choose the deck
def seleccionar_mazo():
    font = pygame.font.Font(None, 36)
    texto = font.render("Selecciona un mazo:", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(ventana_ancho // 2, ventana_alto // 2 - 50))

    boton_frances = pygame.Rect(ventana_ancho // 2 - 100, ventana_alto // 2 + 50, 200, 50)
    boton_espanol = pygame.Rect(ventana_ancho // 2 - 100, ventana_alto // 2 + 150, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_frances.collidepoint(event.pos):
                    return mazo_frances
                elif boton_espanol.collidepoint(event.pos):
                    return mazo_espanol

        ventana.fill((0, 128, 0))  # Fondo verde

        pygame.draw.rect(ventana, (0, 0, 255), boton_frances)
        pygame.draw.rect(ventana, (0, 0, 255), boton_espanol)
        ventana.blit(texto, texto_rect)

        font = pygame.font.Font(None, 48)
        texto_frances = font.render("Mazo Francés", True, (255, 255, 255))
        texto_espanol = font.render("Mazo Español", True, (255, 255, 255))
        ventana.blit(texto_frances, (ventana_ancho // 2 - 60, ventana_alto // 2 + 60))
        ventana.blit(texto_espanol, (ventana_ancho // 2 - 65, ventana_alto // 2 + 160))

        pygame.display.update()

# Select the deck
mazo_seleccionado = seleccionar_mazo()
cartas = cargar_cartas(mazo_seleccionado)

# Create a Juego instance
juego = Juego(mazo_seleccionado)
juego.iniciar_juego()

# Main game loop
jugador = juego.jugador2.cartas  # Player's cards
crupier = juego.jugador1  # AI's cards

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill((0, 128, 0))  # Fondo verde

    # Display player's cards
    mostrar_carta(ventana, jugador[0], 100, 100)
    mostrar_carta(ventana, jugador[1], 200, 100)

    # Display AI's cards
    crupier.mostrar_cartas_enemigo(ventana, 300, 100)

    # Check game outcome (win, lose, or tie)
    resultado = juego.valorar_juego()
    if resultado == "Jugador gana":
        print("¡Jugador gana!")
    elif resultado == "Casa gana":
        print("¡Casa gana!")
    elif resultado == "Empate":
        print("¡Es un empate!")

    pygame.display.update()
