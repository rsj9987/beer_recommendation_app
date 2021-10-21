from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .settings.my_settings import SECRET_KEY, SQLALCHEMY_DATABASE_URI  

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
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
