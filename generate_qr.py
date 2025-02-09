import qrcode

def create_qr():
    url = "https://qr-tracking-ap-1.onrender.com"  # Change this when deploying online
    qr = qrcode.make(url)
    qr.save("qr_code.png")
    print("✅ QR Code successfully saved as 'qr_code.png'!")  # Added print confirmation

create_qr()


