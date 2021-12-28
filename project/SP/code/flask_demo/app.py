import requests
from flask import Flask, render_template, make_response, request
from setting import DefaultConfig
from gevent import pywsgi
from exts import db
from user import User
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import threading

app = Flask(__name__)
app.config.from_object(DefaultConfig)


# db.init_app(app)


@app.route('/')
def main():
    # dict_user = {
    #     'username': '备案学习界面'
    # }
    # result_all = User.query.all()
    # result = result_all[0]
    # print(result.username)
    # username = '张三'
    # password = '456789'
    # dict_user = {'username':username, 'password': password}
    # user = User(**dict_user)
    # db.session.add(user)
    # db.session.commit()
    # response = render_template('main/index.html', user=dict_user)
    return 'hello world123'


@app.route('/index')
def index():
    dict_user = {
        'username': '备案学习界面2'
    }
    html = render_template('user/index.html', user=dict_user)
    return make_response(html, 200)


@app.route('/register', methods=["GET", "POST"])
def register():
    req = request
    # print(request.args.get('username'))
    # print(request.args.get('address'))
    print(request.data.get('username'))
    print(request.data.get('address'))
    return '注册提交'


def test(text):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))


def start_job(access_token):
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    # 每隔 1分钟 运行一次 job 方法
    scheduler.add_job(func=test, args=[access_token],
                      trigger="interval", seconds=10)
    scheduler.start()


if __name__ == '__main__':
    thread = threading.Thread(target=start_job, args=['666'])
    thread.start()
    server = pywsgi.WSGIServer(('0.0.0.0', 8080), app)
    server.serve_forever()
    # app.run(host='0.0.0.0', port='8080')
