from flask import Flask

#import Module views
from .views.view import home


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']  = 'sayMayName'
    
    app.register_blueprint(home, url_prefix = '/')
    return app