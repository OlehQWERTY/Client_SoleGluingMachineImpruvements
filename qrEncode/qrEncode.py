# sudo pip3 install qrcode

import qrcode
import qrcode.image.pil

qr = qrcode.QRCode(version=4, box_size=3*4, border=5)
qr.add_data("Hello World")
img = qr.make_image(image_factory=qrcode.image.pil.PilImage)
small_img = img.crop( (0, 0, 512, 512) )
small_img.save("qrcode_512x512.bmp")