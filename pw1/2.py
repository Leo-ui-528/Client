def byte(a):
    c = eval("str.encode(a, encoding='utf-8')")
    print(f' {c} {type(c)}')


byte('class')
