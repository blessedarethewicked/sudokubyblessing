import Grid

def read_game_file():
        with open('game_file.txt') as f:
            #w = [int(x) for x in next(f).split()]
            array = [[int(x) for x in line.split()] for line in f]
            return array
