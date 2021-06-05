# assistant-school-automate-captcha
A Web Service use OCR to figure number from HUST's Captcha

# CAUTION: vietocr use pyyaml
pip install Flask
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
pip install Pillow
pip install pyyaml
pip install vietocr==0.3.2

# =====WINDOW=====
# install
python3.6.8
py -3 -m venv venv
venv\Scripts\activate

# run
venv\Scripts\activate
python main.py

# =====LINUX=====
# CAUTION: venv có vấn đề về network khi restart app bị connection refused kể cả khi đã listen
# install
python3.9.5
python -m venv venv
source venv/bin/activate

# run
source venv/bin/activate
python main.py