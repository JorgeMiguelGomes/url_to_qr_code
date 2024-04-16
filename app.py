#import libraries 
import qrcode

# Specify the URL for the QR code
url = "https://your.url.here"

# Create a QR Code instance 
qr = qrcode.QRCode(
    version=1,  # You can specify versions from 1 to 40 where higher numbers allow for more data
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,  # Default is 10. The bigger the number the larger the file
    border=4  # Border size in terms of boxes, you can increase if needed
)
qr.add_data(url)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("large_qr_code.png")
