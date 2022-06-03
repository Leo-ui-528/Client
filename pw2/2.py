import json

orders = {'orders': (
    'item:', 'intel',
    'quantity:', '5',
    'price:', '100000',
    'buyer:', 'asgard',
    'date:', '11.08.886'
)}


def write_order_to_json(o):
    with open('orders.json', 'w', encoding='utf-8') as f_n:
        json.dump(o, f_n, indent=4, skipkeys=True)


write_order_to_json(orders)
