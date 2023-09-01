import pygame
import sys
while pygame.get_init() == 0:
    pygame.init()

from player import Player
from rand import rand
from mixer import Mixer
from gui import *
from enemies import *
from level_loader import *

class Game:
    wide = 720
    tall = 1280

    main_menu = 1
    saves = 2
    advance = 3
    paass = 4
    def __init__(self):
        self.screen = pygame.display.set_mode((self.tall, self.wide))
        pygame.display.set_caption("millage castle")
        pygame.mouse.set_visible(0)
        self.rand = rand
        self.boss = Time_machine(self)
        self.mixer = Mixer(self)
        self.castle = 1
        self.level = 5
        self.pause = pygame.mixer.Sound("./assets/sound/pause.ogg")
        self.player = Player(self)
        self.buttons = pygame.sprite.Group()
        # self.buttons.add(Pause_button(self))
        self.mouse = Mouse(self)
        self.fps = 60
        self.status = self.main_menu
        self.font = pygame.font.Font("./assets/image/font.otf", 40)
        self.heal_text = Mind_block(self)
        self.coin_text = Coin_block(self)
        self.clock = pygame.time.Clock()

    def go_level(self):
        self.level = load_level()
        self.status = self.advance
        self.buttons.clear()
        self.buttons.add(Pause_button(self))
        if self.level != 5:
            self.mixer.reload("./assets/music/castle{0}.mp3".format(self.castle))
        else:
            self.mixer.reload("./assets/music/boss.mp3")

    def run(self):
        while True:
            self.game_logic()
            self.draw()
            self.update()

    def game_logic(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.fill("black")
        if self.status == self.advance:
            if self.castle == 1:
                self.screen.fill((50, 53, 50))
            if self.castle == 2:
                self.screen.fill((0, 0, 200))
            if self.castle == 3:
                self.screen.fill((0, 0, 0))
            if self.castle == 4:
                self.screen.fill((255, 255, 0))
            self.mixer.play()
            self.heal_text.draw()
            self.coin_text.draw()
            self.player.draw()
            if self.level == 5:
                self.boss.draw()
        if self.status == self.paass:
            self.mixer.stop()
        for button in self.buttons:
            button.draw()
        self.mouse.draw()


    def update(self):
        if self.status == self.advance:
            self.player.update()
        self.mouse.update()
        self.boss.update()
        pygame.display.update()
        self.clock.tick(self.fps)
if __name__ == "__main__":
    game = Game()
    game.run()
