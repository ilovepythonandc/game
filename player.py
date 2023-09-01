import pygame
import random
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        image = pygame.image.load("./assets/image/sprite.png")
        self.image_index = 0
        self.image_index_speed = 0
        self.facing = "up"
        self.sprint_count = 30
        self.max_healthy = 30
        self.healthy = 30
        self.coin = 0
        self.max_image_index_speed = 10
        self.images = {
            "down": [
                image.subsurface((0, 10, 10, 10)),
                image.subsurface((10, 10, 10, 10)),
                image.subsurface((20, 10, 10, 10)),
                image.subsurface((0, 20, 10, 10))
            ],
            "right": [
                image.subsurface((30, 10, 10, 10)),
                image.subsurface((40, 10, 10, 10)),
                image.subsurface((50, 10, 10, 10)),
                image.subsurface((10, 20, 10, 10))
            ],
            "left": [
                pygame.transform.flip(image.subsurface((30, 10, 10, 10)), 1, 0),
                pygame.transform.flip(image.subsurface((40, 10, 10, 10)), 1, 0),
                pygame.transform.flip(image.subsurface((50, 10, 10, 10)), 1, 0),
                pygame.transform.flip(image.subsurface((10, 20, 10, 10)), 1, 0)
            ],
            "up": [
                image.subsurface((60, 10, 10, 10)),
                image.subsurface((70, 10, 10, 10)),
                image.subsurface((80, 10, 10, 10)),
                image.subsurface((20, 20, 10, 10))
            ]
        }
        self.rect = self.image.get_rect(y=(self.game.wide-50)/2, x=(self.game.tall-50)/2)

    @property
    def image(self):
        image = self.images[self.facing][self.image_index]
        image = pygame.transform.scale(image, (50, 50))
        return image

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        presed_key = pygame.key.get_pressed()
        if presed_key[pygame.K_w]:
            if self.image_index_speed == self.max_image_index_speed:
                self.image_index_speed = 0
                if self.image_index < 2:
                    self.image_index += 1
                else:
                    self.image_index = 0
            else:
                self.image_index_speed += 1
            self.facing = "up"
        if presed_key[pygame.K_s]:
            if self.image_index_speed == self.max_image_index_speed:
                self.image_index_speed = 0
                if self.image_index < 2:
                    self.image_index += 1
                else:
                    self.image_index = 0
            else:
                self.image_index_speed += 1
            self.facing = "down"
        if presed_key[pygame.K_a]:
            if self.image_index_speed == self.max_image_index_speed:
                self.image_index_speed = 0
                if self.image_index < 2:
                    self.image_index += 1
                else:
                    self.image_index = 0
            else:
                self.image_index_speed += 1
            self.facing = "left"
        if presed_key[pygame.K_d]:
            if self.image_index_speed == self.max_image_index_speed:
                self.image_index_speed = 0
                if self.image_index < 2:
                    self.image_index += 1
                else:
                    self.image_index = 0
            else:
                self.image_index_speed += 1
            self.facing = "right"
        if presed_key[pygame.K_SPACE]:
            self.image_index = 3
        if presed_key[pygame.K_LCTRL]:
            self.healthy -= 1
        if not presed_key[pygame.K_w]:
            if not presed_key[pygame.K_a]:
                if not presed_key[pygame.K_s]:
                    if not presed_key[pygame.K_d]:
                        if not presed_key[pygame.K_SPACE]:
                            self.image_index = 0
