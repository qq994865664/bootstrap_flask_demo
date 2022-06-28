# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint
from flask import render_template

chart_blueprint = Blueprint('chart', __name__)


@chart_blueprint.route('/charts/charts-chartjs', methods=['GET', 'POST'])
def chart_chartjs():
    return render_template('charts/charts-chartjs.html', )


@chart_blueprint.route('/charts/charts-apexcharts', methods=['GET', 'POST'])
def chart_apexcharts():
    return render_template('charts/charts-apexcharts.html', )


@chart_blueprint.route('/charts/charts-echarts', methods=['GET', 'POST'])
def chart_echarts():
    return render_template('charts/charts-echarts.html', )
