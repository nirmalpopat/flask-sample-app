import os
from flask import Flask, request, jsonify

from intractor import QRDecoder, construct_qr
from utils import allowed_file, upload_file
 
UPLOAD_FOLDER = 'static/uploads'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No image selected for uploading'})
    if file and allowed_file(file.filename):
        filename = upload_file(file, UPLOAD_FOLDER)
        qr = construct_qr(QRDecoder, os.path.join(app.config['UPLOAD_FOLDER'], filename))
        decoded_resp = qr.get_decoded_response()
        return jsonify({'data': decoded_resp})
    else:
        return jsonify({'message': 'Allowed image types are - png, jpg, jpeg'})

if __name__ == "__main__":
    app.run()
