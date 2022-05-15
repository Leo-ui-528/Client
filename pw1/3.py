def byte(a):
    try:
        c = eval("str.encode(a, encoding='utf-8')")
    except SyntaxError:
        print('no')

byte('класс')
