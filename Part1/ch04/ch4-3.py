def f(x,y,z,a=10,b=20):
    """必須引数と、オプション引数のサンプル

    3つの必須引数と、2つのオプション引数を表示、計算する。
    引数は予め指定する。

    Args:
        x, y, z (int)   : number.
        a, b (int)  : number. optional.
            
    Returns:
        None
    
    Note:
        例外処理をしていないので、予定外の動作を引き起こすことをしないでください。
    
    """
    print(x,y,z,a,b)
    print((x + y - z) * a // b)

f(1,2,3)

