import qrcode
from PIL import Image

def generateQR(contenido):
    #img = qrcode.make('QR Code')
    img = qrcode.make()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(contenido)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    img.save("imagen.png")
