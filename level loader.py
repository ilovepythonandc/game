from pygame.sprite import Group
import Map
def load_level(castle, level):
    if castle > 0 and castle < 6:
        if level > 0 and level < 6:
            with open("./assets/data/castle{0}/level{1}.x".format(castle, level)) as level_file:
                level_data = level_file.read()
                del level_file
            level = Group()
            x = 0
            y = 0
            for i in range(level_data):
                if i == "x":
                    level.add(Sprite(x, y))
