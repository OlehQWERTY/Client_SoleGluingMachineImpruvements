import base64
import numpy as np
import cv2

# encode = base64.b64encode(b'data 123')
# print(encode)

with open("1.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

# store to byte file and restore it
# f = open("2.jpg", "wb")
# f.write(encoded_string)
# f.close()

# with open("2.jpg", "rb") as image_file:
# 	encoded_string2 = image_file.read()
# img_str = base64.decodebytes(encoded_string2)

img_str = base64.decodebytes(encoded_string)

# cv byte img show
nparr = np.frombuffer(img_str, np.uint8)
img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1
cv2.imshow('image',img_np)

# cv wait untill ESC will be pressed
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()