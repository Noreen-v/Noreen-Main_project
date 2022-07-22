import pyqrcode
import png
from pyqrcode import QRCode
import random
number = random.randint(111111,999999)
print(number)
  
# String which represents the QR code
scode = str(number)
  
# Generate QR code
url = pyqrcode.create(scode)
  
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)

import base64

with open("myqr.png", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
print(b64_string)
print(b64_string.decode("utf-8") )