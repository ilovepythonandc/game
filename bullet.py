import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.facing = self.game.player.facing
        self.roto = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(x=self.game.player.rect.x, y=self.game.player.rect.y)

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        preesed_key = pygame.key.get_pressed()
        if preesed_key[pygame.K_d] and not self.game.screen_row >= self.game.max_screen_row and self.game.player.in_rect_right:
            self.rect.move_ip(-5, 0)
        if preesed_key[pygame.K_a] and not self.game.screen_row <= 0 and self.game.player.in_rect_left:
            self.rect.move_ip(5, 0)
        if self.facing == 0:
            self.rect.move_ip(7, 0)
        if self.facing == 1:
            self.rect.move_ip(-7, 0)
        if self.roto >= -360:
            self.roto -= 3
        else:
            self.roto = 0
        if self.rect.x >= self.game.Weight or self.rect.x <= -self.game.Weight:
            self.kill()

    @property
    def image(self):
        image = pygame.image.load("./assets/image/sprite.png").convert_alpha().subsurface((60, 11, 9, 8))
        image = pygame.transform.rotate(image, self.roto)
        image = pygame.transform.scale(image, (45, 40))
        image = pygame.transform.flip(image, self.facing, 0)
        return image
