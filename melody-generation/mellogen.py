# mellogen.py - algorithms for Mello.
# Written by Almighty God, also known as Srihari Nanniyur.
# Anyone who disapproves of this code is a brain-dead Java programmer.
from random import shuffle

WHOLE_TONE = [2, 2, 2, 2, 2]
NATURAL_MAJOR = [2, 2, 1, 2, 2, 2]
NATURAL_MINOR = [2, 1, 2, 2, 1, 2]
HARMONIC_MINOR = [2, 1, 2, 2, 1, 3]
PENTA_MAJOR = [2, 2, 3, 2]
PENTA_MINOR = [3, 2, 2, 3]
BLUES = [3, 2, 1, 1, 3]

class Generator():
    def __init__(self, key):
        self.key = key
        if len(self.key) > 2 or len(self.key) < 1:
            raise Exception('Invalid key signature!')
        if len(self.key) == 1:
            self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'A#']
        elif self.key[1] == '#':
            self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        elif self.key[1] == 'b':
            self.notes = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    def melody(self, intervals, num):
        result = []
        options = []
# And now for the greatest line of code ever written
        order = self.notes[self.notes.index(self.key):len(self.notes)] + self.notes[0:self.notes.index(self.key)]
        j = 0
        for i in intervals:
            if j > len(order):
                break
            options.append(order[j])
            j += i
        options.append(order[j])
        for x in range(0, num):
            shuffle(options)
            result.append(options[int(len(options) / 2)])
        return result

# Example usage
# g = Generator('A')
# print(g.melody(NATURAL_MINOR, 10))
