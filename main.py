from PIL import Image
from flask import Flask, request, flash
from werkzeug.utils import secure_filename

from vietocr.tool.config import Cfg
from vietocr.tool.predictor import Predictor

import os
import io
import yaml
import logging

with open('resource/app-config.yml') as f:
    APP_CONFIG = yaml.load(f, Loader=yaml.FullLoader)


def load_model(config_path, weights_path, device_type):
    model_config = Cfg.load_config_from_file(config_path)
    model_config['weights'] = weights_path
    model_config['device'] = device_type
    # EXPLAIN: để false vì mình không train
    model_config['cnn']['pretrained'] = False
    model = Predictor(model_config)
    return model


model = load_model(
    config_path=APP_CONFIG['weights']['config'],
    weights_path=APP_CONFIG['weights']['path'],
    device_type=APP_CONFIG['weights']['device']
)


def init_server(custom_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    # try:
    #     instance_path = app.instance_path
    #     os.makedirs(instance_path)
    # except OSError:
    #     pass

    # param config
    if custom_config is not None:
        app.config.from_mapping(custom_config)

    # manual config
    app.config.from_mapping(
        SECRET_KEY='b7HHex1dxdfjxfcxd3x1b!xb4xe6m',
        MAX_CONTENT_LENGTH=5 * 1024 * 1024,  # EXPLAIN: 5MB
    )

    # custom logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    return app


app = init_server()


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def check_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/predict/captcha', methods=['POST'])
def upload_to_predict():
    if 'file' not in request.files:
        flash('No file part')
        return 'no file upload'

    uploadfile = request.files['file']
    filename = secure_filename(uploadfile.filename)

    if uploadfile and check_allowed_file(filename):
        try:
            buffers = uploadfile.stream._file.getvalue()
            image = Image.open(io.BytesIO(buffers))
            result = model.predict(img=image)
            return result

        except TypeError:
            return 'Error'

        except ValueError:
            return 'Error'

    return 'not allowed: ' + filename


print(' * Listen: ' + APP_CONFIG['server']['address'])
app.run(host='0.0.0.0', port=APP_CONFIG['server']['port'])
