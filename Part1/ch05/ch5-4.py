# ch5-3's dic
dic_me={
    'height':165,
    'color':'red',
    'artist':'桜野みねね'
}

def get_value():
    key = input('Keyを入力してください: ')
    if key in dic_me:
        value = dic_me[key]
        print(value)
    else:
        print("keyを正しく入力してください。")

get_value()