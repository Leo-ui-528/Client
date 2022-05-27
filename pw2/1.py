import chardet
import csv
import re


def get_data():
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    main_data = []
    for i in range(1, 4):
        with open(f"info_{i}.txt", 'rb') as file_obj:
            data_bytes = file_obj.read()
            result = chardet.detect(data_bytes)
            data = data_bytes.decode(result['encoding'])

        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        list_1.append(os_prod_reg.findall(data)[0].split()[2])

        os_name_reg = re.compile(r'Windows:\s*\S*')
        list_2.append(os_name_reg.findall(data)[0])

        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        list_3.append(os_code_reg.findall(data)[0].split()[2])

        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        list_4.append(os_type_reg.findall(data)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип ситемы']
    main_data.append(headers)

    data_for_rows = [list_1, list_2, list_3, list_4]

    for idx in range(len(data_for_rows[0])):
        line = [row[idx] for row in data_for_rows]
        main_data.append(line)
    return main_data


def write_to_csv(out_file):
    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)


write_to_csv('data_report.csv¶')
