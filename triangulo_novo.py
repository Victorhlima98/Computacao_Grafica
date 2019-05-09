import pygame
from pygame.locals import *
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "2000, 100"

res = 600


class Forma:
    meio = res / 2
    x_pos = 0
    y_pos = 0
    x = res // 12
    y = res // 6
    ax, ay = (0, -50)
    bx, by = (50, 50)
    cx, cy = (-50, 50)

    def cria_forma(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (self.meio, 0), (self.meio, res))
        pygame.draw.line(screen, (255, 255, 255), (0, self.meio), (res, self.meio))
        pygame.draw.polygon(screen, (255, 0, 0), [(self.ax + self.meio, self.ay + self.meio),
                                                  (self.bx + self.meio, self.by + self.meio),
                                                  (self.cx + self.meio, self.cy + self.meio),
                                                  ])
        pygame.display.flip()

    def teste(self):
        print('a', self.ax, self.ay,
              '\nb', self.bx, self.by,
              '\nc', self.cx, self.cy, '\n')

    def reset(self):
        self.ax, self.ay = (0, -50)
        self.bx, self.by = (50, 50)
        self.cx, self.cy = (-50, 50)

    def move_up(self):
        self.ay -= 10
        self.by -= 10
        self.cy -= 10

    def move_down(self):
        self.ay += 10
        self.by += 10
        self.cy += 10

    def move_right(self):
        self.ax += 10
        self.bx += 10
        self.cx += 10

    def move_left(self):
        self.ax -= 10
        self.bx -= 10
        self.cx -= 10

    def scale_up(self):
        self.ay += 10
        self.bx -= 5
        self.by -= 5
        self.cx += 5
        self.cy -= 5

    def scale_down(self):
        self.ay -= 10
        self.bx += 5
        self.by += 5
        self.cx -= 5
        self.cy += 5

    def rotate(self):
        maxx = max(self.ax, self.bx, self.cx)
        minx = min(self.ax, self.bx, self.cx)
        maxy = max(self.ay, self.by, self.cy)
        miny = min(self.ay, self.by, self.cy)
        x = (maxx + minx) // 2
        y = (maxy + miny) // 2
        print x, y

        self.ax, self.ay = (self.ax - x, self.ay - y)
        self.bx, self.by = (self.bx - x, self.by - y)
        self.cx, self.cy = (self.cx - x, self.cy - y)

        auxx, auxy = (self.ax, self.ay)
        self.ax, self.ay = (self.by, -self.bx)
        self.bx, self.by = (self.cy, -self.cx)
        self.cx, self.cy = (auxy, -auxx)

        self.ax, self.ay = (self.ax + x, self.ay + y)
        self.bx, self.by = (self.bx + x, self.by + y)
        self.cx, self.cy = (self.cx + x, self.cy + y)

    def espelhamento_x(self):
        self.ay = -self.ay
        self.by = -self.by
        self.cy = -self.cy

    def espelhamento_y(self):
        self.ax = -self.ax
        self.bx = -self.bx
        self.cx = -self.cx

    def espelhamento_xy(self):
        self.ax, self.ay = (-self.ax, -self.ay)
        self.bx, self.by = (-self.bx, -self.by)
        self.cx, self.cy = (-self.cx, -self.cy)

    def cisalhamento_a_plus(self):
        self.ay -= 10

    def cisalhamento_a_minus(self):
        self.ay += 10

    def cisalhamento_b_plus(self):
        self.bx += 5
        self.by += 5

    def cisalhamento_b_minus(self):
        self.bx -= 5
        self.by -= 5

    def cisalhamento_c_plus(self):
        self.cx -= 5
        self.cy += 5

    def cisalhamento_c_minus(self):
        self.cx += 5
        self.cy -= 5


def main():
    pygame.init()
    display = (res, res)
    screen = pygame.display.set_mode(display)

    forma = Forma()

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_SPACE:
                    forma.teste()
                elif event.key == K_RETURN:
                    forma.reset()
                elif event.key == K_w:
                    forma.move_up()
                elif event.key == K_s:
                    forma.move_down()
                elif event.key == K_d:
                    forma.move_right()
                elif event.key == K_a:
                    forma.move_left()
                elif event.key == K_q:
                    forma.scale_up()
                elif event.key == K_e:
                    forma.scale_down()
                elif event.key == K_r:
                    forma.rotate()
                elif event.key == K_1:
                    forma.espelhamento_x()
                elif event.key == K_2:
                    forma.espelhamento_y()
                elif event.key == K_3:
                    forma.espelhamento_xy()
                elif event.key == K_KP7:
                    forma.cisalhamento_a_plus()
                elif event.key == K_KP4:
                    forma.cisalhamento_a_minus()
                elif event.key == K_KP8:
                    forma.cisalhamento_b_plus()
                elif event.key == K_KP5:
                    forma.cisalhamento_b_minus()
                elif event.key == K_KP9:
                    forma.cisalhamento_c_plus()
                elif event.key == K_KP6:
                    forma.cisalhamento_c_minus()
        forma.cria_forma(screen)


if __name__ == '__main__':
    main()
