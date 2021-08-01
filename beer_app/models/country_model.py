from beer_app import db

class Country(db.Model):
    __tablename__ = 'country'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    beers = db.relationship("Beer", backref="country")

    def __repr__(self):
        return f"Country {self.id} ({self.name})"

def add_country(name):
    db.session.add(Country(**{'name' : name}))
    db.session.commit()
