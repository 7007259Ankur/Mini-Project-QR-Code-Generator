import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,border=4,)
data=input("Enter the link which you want to convert to qrcode")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="pink",back_color="Darkblue")
img.save("chatgpt.png")
