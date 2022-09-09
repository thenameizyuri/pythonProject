import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "https://www.raktimneupane.com.np/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("myqr.svg", scale=8)