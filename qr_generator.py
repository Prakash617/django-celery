import qrcode

# Define the data that you want to encode in the QR code
data = "https://www.example.com"

# Create a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Add the data to the QR code instance
qr.add_data(data)

# Compile the data into a QR code matrix
qr.make(fit=True)

# Create an image from the QR code matrix
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")
# img.show()
