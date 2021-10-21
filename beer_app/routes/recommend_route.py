from flask import Blueprint, render_template, request, redirect, url_for, Response
from beer_app.models.beer_model import Beer, get_beer_list, get_recommend_beer
from beer_app.services.recommend import get_recommendation


bp = Blueprint('recommend', __name__)

@bp.route('/recommend', methods=['GET', 'POST'])
def recommend_index():
    title = "고그시 맥주 추천"
    sub_title = "맥주의 종류와 잘 맞는 안주를 추천받아보세요!"
    beer_list = None
    text = None
    if request.method == 'POST':
        beer_name = request.form.get('name')
        name = get_beer_list(beer_name, check_query=1)
        recommended = get_recommendation(name[0].name)
        if type(recommended) == str:
            beer_list = None
            text = recommended
        else:
            beer_list = get_recommend_beer(recommended)
        
    return render_template('recommend.html', title=title, sub_title=sub_title, beer_list=beer_list, text=text)

