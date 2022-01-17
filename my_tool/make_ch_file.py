x=input('chpter?  ')
y=int(input('section?  '))
# test="ch{}-{}.py".format(x,y)
# print(test)

for i in range(y):
    test="ch{}-{}.py".format(x,i+1)
    print(test)