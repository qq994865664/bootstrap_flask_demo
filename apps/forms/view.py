# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint
from flask import render_template

forms_blueprint = Blueprint('forms', __name__)


@forms_blueprint.route('/forms/forms-editors', methods=['GET', 'POST'])
def forms_editors():
    return render_template('forms/forms-editors.html', )


@forms_blueprint.route('/forms/forms-elements', methods=['GET', 'POST'])
def forms_elements():
    return render_template('forms/forms-elements.html', )


@forms_blueprint.route('/forms/forms-layouts', methods=['GET', 'POST'])
def forms_layouts():
    return render_template('forms/forms-layouts.html', )


@forms_blueprint.route('/forms/forms-validation', methods=['GET', 'POST'])
def forms_validation():
    return render_template('forms/forms-validation.html', )
