# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Flask
from apps.index.view import index_blueprint
from apps.forms.view import forms_blueprint
from apps.icons.view import icons_blueprint
from apps.charts.view import chart_blueprint
from apps.tables.view import table_blueprint
from apps.pages.view import pages_blueprint
from apps.components.view import components_blueprint


app = Flask(__name__, template_folder="..\\ui\\templates", static_folder="..\\ui\\static")
app.register_blueprint(index_blueprint)
app.register_blueprint(forms_blueprint)
app.register_blueprint(icons_blueprint)
app.register_blueprint(chart_blueprint)
app.register_blueprint(table_blueprint)
app.register_blueprint(pages_blueprint)
app.register_blueprint(components_blueprint)

