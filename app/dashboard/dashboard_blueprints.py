from flask import Blueprint, render_template
from flask_login import login_required

dashboard_blueprints = Blueprint('dashboard_blueprints', __name__)


@dashboard_blueprints.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')
