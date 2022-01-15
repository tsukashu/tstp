import os

answer = input('How are you now??')
fname = os.path.join('Part1','ch09','Q&A.txt')

with open(fname,'w',encoding='utf-8') as file:
    file.write(answer)

with open(fname,'r',encoding='utf-8') as file:
    feel = file.read()
    
print(feel)