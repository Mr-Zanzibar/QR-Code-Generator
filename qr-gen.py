import pyqrcode
import io

link = input("URL: ")
url = pyqrcode.create(link)

url.svg('output.svg', scale=4)
buffer = io.Bytes.IO()
url.svg(buffer)
print("Done!")
