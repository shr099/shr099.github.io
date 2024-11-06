import pygame

class Cubo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 60
        self.alto = 60
        self.velocidad = 3
        self.color = "red"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        self.imagen = pygame.image.load("Juego_tik_tok/gotita-removebg-preview.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.imagen = pygame.transform.rotate(self.imagen, 0)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        # pygame.draw.rect(ventana,self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))