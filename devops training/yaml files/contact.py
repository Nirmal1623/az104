from flask import Blueprint
contact_bp = Blueprint('contact', __name__)
@contact_bp.route('/hello/')
def hello():
    return "hello from contact page"