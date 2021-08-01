from flask import Blueprint, render_template, request, redirect, url_for, Response
from beer_app.models.beer_model import Beer, get_recommend_beer
from beer_app.services.zero_transform import zero_to_none
from beer_app.services.recommend import recommend_beer


bp = Blueprint('recommend', __name__)

@bp.route('/recommend', methods=['GET', 'POST'])
def recommend_index():
    title = "고그시 맥주 추천"
    sub_title = "맥주의 종류와 잘 맞는 안주를 추천받아보세요!"
    check_body = None
    fruit = None
    bitter = None
    hoppy = None
    sweet = None
    high_alcohol = None
    malty = None
    beer_list = None
    result = None
    food = None
    if request.method == 'POST':
        check_body = request.form.get('check_body_type', type=int)
        fruit = request.form.get('check_fruit', type=int)
        bitter = request.form.get('check_bitter', type=int)
        hoppy = request.form.get('check_hoppy', type=int)
        sweet = request.form.get('check_sweet', type=int)
        high_alcohol = request.form.get('check_high_alcohol', type=int)
        malty = request.form.get('check_malty', type=int)
        result = None
        if fruit is not None:
            result = recommend_beer(body=1, fruit=fruit)
        elif bitter is not None:
            result = recommend_beer(body=2, hoppy=hoppy, sweet=sweet)
        elif high_alcohol is not None:
            result = recommend_beer(body=3, high_alcohol=high_alcohol, malty=malty)
            
        if result is not None:
            beer_list = get_recommend_beer(result)
            beer_1 = ['라거', '바이젠', '브라운 에일']
            beer_2 = ['IPA', '골든 에일', '페일 에일']
            beer_3 = ['포터', '트라피스트']
            for b in beer_1:
                if b in result:
                    food = 1
            for b in beer_2:
                if b in result:
                    food = 2
            for b in beer_3:
                if b in result:
                    food = 3
    return render_template('recommend.html', title=title, sub_title=sub_title, check_body=check_body, beer_list=beer_list, food=food)

