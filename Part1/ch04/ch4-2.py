def f():
    """文字列を入力してもらって、表示

    Args:
        x : (any) : user input; into str type.
            
    Returns:
        None
    
    Note:
        例外処理をしていないので、予定外の動作を引き起こすことをしないでください。
    
    """
    x = input('なにか入力してください: ')
    x = str(x)
    print(x)

f()
