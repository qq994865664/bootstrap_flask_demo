# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint
from flask import render_template

pages_blueprint = Blueprint('pages', __name__)


@pages_blueprint.route('/pages/pages-blank', methods=['GET', 'POST'])
def page_blank():
    return render_template('pages/pages-blank.html', )


@pages_blueprint.route('/pages/pages-contact', methods=['GET', 'POST'])
def page_contact():
    return render_template('pages/pages-contact.html', )


@pages_blueprint.route('/pages/pages-error-404', methods=['GET', 'POST'])
def page_error_404():
    return render_template('pages/pages-error-404.html', )


@pages_blueprint.route('/pages/pages-faq', methods=['GET', 'POST'])
def page_faq():
    return render_template('pages/pages-faq.html', )


@pages_blueprint.route('/pages/pages-login', methods=['GET', 'POST'])
def page_login():
    return render_template('pages/pages-login.html', )


@pages_blueprint.route('/pages/pages-register', methods=['GET', 'POST'])
def page_register():
    return render_template('pages/pages-register.html', )


@pages_blueprint.route('/pages/users-profile', methods=['GET', 'POST'])
def users_profile():
    return render_template('pages/users-profile.html', )


