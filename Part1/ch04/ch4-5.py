def str_to_float():
    try:
        x = input("数字を入力してください: ")
        y = float(x)
        print(y)
        return y
    except(TypeError,ValueError):
        print("数字以外を入力しないでください。プログラムを終了します。 ")
        
z = str_to_float()
print(z+z+z+z+z)