# import qrcode as qr 

# img = qr.make("https://www.youtube.com/channel/UC4iHhzV9g8guRGS-Z_c4JRQ")
# img.save("CinemaChamp_youtube.png")



import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.youtube.com/channel/UC4iHhzV9g8guRGS-Z_c4JRQ')
qr.make(fit=True)

img = qr.make_image(fill_color="grey", back_color="green")
img.save("CinemaChamp_you.png")