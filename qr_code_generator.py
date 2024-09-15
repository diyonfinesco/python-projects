import qrcode

user_input = input("Enter the text or URL: ").strip()
file_name = input("Enter the filename: ").strip()

img = qrcode.make(user_input)
img.save(file_name)
