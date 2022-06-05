Class color:
   UNDERLINE = '\033[4m'

import pyqrcode
import io
From colorama import init

link = input("URL: ")
url = pyqrcode.create(link)

url.svg('output.svg', scale=4)
buffer = io.Bytes.IO()
url.svg(buffer)
print(f' ')
print(color.UNDERLINE + f 'Done!')
print(f' ')
