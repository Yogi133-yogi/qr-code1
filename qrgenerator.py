import qrcode
import image
qr = qrcode.QRCode(
    version= 15,
    box_size= 10,
    border= 4,
)
data = "https://www.youtube.com/watch?v=TMY1g8pAktk"
 
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("test.png")


    