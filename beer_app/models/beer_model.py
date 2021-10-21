# from flask_sqlalchemy import 
from beer_app import db
from beer_app.models.country_model import Country, add_country

class Beer(db.Model):
    __tablename__ = 'beer'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    types = db.Column(db.String(50), nullable=False)
    alcohol = db.Column(db.Float(), nullable=False)
    taste = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(150))
    image_url = db.Column(db.String(150), default='../static/img/default.jpg')
    country_id = db.Column(db.Integer(), db.ForeignKey('country.id'), nullable=False)

    def __repr__(self):
        return f"Beer {self.id} (Name : {self.name}, types : {self.types})"


def get_beer_list(search=None, check_query=None):
    if search is not None:
        search = f"%{search}%"
        if check_query == 1:
            return Beer.query.filter(Beer.name.like(search)).all()
        elif check_query == 2:
            return Beer.query.filter(Beer.types.like(search)).all()
        elif check_query == 3:
            country = Country.query.filter(Country.name.like(search)).first()
            return country.beers

    return Beer.query.all()

def add_beer(name, types, alcohol, taste, comment, image_url, country_id):
    beer = Beer(**{'name' : name, 'types' : types, 'alcohol' : alcohol, 'taste' : taste,
                 'comment': comment, 'image_url': image_url, 'country_id' : country_id})
    db.session.add(beer)
    db.session.commit()

def delete_beer_on_db(beer_id):
        beer = Beer.query.filter_by(id=beer_id).first()
        db.session.delete(beer)
        db.session.commit()

def add_update_beer(beer_name, beer_types, beer_country, beer_alcohol, beer_taste, beer_comment, beer_image_url):
    beer_from_db = Beer.query.filter_by(name=beer_name).one_or_none()
    country = Country.query.filter_by(name=beer_country).one_or_none()
    # beer update
    if beer_from_db:
        if beer_types is not None:
            beer_from_db.types = beer_types
        if beer_country is not None:
            if country is None:
                add_country(beer_country)
                ctr_id = Country.query.filter_by(name=beer_country).first()
                ctr_id = ctr_id.id
                beer_from_db.country_id = ctr_id
        if beer_alcohol is not None:
            beer_from_db.types = beer_alcohol
        if beer_taste is not None:
            beer_from_db.types = beer_taste
        if beer_comment is not None:
            beer_from_db.comment = beer_comment
        if beer_image_url is not None:
            beer_from_db.image_url = beer_image_url
        db.session.commit()
    # beer create
    else:
        if country is None:
            add_country(beer_country)
        ctr_id = Country.query.filter_by(name=beer_country).first()
        ctr_id = ctr_id.id
        add_beer(beer_name, beer_types, beer_alcohol, beer_taste,
                    beer_comment, beer_image_url, ctr_id)

def get_recommend_beer(result):
    beers = []
    for name in result:
        beers.append(Beer.query.filter(Beer.name.like(f'%{name}%')).first())
    return beers