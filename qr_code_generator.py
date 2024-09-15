import qrcode

user_data = input("Enter the text or URL: ").strip()
file_name = input("Enter the filename: ").strip()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(user_data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(file_name)
print(f'QR code saved as {file_name}')
