import yaml

a = {'by': ['44', '67'], 'quantity': 5, 'date': {'march': '35€'}}

with open('file.yaml', 'w') as f_n:
    yaml.dump(a, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as f:
    content = yaml.load(f)

print(content)


if content == f_n:
    print('ok')
else:
    print('no')
