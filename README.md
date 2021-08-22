# HUST's captcha to text

<pre>
là webservice nhận diện captcha các trang web trường đại học Bách Khoa Hà Nội thành text
mình dùng thư viện <a href="https://github.com/pbcquoc/vietocr">pbcquoc/vietocr</a> đã train tiếp models với ~2000 bức ảnh
các bạn có thể <a href="https://github.com/tuana9a/tuana9a">liên hệ mình</a> để lấy trọng số, config, và ảnh đã dán nhãn 
</pre>

# #requirements

<strong><i style="color:red">CAUTION:</i> vietocr use pyyaml</strong>

<pre>
pip install Flask==2.0.1
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
pip install Pillow==8.2.0
pip install pyyaml==5.4.1
pip install vietocr==0.3.2
</pre>

# #structure

<pre>
-- root
    |-- .venv
    |-- resource
    |       |-- app-config.yml
    |       |-- weights.pth
    |       |-- weights-config.yml
    |-- main.py
</pre>

# #run

<pre>
python main.py
</pre>
