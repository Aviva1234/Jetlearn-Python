class Piano:
    def play(self):
        print('Beethoven')
class Violin:
    def play(self):
        print('Tchaikovsky')

instruments = [Piano(), Violin()]

for i in instruments:
    i.play()