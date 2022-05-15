from chardet import detect

out_f = open("test_file.txt", "w", encoding='cp1251')
str_list = ['Программирование\n', 'Сокет\n', 'Декоратор\n']
out_f.writelines(str_list)
out_f.close()

with open('test_file.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)

with open('test_file.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
    print()
