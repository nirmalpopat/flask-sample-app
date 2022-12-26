from PIL import Image
from pyzbar.pyzbar import decode

class QR:   
  
    def __init__(self):   
        self.decoder()   
        self.generate_decoded_response()
        self.get_decoded_response()
    
    def decoder(self):   
        raise NotImplementedError   
    
    def generate_decoded_response(self):   
        raise NotImplementedError
  
    def get_decoded_response(self):   
      raise NotImplementedError 

class QRDecoder(QR):
    decoded_data = None
    def __init__(self, image):
        self.image = image
    
    def decoder(self):
        img = Image.open(self.image)
        self.decoded_data = decode(img)
        
    def generate_decoded_response(self):
        self.response = []
        for data in self.decoded_data:
            temp = {}
            # Used decode method to convert byte to string
            temp[data.data.decode()] = {
                'position': [data.polygon[0][0], data.polygon[0][1], data.polygon[2][0], data.polygon[2][1]]
            }
            self.response.append(temp)
        
    def get_decoded_response(self):
        return self.response
    
def construct_qr(cls, path):   
    qr = cls(path)   
    qr.decoder()   
    qr.generate_decoded_response()  
    return qr
