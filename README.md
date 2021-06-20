# assistant-school-automate-captcha
A Web Service use OCR to figure number from HUST's Captcha

# REQUIREMENTS
# CAUTION: vietocr use pyyaml
- <code>pip install Flask</code>
- <code>pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html</code>
- <code>pip install Pillow</code>
- <code>pip install pyyaml</code>
- <code>pip install vietocr==0.3.2</code>

# WINDOW
# setup
- <code>python3.6.8</code>
- <code>py -3 -m venv venv</code>
- <code>venv\Scripts\activate</code>
# run
- <code>venv\Scripts\activate</code>
- <code>python main.py</code>

# LINUX
# CAUTION: có thể  venv có vấn đề về network (connection refused)
# setup
- <code>python3.9.5</code>
- <code>python -m venv venv</code>
- <code>source venv/bin/activate</code>
# run
- <code>source venv/bin/activate</code>
- <code>python main.py</code>