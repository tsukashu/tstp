numbers = [1,2,3,4,5]

"""
数字当てゲーム

TODO
本当は無限ループのはずなので、ループの条件を見直す


1. 数字は予め決めておく
2. 数字以外を入力するとErrorになる→"終わりにするか？"と聞かれる
3. そこで→Qを入力すると終わる
4. 最後まで正解できない、あるいは数字以外を入力し続けると終わる

"""
while True:
    
    answer = input('Guess Number: ')
    
    try:
        answer = int(answer)
    except ValueError:
        print('Type Number or "Q" to quit')
        quit = input('quit the game?: ')
    if quit == 'q':
        break
        
    if answer in numbers:
        print('ok')
        break
    else:
        print('no good')
        break

        






