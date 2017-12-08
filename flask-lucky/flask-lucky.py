from flask import Flask
import json
from flask import request, jsonify
from flask import make_response
from flask import Response
from flask_mysqldb import MySQL
from functools import wraps
from os import path
from werkzeug.utils import secure_filename
from flask import make_response, request, current_app
from functools import update_wrapper

app = Flask(__name__)
# mysql = MySQL(app)

# app.config['MYSQL_HOST'] = '35.194.183.62'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'lucky'


@app.route("/")
def home():
    # data = []
    # cur = mysql.connection.cursor()
    # cur.execute('''SELECT * FROM images''')
    # result = cur.fetchall()
    # for row in result:
    #     print(row)
    #     data.append(row)

    result = {
        "code": 0,
        "msg": "success",
        "data": [
            {'name': '1.jpg', 'path': 'https://wx2.sinaimg.cn/mw690/006t5KMygy1fm4n316fpgj30gm0gjqef.jpg'},
            {'name': '2.jpg', 'path': 'https://wx1.sinaimg.cn/mw690/006t5KMygy1fm4n305kvvj30gm0gfdry.jpg'},
            {'name': '3.jpg', 'path': 'https://wx1.sinaimg.cn/mw690/006t5KMygy1fm4n30so5kj30gm0gaqdx.jpg'},
            {'name': '4.jpg', 'path': 'https://wx3.sinaimg.cn/mw690/006t5KMygy1fm4n30a2x6j30gj0gkwpz.jpg'},
            {'name': '5.jpg', 'path': 'https://wx2.sinaimg.cn/mw690/006t5KMygy1fm4n31gluij30gj0gigwi.jpg'},
            {'name': '6.jpg', 'path': 'https://wx3.sinaimg.cn/mw690/006t5KMygy1fm4n306su6j30gl0gh4ah.jpg'},
            {'name': '7.jpg', 'path': 'https://wx1.sinaimg.cn/mw690/006t5KMygy1fm4n32q34dj30gl0gik3s.jpg'},
            {'name': '8.jpg', 'path': 'https://wx4.sinaimg.cn/mw690/006t5KMygy1fm4n32knnpj30gm0ggwpu.jpg'},
        ]
    }
    result_json = json.dumps(result)
    resp = Response(result_json)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        return rst
    return wrapper_fun


@app.route("/uploadpic", methods=['GET', 'POST', 'OPTIONS'])
# @allow_cross_domain
def uploadPic():
    data = {
        "code": 0,
        "msg": "success"
    }
    pic_file = ''
    if request.files['file']:
        pic_file = request.files['file']

    if pic_file != '':
        base_path = path.abspath(path.dirname(__file__))
        upload_path = path.join(base_path, 'static/uploads/')
        file_name = upload_path + secure_filename(pic_file.filename)
        pic_file.save(file_name)
    if pic_file == '':
        data = {
            "code": 1,
            "msg": "error, pic file does not exist!"
        }
    result_json = json.dumps(data)
    resp = Response(result_json)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run()
