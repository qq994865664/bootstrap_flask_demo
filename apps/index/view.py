# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
import json

from flask import Blueprint, request, jsonify
from flask import render_template

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', )


@index_blueprint.route('/test', methods=['GET', 'POST'])
def test_service():
    num = '-----'
    if request.method == 'POST':
        num = request.form['num']
    data = ["从后台传来的数据" + num]
    return render_template('test.html', data=data)


@index_blueprint.route('/test/ajax', methods=['GET', 'POST'])
def test_ajax_service():
    if request.method == 'POST':
        num = request.form['num']
        return jsonify(["从后台传来的数据" + num])


@index_blueprint.route('/ajax', methods=['GET', 'POST'])
def ajax_service():
    if request.method == 'POST':
        num = request.get_json()
        print(num)
        # print(json.loads(num))
        return jsonify(["从后台传来的数据" + json.dumps(num)])
