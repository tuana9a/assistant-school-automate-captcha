# import matplotlib.pyplot as plt
from PIL import Image
from flask import Flask

import yaml
import model

with open("config.yaml", "r") as file:
    app_config = yaml.load(file,  Loader=yaml.BaseLoader)


base_path = "D:/GemDino/WEB-RESOURCE/school-automate/captcha"
model = model.load_model('models/weights.pth', 'cpu')
app = Flask(__name__)


@app.route('/api/captcha/<captchaId>', methods=["GET"])
def predict_captcha(captchaId):
    img_path = base_path + "/" + captchaId + ".png"
    result = model.predict(Image.open(img_path))
    return result


if __name__ == '__main__':
    app.run(port=app_config["server"]["port"], debug=True)
