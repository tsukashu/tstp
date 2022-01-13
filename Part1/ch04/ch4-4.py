x= 10
int(x)
def fx(x):
    """xを2で割って表示。

    Return: result

    Note:
    見たらわかるので、以下省略。
    """
    result = (x // 2)
    print(result)
    return result

fx(5)
y = fx(5)

y = int(y)
def fy(y):
    """yに4をかけて表示

    Note:
    見たらわかるので、以下省略。
    """
    result = y * 4
    print(result)

fy(y)