import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprite Example")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        try:
            self.image = pygame.image.load(image_path)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        except pygame.error as e:
            print(f"Error loading image: {e}")

            self.image = pygame.Surface((50, 50))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def update(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5

        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    def draw(self, surface):
        surface.blit(self.image, self.rect)


all_sprites = pygame.sprite.Group()

import os

script_dir = os.path.dirname(__file__)
cuphead_path = os.path.join(script_dir, "cuphead.jpg")
sprite = CustomSprite(cuphead_path, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
all_sprites.add(sprite)


running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()


    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()