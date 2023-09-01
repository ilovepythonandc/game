import pygame
class Mouse(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.preesed = 0
        image = pygame.image.load("./assets/image/sprite.png")
        self.images = [
            image.subsurface((50, 30, 10, 10)),
            image.subsurface((60, 30, 10, 10))
        ]
        self.image_index = 0
        self.rect = self.image.get_rect()

    @property
    def image(self):
        image = self.images[self.image_index]
        image = pygame.transform.scale(image, (45, 45))
        image = image.convert_alpha()
        return image

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.preesed = pygame.mouse.get_pressed()[0]
        be_collide = pygame.sprite.spritecollide(self, self.game.buttons, 0)
        if be_collide:
            self.image_index = 1
            if self.preesed:
                for be_once in be_collide:
                    be_once.next()
        else:
            self.image_index = 0
class Pause_button(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        image = pygame.image.load("./assets/image/sprite.png")
        self.image = pygame.transform.scale(image.subsurface((20, 30, 10, 10)), (60, 60))
        self.rect = self.image.get_rect(x=self.game.tall-60)

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def next(self):
        self.game.pause.play()
        if self.game.status == self.game.advance:
            self.game.status = self.game.paass
            self.rect.x = (self.game.tall - 45) / 2
            self.rect.y = (self.game.wide - 45) / 2
        elif self.game.status == self.game.paass:
            self.game.status = self.game.advance
            self.rect.x = self.game.tall - 60
            self.rect.y = 0

class Mind_block:
    def __init__(self, game):
        self.game = game
        self.cout = 0
        self.low_heal = pygame.mixer.Sound("./assets/sound/lowheal.ogg")
        self.cout2 = 0
        self.cout3 = 36
        self.green = 0
        self.red = 255
        self.rect = self.image.get_rect()

    @property
    def image(self):
        if self.game.player.healthy >= self.game.player.max_healthy/2-4:
            self.green = 255
            self.red = 0
        else:
            if self.cout3 != 0:
                self.cout3 -= 1
            else:
                self.cout3 = 36
                self.low_heal.play()
            if self.cout != 10:
                self.cout += 1
                self.red = 255
                self.green = 0
            elif self.cout2 != 10:
                self.green = 255
                self.red = 0
                self.cout2 += 1
            else:
                self.cout = 0
                self.cout2 = 0
        image = self.game.font.render("healthy:{}".format(self.game.player.healthy), False, (self.red, self.green, 0))
        return image

    def draw(self):
        self.game.screen.blit(self.image, self.rect)



class Coin_block:
    def __init__(self, game):
        self.game = game
        self.cout = 0
        self.cout2 = 0
        self.red = 255
        self.green = 0
        self.rect = self.image.get_rect(x=300)

    @property
    def image(self):
        if self.game.player.coin == 0:
            if self.cout != 10:
                self.cout += 1
                self.red = 255
                self.green = 0
            elif self.cout2 != 10:
                self.green = 255
                self.red = 0
                self.cout2 += 1
            else:
                self.cout = 0
                self.cout2 = 0
        image = self.game.font.render("coins:{}".format(self.game.player.coin), False, (0, self.red, self.green))
        return image

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
