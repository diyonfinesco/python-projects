import qrcode

user_input = input("Enter the text or URL: ")
file_name = input("Enter the filename: ")

img = qrcode.make(user_input)
img.save(file_name)
