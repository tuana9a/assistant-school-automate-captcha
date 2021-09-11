import os
import io
import sys
import yaml
import logging

from PIL import Image
from flask import Flask, request
from werkzeug.utils import secure_filename

from vietocr.tool.config import Cfg
from vietocr.tool.predictor import Predictor


with open("resource/app-config.yaml") as f:
    AppConfig = yaml.load(f, Loader=yaml.FullLoader)


def load_model():
    config = AppConfig["vietocr"]
    model_config = Cfg.load_config_from_file(config["weights"]["config"])
    model_config["weights"] = config["weights"]["path"]
    model_config["device"] = config["device_type"]
    # EXPLAIN: để false vì mình không train
    model_config["cnn"]["pretrained"] = False
    model = Predictor(model_config)
    return model


def create_server(custom_config=None):
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
        SECRET_KEY="b7HHex1dxdfjxfcxd3x1b!xb4xe6m",
        MAX_CONTENT_LENGTH=5 * 1024 * 1024,  # EXPLAIN: 5MB
    )

    # custom logging
    log = logging.getLogger("werkzeug")
    log.setLevel(logging.ERROR)
    return app


def is_allowed_extension(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in AppConfig["flask"]["allowed_extension"]


def main():
    model = load_model()
    server = create_server()

    @server.route("/", methods=["GET"])
    def index():
        return "hello world"

    @server.route("/api/captcha/to/text", methods=["GET"])
    def _captcha_to_text():
        return "your are right"

    @server.route("/api/captcha/to/text", methods=["POST"])
    def captcha_to_text():
        if "file" not in request.files:
            return "no file upload"

        uploadfile = request.files["file"]

        if not uploadfile:
            return "no file upload"

        filename = secure_filename(uploadfile.filename)

        if not is_allowed_extension(filename):
            return "not allowed " + filename

        try:
            buffers = uploadfile.stream._file.getvalue()
            image = Image.open(io.BytesIO(buffers))
            result = model.predict(img=image)
            return result

        except:
            return "I don't know"

    bind = AppConfig["server"]["bind"]
    port = os.environ.get("PORT") or AppConfig["server"]["port"]
    print(" * Listen: " + str(port))
    server.run(host=bind, port=port)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
