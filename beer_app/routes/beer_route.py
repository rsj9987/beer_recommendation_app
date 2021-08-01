from flask import Blueprint, render_template, request, redirect, url_for, Response
from beer_app.models.beer_model import get_beer_list, delete_beer_on_db, add_update_beer, Beer
from beer_app.models.country_model import Country, add_country
from beer_app.services.zero_transform import zero_to_none 
bp = Blueprint('beer', __name__)


@bp.route('/beers', methods=['GET', 'POST'])
def beer_index():
    title = "고그시 맥주"
    sub_title = "어떤 맥주들이 있는지 확인해보세요"
    if request.method == 'POST':
        search = zero_to_none(request.form.get('search'))
        check_query = request.form.get('check_query', type=int)
        try:
            beer_list = get_beer_list(check_query=check_query, search=search)
        except:
            beer_list = get_beer_list()
    else:
        beer_list = get_beer_list()
    return render_template('beers.html', beer_list=beer_list, title=title, sub_title=sub_title)


## warehouse ##
"""
맥주 창고 관리
CRUD 가능하게
"""


@bp.route('/warehouse', methods=["GET", "POST"])
def warehouse_index():
    title = '고그시 맥주 창고'
    sub_title = '맥주창고에 오신 것을 환영합니다!'

    beer_list = get_beer_list()
    # beer_create and update
    if request.method == "POST":
        beer_name = zero_to_none(request.form.get('beername'))
        beer_types = zero_to_none(request.form.get('beer_types'))
        beer_country = zero_to_none(request.form.get('beer_madeby'))
        beer_alcohol = zero_to_none(request.form.get('beer_alcohol'))
        beer_taste = zero_to_none(request.form.get('beer_taste'))
        beer_comment = zero_to_none(request.form.get('beer_comment'))
        beer_image_url = zero_to_none(request.form.get('beer_image_url'))
        add_update_beer(beer_name, beer_types, beer_country, beer_alcohol, beer_taste, beer_comment, beer_image_url)

        return redirect(url_for('beer.warehouse_index', msg_code='add & update success'), code=200)
            
              
                    
    return render_template('warehouse.html', beer_list=beer_list, title=title, sub_title=sub_title)


@bp.route('/warehouse/')
@bp.route('/warehouse/<int:beer_id>')
def delete_beer(beer_id=None):
    if beer_id == None:
        return redirect(url_for('beer.warehouse_index'), code=400)
    try:
        delete_beer_on_db(beer_id)
    except:
        return redirect(url_for('beer.warehouse_index', msg_code='delete not success'), code=404)

    return redirect(url_for('beer.warehouse_index', msg_code='delete success'), code=200)

