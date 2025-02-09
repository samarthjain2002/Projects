import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


def encodeQR():
    data = input("Enter the data to be encoded: ")
    file_name = input("Enter the file name: ")

    qr = qrcode.QRCode(version = 1, box_size = 10, border = 50)
    qr.add_data(data)

    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")

    img.save(f"C:/Users/Admin/Git_hub/Projects/Python Projects/CLI Apps/QRCode Generator/qrcodes/{file_name}.png")

def decodeQR():
    file_name = input("Enter the filename of QRCode image: ")
    img = Image.open(f"C:/Users/Admin/Git_hub/Projects/Python Projects/CLI Apps/QRCode Generator/qrcodes/{file_name}.png")

    result = decode(img)
    if result:
        print(result)
    else:
        print("No QR Code found in the image.")


if __name__ == "__main__":
    print("1) Encode QR code")
    print("2) Decode QR code")
    choice = int(input("Select option: "))

    if choice == 1:
        encodeQR()
    elif choice == 2:
        decodeQR()