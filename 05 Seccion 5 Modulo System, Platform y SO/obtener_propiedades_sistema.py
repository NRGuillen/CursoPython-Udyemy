import platform
import sys
from locale import getlocale, getencoding

# platform

print(platform.system()) # Windows
print(platform.version()) # 10.0.26200
print(platform.python_version()) # 3.14.2
print(platform.processor()) # AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD
print(platform.uname()) # uname_result(system='Windows', node='DESKTOP-RLE4185', release='11', version='10.0.26200',
# machine='AMD64')

# sys

print(sys.version) # 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)]
print(sys.platform) # win32
print(sys.executable) # C:\Users\Ruben\AppData\Local\Programs\Python\Python314\python.exe
print(getlocale()) # ('es_ES', 'cp1252')
print(getencoding()) # cp1252
print(sys.getdefaultencoding()) # utf-8
print(sys.argv) # ['C:\\Users\\Ruben\\Desktop\\Curso Python\\Seccion 5 Modulo System, Platform y SO\\obtener_propied
# ades_sistema.py']

objeto = 'Hola que tal'

print(sys.getsizeof(objeto)) # 53, tamaño byte


