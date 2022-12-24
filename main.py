from PIL import Image
from pyzbar.pyzbar import decode
from intractor import QRDecoder

qr = QRDecoder('qrcode.png')

decoded_data = qr.decoder()

decoded_resp = qr.get_decoded_response(decoded_data)

print(decoded_resp)