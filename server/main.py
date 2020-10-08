import os
from flask import *
from werkzeug.utils import secure_filename
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from fastai.vision.all import *
from PIL import Image
import numpy as np
import base64
from io import BytesIO
import json
import logging


app = Flask(__name__)
CORS(app)
api = Api(app)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

model = load_learner('model/model_v0.pkl')
UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = (['png', 'jpg', 'jpeg'])

def is_allowed_filename(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@cross_origin()
@app.route('/upload', methods=['POST'])
def upload():
	if 'file' not in request.files:
		image = json.dumps(request.get_json())
		im = Image.open(BytesIO(base64.b64decode(image.split(',')[1])))
		im.save('image.png')
		image_np = np.array(im)
		image_without_alpha = image_np[:, :, :3]
		is_clean, _, probs = model.predict(image_without_alpha)
		prob = float(list(probs.numpy())[1])
		return {"is_clean": is_clean, "predictedVal": prob}

	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message': 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and is_allowed_filename(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		path = UPLOAD_FOLDER + '/' + filename
		resp = predict(path)
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message': 'Allowed file types are png, jpg, jpeg'})
		resp.status_code = 400
		return resp

@cross_origin()
def predict(img_path):
	img = Image.open(img_path)
	print(img)
	img_np = np.array(img)
	is_clean, _ ,probs = model.predict(img_np)
	prob = float(list(probs.numpy())[1])
	return {"is_clean": is_clean , "predictedVal": prob}

if __name__ == "__main__":
    app.run(debug=True)
