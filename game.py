from random import choice

class Game:

    def __init__(self):
        self.lives = 6
        self.correct_letters = []
        self.incorrect_letters = []
        self.words = ['javascript', 'django', 'python']
        self.letter = ''
        self.word = ''

    def select_word(self, words):
        self.word = choice(words)
        return self.word

    def choose_letter(self):
        correct_letter = False
        while not correct_letter:
            self.letter = input('Choose a letter:\n').lower()
            if len(self.letter) != 1:
                print('Choose only one letter or do not leave it blank!')
            elif not self.letter.isalpha():
                print('You can only write letters!')
            elif self.letter in self.correct_letters or self.letter in self.incorrect_letters:
                print('You have already called this letter! Choose another!')
            else:
                correct_letter = True
        return self.letter

    def check_letter(self, letter, word):
        if letter in word:
            print('\nWell done!')
            self.correct_letters.append(letter)
        else:
            self.lives -= 1
            print(f'\nThe word does not contain this letter.\nYou have {self.lives} lives left!')
            self.incorrect_letters.append(letter)

    def game_graphics(self):
        graphics = []
        for letter in self.word:
            if letter in self.correct_letters:
                graphics.append(letter)
            else:
                graphics.append('_')
        print("".join(graphics) + '\n')
        return graphics

play = Game()
play.word = play.select_word(play.words)
length = len(play.word)

print(f'''\nWelcome to the Hangman game!!! Let's start!!!\n
The word is composed of {length} letters\n''')
spacing = '*' * 50 + '\n'
print(spacing)

while play.lives > 0:
    play.letter = play.choose_letter()
    play.check_letter(play.letter, play.word)
    game_progress = play.game_graphics()
    print(spacing)

    if "".join(game_progress) == play.word:
        print('Congratulations! You have guessed the word!!!')
        break
else:
    print(f'Game over! The hidden word was "{play.word}"!')

