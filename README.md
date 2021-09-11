# HUST's captcha to text

<pre>
webservice nhận diện captcha các trang web trường đại học Bách Khoa Hà Nội thành text
mình dùng thư viện <a href="https://github.com/pbcquoc/vietocr">pbcquoc/vietocr</a> đã train tiếp models với ~2000 bức ảnh
các bạn có thể <a href="https://github.com/tuana9a/tuana9a">liên hệ mình</a> nếu cần hỗ trợ
mọi thông tin có thể public mình để ở <a href="https://drive.google.com/drive/folders/1YAVIaEI7ffRzCIAhXJNJYV_bVdQLie4F?usp=sharing">thư mục drive</a>
</pre>

# #requirements

<strong><b style="color:red">NOTE:</b>
<br>
pip install -r requirements.txt nếu có lỗi thì bạn có thể cài thủ công phía dưới
<br>
pytorch mình cài là CPU, với CUDA hiện tại mình chưa test, các bạn có thể cài và thử từ <a href="https://pytorch.org/">trang chủ</a> pytorch
</strong>

<pre>
pip install Flask==2.0.1
pip install Pillow==8.3.2
pip install pyyaml==5.4.1
pip install torch==1.8.2+cpu torchvision==0.9.2+cpu torchaudio===0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
pip install vietocr==0.3.2
</pre>

# #structure

<pre>
-- ./
   |-- .venv/
   |-- resource/
   |       |-- app-config.yaml
   |       |-- weights.pth
   |       |-- weights-config.yaml
   |-- main.py
</pre>

# #run

<pre>
python main.py
</pre>
