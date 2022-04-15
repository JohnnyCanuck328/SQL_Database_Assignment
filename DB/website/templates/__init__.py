import imp
from flask import Flask, url_for

from website.templates.receptionist import patient

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    from.views import views
    from.receptionist import receptionist
    from.dentist import dentist
    from.patient import patient

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(receptionist, url_prefix='/')
    app.register_blueprint(dentist, url_prefix='/')
    app.register_blueprint(patient, url_prefix='/')

    return app