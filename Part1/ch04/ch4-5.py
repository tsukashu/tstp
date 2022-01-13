def str_to_float():
    """例外処理のサンプル

    入力から`Float`に変換する際のエラー処理を行う。

    想定されるエラー:
        文字列など数字以外→`ValueError`
        
    Return: 入力をFloatに変換したもの

    Note:
    テスト用の変数zが、関数がエラーだった場合空になるため`TypeErrorになる`
    """

    try:
        x = input("数字を入力してください: ")
        y = float(x)
        print(y)
        return y
    except(ValueError):
        print("数字以外を入力しないでください。プログラムを終了します。 ")
        
z = str_to_float()
print(z+z+z+z+z)