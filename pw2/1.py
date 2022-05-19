import csv
from chardet import detect
import re


# def write_to_csv():
#     with open('write.csv', 'w') as f_n:
#         f_n_writer = csv.writer(f_n)
#     for row in info:
#         f_n_writer.writerow(row)


info = 'info_1.txt', 'info_2.txt', 'info_3.txt'


def get_data(i):
    for i in info:
        with open(i, 'rb') as f:
            content = f.read()
        encoding = detect(content)['encoding']
        # print('encoding: ', encoding)

        with open(i, encoding=encoding) as f_n:
            for el_str in f_n:
                print(el_str, end='')


list_1 = []
list_2 = []
list_3 = []
list_4 = []

main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

for file in info:
    datafile = open(file)
    for row in datafile:
        row = row.rstrip()
        if re.match('Изготовитель системы', row):
            list_1.append(re.search(r'(Изготовитель системы).\s*(.*)', row).group(2))
        elif re.match('Название ОС', row):
            list_2.append(re.search(r'(Название ОС).\s*(.*)', row).group(2))
        elif re.match('Код продукта', row):
            list_3.append(re.search(r'(Код продукта).\s*(.*)', row).group(2))
        elif re.match('Тип системы', row):
            list_4.append(re.search(r'(Тип системы).\s*(.*)', row).group(2))

# def write_to_csv():
#     with open('write.csv', 'w') as f_n:
#         f_n_writer = csv.writer(f_n)
#     for row in info:
#         f_n_writer.writerow(row)
# print(get_data(info))

print(list_1)
print(list_2)
print(list_3)
print(list_4)
