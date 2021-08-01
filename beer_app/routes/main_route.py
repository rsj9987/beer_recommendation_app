from flask import Blueprint, render_template, request
from beer_app.models.beer_model import Beer


bp = Blueprint('main', __name__)

@bp.route('/')
def recommend_index():
    return render_template('index.html')

