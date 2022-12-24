#app.py
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
import urllib.request
import os
from werkzeug.utils import secure_filename

from intractor import QRDecoder
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
 
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No image selected for uploading'})
    if file and allowed_file(file.filename):
        # TODO: filename will change to UUID
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        qr = QRDecoder(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        decoded_data = qr.decoder()
        decoded_resp = qr.get_decoded_response(decoded_data)
        
        return jsonify({'data': decoded_resp})
        # return jsonify({'message': 'Image successfully uploaded and displayed below'})
    else:
        return jsonify({'message': 'Allowed image types are - png, jpg, jpeg, gif'})
    
    
    
    
 
if __name__ == "__main__":
    app.run()