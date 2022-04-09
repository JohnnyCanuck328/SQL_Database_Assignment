import imp
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    from.views import views
    from.auth import auth
    from.dentist import dentist

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(dentist, url_prefix='/')

    return app