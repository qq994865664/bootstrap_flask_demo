# @Time : 2020/7/13
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from flask import Blueprint, request, jsonify
from flask import render_template

components_blueprint = Blueprint('components', __name__)


@components_blueprint.route('/components/components-alerts', methods=['GET', 'POST'])
def components_alerts():
    return render_template('components/components-alerts.html')


@components_blueprint.route('/components/components-accordion', methods=['GET', 'POST'])
def components_accordion():
    return render_template('components/components-accordion.html')


@components_blueprint.route('/components/components-badges', methods=['GET', 'POST'])
def components_badges():
    return render_template('components/components-badges.html')


@components_blueprint.route('/components/components-breadcrumbs', methods=['GET', 'POST'])
def components_breadcrumbs():
    return render_template('components/components-breadcrumbs.html')


@components_blueprint.route('/components/components-buttons', methods=['GET', 'POST'])
def components_buttons():
    return render_template('components/components-buttons.html')


@components_blueprint.route('/components/components-cards', methods=['GET', 'POST'])
def components_cards():
    return render_template('components/components-cards.html')


@components_blueprint.route('/components/components-carousel', methods=['GET', 'POST'])
def components_carousel():
    return render_template('components/components-carousel.html')


@components_blueprint.route('/components/components-list-group', methods=['GET', 'POST'])
def components_list_group():
    return render_template('components/components-list-group.html')


@components_blueprint.route('/components/components-modal', methods=['GET', 'POST'])
def components_modal():
    return render_template('components/components-modal.html')


@components_blueprint.route('/components/components-pagination', methods=['GET', 'POST'])
def components_pagination():
    return render_template('components/components-pagination.html')


@components_blueprint.route('/components/components-progress', methods=['GET', 'POST'])
def components_progress():
    return render_template('components/components-progress.html')


@components_blueprint.route('/components/components-spinners', methods=['GET', 'POST'])
def components_spinners():
    return render_template('components/components-spinners.html')


@components_blueprint.route('/components/components-tabs', methods=['GET', 'POST'])
def components_tabs():
    return render_template('components/components-tabs.html')


@components_blueprint.route('/components/components-tooltips', methods=['GET', 'POST'])
def components_tooltips():
    return render_template('components/components-tooltips.html')

