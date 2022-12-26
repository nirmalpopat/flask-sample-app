import os
from werkzeug.utils import secure_filename

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(file, path):
    # TODO: filename will change to UUID
    filename = secure_filename(file.filename)
    file.save(os.path.join(path, filename))
    return filename
