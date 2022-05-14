def byte(a):
    c = eval('"b"+a')
    print(f'{type(c)}, {c}, {len(c)}')


byte('class')
