def fxx():
    """数字を入力してもらって、2乗して表示

    user input number, and square.

    Args:
        x : (int) : user input number
        xx : (int) : the squared number
    
    Returns:
        None
    
    Note:
        例外処理をしていないので、数字以外の入力があるなど、
        予定外の動作を引き起こすことをしないでください。
    
    """
    x = input('数字を入力してください: ')
    x = int(x)
    xx = x ** 2
    print(xx)

fxx()

