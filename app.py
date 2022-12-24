import os
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

from intractor import QRDecoder

app = Flask(__name__)
api =   Api(app)
UPLOAD_FOLDER = 'qr_codes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# @app.route('/upload', methods = ['POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if not file:
#             return jsonify({'error': 'Send File'})
#         path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(path)
        
#         qr = QRDecoder('qrcode.png')
#         decoded_data = qr.decoder()
#         decoded_resp = qr.get_decoded_response(decoded_data)
        
#         return jsonify({'data': decoded_resp})
    
class QRDecoderAPI(Resource):
    def post(self):
        file = request.files['file']
        print('gnrie')
        input()
        if not file:
            return {'error': 'Send File'}
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        
        qr = QRDecoder('qrcode.png')
        decoded_data = qr.decoder()
        decoded_resp = qr.get_decoded_response(decoded_data)
        
        return {'data': decoded_resp}
  
api.add_resource(QRDecoderAPI,'/upload')

if __name__ == '__main__':

	app.run()
