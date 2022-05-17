def byte(a):
    enc = bytes(a, encoding='utf-8')
    print(enc)
    dec = bytes.decode(enc, encoding='utf-8')
    print(dec)


byte('разработка')
byte('администрирование')
byte('protocol')
byte('standard')

