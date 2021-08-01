from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '0cfeb98912589a4a7138882953cc2df9'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yhthgsqa:1Zv1zL5yJ4lnaxW-UppjUtUK52vFGs7p@arjuna.db.elephantsql.com:5432/yhthgsqa'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    migrate.init_app(app, db)

    from beer_app.routes import (main_route, beer_route, recommend_route)
    app.register_blueprint(main_route.bp)
    app.register_blueprint(beer_route.bp)
    app.register_blueprint(recommend_route.bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
