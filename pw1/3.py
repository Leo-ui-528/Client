def byte(a):
    try:
        c = eval('"b"+a')
    except SyntaxError:
        print('no')


byte('класс')