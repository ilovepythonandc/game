import pygame
class Time_machine(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        image = pygame.image.load("./assets/image/sprite.png")
        self.image_index = 0
        self.stauts = "start"
        self.image_index_speed = 0
        self.images = {
            "start": [
                image.subsurface((0, 40, 30, 29)),
                image.subsurface((30, 40, 30, 29)),
                image.subsurface((60, 40, 30, 29)),
                image.subsurface((90, 40, 30, 29)),
                image.subsurface((120, 40, 30, 29)),
                image.subsurface((150, 40, 30, 29)),
                image.subsurface((0, 70, 30, 29)),
                image.subsurface((30, 70, 30, 29)),
                image.subsurface((60, 70, 30, 29)),
                image.subsurface((90, 70, 30, 29)),
                image.subsurface((120, 70, 30, 29)),
                image.subsurface((150, 70, 30, 29)),
                image.subsurface((0, 100, 30, 29)),
                image.subsurface((30, 100, 30, 29)),
                image.subsurface((60, 100, 30, 29)),
                image.subsurface((90, 100, 30, 29)),
                image.subsurface((60, 100, 30, 29)),
                image.subsurface((90, 100, 30, 29)),
                image.subsurface((60, 100, 30, 29)),
                image.subsurface((90, 100, 30, 29)),
                image.subsurface((60, 100, 30, 29)),
                image.subsurface((90, 100, 30, 29)),
                image.subsurface((60, 100, 30, 29)),
                image.subsurface((90, 100, 30, 29)),
                image.subsurface((60, 100, 30, 29)),
                image.subsurface((90, 100, 30, 29)),
                image.subsurface((120, 100, 30, 29)),
                image.subsurface((150, 100, 30, 29)),
                image.subsurface((0, 130, 30, 29)),
                image.subsurface((30, 130, 30, 29)),
                image.subsurface((60, 130, 30, 29)),
            ]
        }
        self.rect = self.image.get_rect()
    @property
    def image(self):
        image = pygame.transform.scale(self.images[self.stauts][self.image_index], [30*10, 29*10])
        return image

    def update(self):
        if self.stauts == "start":
            if self.image_index_speed == 0:
                self.image_index_speed = 5
                if self.image_index < 30:
                    self.image_index += 1
                else:
                    self.image_index = 0
            else:
                self.image_index_speed -= 1
        pk = pygame.key.get_pressed()
        if pk[pygame.K_w]:
            self.rect.move_ip(0, 5)
        if pk[pygame.K_s]:
            self.rect.move_ip(0, -5)
        if pk[pygame.K_a]:
            self.rect.move_ip(5, 0)
        if pk[pygame.K_d]:
            self.rect.move_ip(-5, 0)

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
