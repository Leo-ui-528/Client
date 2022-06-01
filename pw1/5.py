import chardet
import subprocess
import platform
import locale

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2',  'youtube.com']

process = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in process.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
ar = ['ping', param, '2',  'ya.ru']
process = subprocess.Popen(ar, stdout=subprocess.PIPE)
for line in process.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

default_encoding = locale.getpreferredencoding()
print(default_encoding)