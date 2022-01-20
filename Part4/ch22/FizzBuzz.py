def fizzbuzz(x, y):
    for i in range(x, y + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzbuzz(1, 100)
fizzbuzz(100, 150)
fizzbuzz(200, 50)  # TODO if x>=y, print error.
