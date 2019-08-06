from flask import Flask,request,redirect,url_for
import os
import werkzeug
import base64

app = Flask(__name__)

base_url='/infer-66f28b95-d8ec-4e11-a2fe-14a544cc6b16'

@app.route(base_url+'/', methods=['POST'])
def upload_image():
    # 接收图片
    upload_file = request.files['file']
    # 获取图片名
    file_name = upload_file.filename
    
    # 文件保存目录（桌面）
    if upload_file:
        # 地址拼接
        file_paths = os.path.join('/data/code/input_flask/' , file_name)
        # 保存接收的图片到桌面
        upload_file.save(file_paths)
        # 随便打开一张其他图片作为结果返回，
        Predict()
#         output_name = 'trained_'+ file_name
        with open(r'test1.png', 'rb') as f:
        
            res = base64.b64encode(f.read())
            return res


def Predict():
    os.system("python process-local.py --model_dir /data/code/233/pix2pix-origin/export_0806 --input_file 1.png --output_file 2.png")
    #"python pix2pix.py --mode test --output_dir /data/data/233/outline_test_out --input_dir /data/code/input_flask/ --batch_size 1 --checkpoint /data/output/checkpoints/outline_WGAN_2"
    
    
#     return redirect(url_for(endpoint="return"))

app.add_url_rule(rule="/predict/", endpoint="predict", view_func=Predict)


if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port='8080')
