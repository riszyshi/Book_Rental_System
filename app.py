from flask import Flask, render_template,session
from datetime import datetime
from flask_migrate import Migrate
from models.Models import db
from routes.web import auth,dashboards,histories,books,status,users,rents
app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(dashboards, url_prefix='/dashboard')
app.register_blueprint(histories, url_prefix='/histories')
app.register_blueprint(books, url_prefix='/books')
app.register_blueprint(status, url_prefix='/status')
app.register_blueprint(users, url_prefix='/users')

app.register_blueprint(rents, url_prefix='/rent')


###################################################

@app.route('/')
def index():
    
    return '<h1>Proceed to /login</h1>'
    
#####################ERRORS########################

@app.errorhandler(401)
def error_401(e):
    code_no = '401'
    code_d = 'Unauthorized Access'
    if 'logged_in' in session:
        balik = '/dashboard/'
    else:
        balik = '/login'

    return render_template('auth/login.html')

@app.errorhandler(403)
def error_403(e):
    code_no = '403'
    code_d = 'Access Forbidden'
    if 'logged_in' in session:
        balik = '/dashboard/'
    else:
        balik = '/login'
    return render_template('errors/main.html',code=code_no, desc = code_d,bacs = balik)

@app.errorhandler(404)
def error_404(e):
    code_no = '404'
    code_d = 'Invalid Page'
    if 'logged_in' in session:
        balik = '/dashboard/'
    else:
        balik = '/login'
    return render_template('errors/main.html',code=code_no, desc = code_d,bacs = balik)

@app.errorhandler(500)
def error_500(e):
    code_no = '500'
    code_d = 'Server Error'
    balik = None
    return render_template('errors/main.html',code=code_no, desc = code_d,bacs = balik)

@app.errorhandler(502)
def error_502(e):
    code_no = '502'
    code_d = 'Bad Gateway'
    balik = None
    return render_template('errors/main.html',code=code_no, desc = code_d,bacs = balik)

@app.errorhandler(503)
def error_503(e):
    code_no = '503'
    code_d = 'Service Unavailable'
    balik = None
    return render_template('errors/main.html',code=code_no, desc = code_d,bacs = balik)

@app.errorhandler(504)
def error_504(e):
    code_no = '504'
    code_d = 'Getway Timeout'
    balik = None
    return render_template('errors/main.html',code=code_no, desc = code_d,bacs = balik)


@app.template_filter('ctime')
def custom_time_format(s):
    if isinstance(s, str):
        try:
            timestamp = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return s  # Return the input string if the format doesn't match
    elif isinstance(s, datetime):
        timestamp = s
    else:
        return s  
    
    return timestamp.strftime('%A, %B %d, %Y %I:%M:%S %p')


####################################################
with app.app_context():
    app.jinja_env.cache.clear()

if __name__ == '__main__':
    app.debug = True
    app.run()


















