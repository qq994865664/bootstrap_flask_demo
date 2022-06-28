# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint
from flask import render_template

icons_blueprint = Blueprint('icons', __name__)


@icons_blueprint.route('/icons/icons-bootstrap', methods=['GET', 'POST'])
def icons_bootstrap():
    return render_template('icons/icons-bootstrap.html', )


@icons_blueprint.route('/icons/icons-boxicons', methods=['GET', 'POST'])
def icons_boxicons():
    return render_template('icons/icons-boxicons.html', )


@icons_blueprint.route('/icons/icons-remix', methods=['GET', 'POST'])
def icons_remix():
    return render_template('icons/icons-remix.html', )
