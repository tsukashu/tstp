"""
TODO
単語をランダムなリストから選ぶように変更

Note
Calthoff氏(Github)は`random.randint`を使っていた。
おそらく本の内容に合わせたのだと思うが、よりシンプルな`random.choice`を使った。
`random.randint`を使って、かつ、リストの個数を`len`で取得するとか

testcode

import random

wlist = ["Python", "", "computer", "", ""]

wcount = len(wlist)-1       # 個数は1、インデックスは0から始まるため-1する
rnumber = random.randint(0, wcount) # リスト個数の範囲内でランダムな数値が得られる
rword = wlist[rnumber]      # 変数に代入して、メインの関数に渡す
"""
import random

word_list = [
    'cat',
    'dog',
    'bird',
    'penguin',
    'lion',
    'monkey',
    'human',
    'superultrahypermiracleromantic',
]

rword = (random.choice(word_list))


def hangman(rword):
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ",
              "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(rword)
    letter_board = ["__"] * len(rword)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(rword))


hangman(rword)
