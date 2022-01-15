numbers = [1, 2, 3, 4, 5]

"""
数字当てゲーム
以下をほとんど参考にした
https://github.com/calthoff/tstp/blob/master/part_I/loops/challenges/chap7_challenge4.py

"""
while True:
    answer = input('Guess Number, or type "Q" to quit: ')

    if answer == 'q':
        break

    try:
        answer = int(answer)
    except ValueError:
        print('Q to quit')

    if answer in numbers:
        print('good')
    else:
        print('not good')
