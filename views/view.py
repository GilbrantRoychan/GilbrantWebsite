from flask import Blueprint,render_template
from markupsafe import escape

home = Blueprint('home',__name__)


@home.route('/')
def index():
    linkwa = 'https://api.whatsapp.com/send/?phone=62089504455462&text&type=phone_number&app_absent=0'
    return render_template('base.html',wa = escape(linkwa) )