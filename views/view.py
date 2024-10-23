from flask import Blueprint,render_template
from markupsafe import escape

home = Blueprint('home',__name__)
def umur():
    from datetime import datetime
    
    # lahir di tahun
    kelahiran = 2002

    # Tahun saat ini
    tahunToday = datetime.now().year
    

    # Menghitung umur
    umurku = tahunToday - kelahiran
    return umurku

@home.route('/')
def index():
    linkwa = 'https://api.whatsapp.com/send/?phone=62089504455462&text&type=phone_number&app_absent=0'
    about = 'about_me.html'
    
    # , templates = tamplates
    return render_template('base.html',wa = escape(linkwa), about = about,umur = umur() )

@home.route('/aboutMe')
def aboutMe():
    return render_template('about_me.html',umur = umur())
