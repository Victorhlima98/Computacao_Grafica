import pygame
from pygame import *


def rotate(surface, rect, angle):
    new_image = pygame.transform.rotate(surface, angle)
    rect = new_image.get_rect(center=(rect[0]+(rect[2]//2), rect[1] + (rect[3] // 2)))
    return new_image, rect


def main():
    pygame.init()
    raio = 5
    xpos = 40
    ypos = 40
    tela = pygame.display.set_mode((600, 600))
    tela.fill((0, 0, 0))
    surface = pygame.Surface((xpos, ypos), pygame.SRCALPHA)
    surface.fill((0,255,0))
    rotated_surface = surface
    triangulo = [[0, 20], [40, 0], [40, 40]]
    pygame.draw.polygon(surface, (255, 0, 0), triangulo, raio)
    pygame.display.flip()
    rect = surface.get_rect(center=(300, 300))
    rot = 0  # variavel responsavel pela rotacao

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                tela.fill((0, 0, 0))
                if event.key == K_ESCAPE:
                    pygame.quit()
                elif event.key == K_KP6:
                    rect = (rect[0] + 5, rect[1])
                elif event.key == K_KP4:
                    rect = (rect[0] - 5, rect[1])
                elif event.key == K_KP2:
                    rect = (rect[0], rect[1] + 5)
                elif event.key == K_KP8:
                    rect = (rect[0], rect[1] - 5)
                elif event.key == K_KP5:
                    rot += 10
                    rotated_surface, rect = rotate(pygame.transform.scale(surface, (xpos, ypos)), rect, rot)
                elif event.key == K_KP9:
                    xpos += 20
                    ypos += 20
                    rotated_surface = pygame.transform.scale(surface, (xpos, ypos))
                elif event.key == K_KP7:
                    xpos -= 20
                    ypos -= 20
                    rotated_surface = pygame.transform.scale(surface, (xpos, ypos))

        tela.fill((0, 0, 0))
        pygame.draw.line(tela, (255, 255, 255), (300, 0), (300, 600))
        pygame.draw.line(tela, (255, 255, 255), (0, 300), (600, 300))
        tela.blit(rotated_surface, rect)  # renderiza objetos na tela
        pygame.display.update()


if __name__ == '__main__':
    main()
