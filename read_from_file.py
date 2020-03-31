import Grid

def read_game_file1():
        with open('game_file.txt') as f:
            #w = [int(x) for x in next(f).split()]
            array = [[int(x) for x in line.split()] for line in f]
            return array


def read_game_file2():
        with open('game_file1.txt') as f:
            #w = [int(x) for x in next(f).split()]
            array = [[int(x) for x in line.split()] for line in f]
            return array
def read_game_file3():
        with open('game_file2.txt') as f:
            #w = [int(x) for x in next(f).split()]
            array = [[int(x) for x in line.split()] for line in f]
            return array
