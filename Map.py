import pygame
class Floor(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.speed = 5
        self.image = pygame.image.load("./assets/image/background.png")
        self.rect = self.image.get_rect()

    def update(self):
        presed_key = pygame.key.get_pressed()
        if presed_key[pygame.K_w]:
            self.rect.move_ip(0, self.speed)
        if presed_key[pygame.K_s]:
            self.rect.move_ip(0, -self.speed)
        if presed_key[pygame.K_a]:
            self.rect.move_ip(self.speed, 0)
        if presed_key[pygame.K_d]:
            self.rect.move_ip(-self.speed, 0)
        if presed_key[pygame.K_SPACE]:
            self.speed = 7
        else:
            self.speed = 5
    def draw(self):
        self.game.screen.blit(self.image, self.rect)

