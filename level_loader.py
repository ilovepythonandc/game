from pygame.sprite import Group
import Map
def load_level(game, castle, level):
    if castle > 0 and castle < 6:
        if level > 0 and level < 6:
            with open("./assets/data/castle{0}/level{1}.x".format(castle, level)) as level_file:
                level_data = level_file.read()
            level = Group()
            x = 0
            y = 0
            for i in range(level_data):
                if i == "x":
                    level.add(Map.Floor(game, x, y))
                if i == "\n":
                    y += 5
                x += 5
    del level_file, level_data
    return level
