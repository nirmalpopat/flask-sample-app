from PIL import Image
from pyzbar.pyzbar import decode

class QRDecoder:
    
    def __init__(self, image):
        self.image = image
    
    def decoder(self):
        img = Image.open(self.image)
        return decode(img)
        
    def get_decoded_response(self, decoded_data):
        response = []
        for data in decoded_data:
            temp = {}
            
            # Used decode method to convert byte to string
            temp[data.data.decode()] = {
                'position': [data.polygon[0][0], data.polygon[0][1], data.polygon[2][0], data.polygon[2][1]]
            }
            response.append(temp)
        return response