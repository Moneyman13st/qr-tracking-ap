import qrcode

def create_qr():
    url = "http://127.0.0.1:5000/"  # Change this when deploying online
    qr = qrcode.make(url)
    qr.save("qr_code.png")
    print("✅ QR Code successfully saved as 'qr_code.png'!")  # Added print confirmation

create_qr()pip3 freeze > requirements.txt


