from flask import Blueprint

'''
CONTROLLERS
'''
from controllers.AuthController import *
from controllers.DashboardController import *
from controllers.HistoryController import *
from controllers.BookController import *
from controllers.StatusController import *
from controllers.UserController import *
from controllers.FrontController import *

'''
Blueprints
'''
auth = Blueprint('auth', __name__) #
dashboards = Blueprint('dashboards', __name__)#
histories = Blueprint('histories', __name__) #
books = Blueprint('books', __name__) #
status = Blueprint('status', __name__)
users = Blueprint('users', __name__)
rents = Blueprint('rents', __name__)


'''
ROUTES
'''

#Auth
auth.route('login',  methods=['GET','POST'])(login)
auth.route('/logout')(logout)


#Dashboard
dashboards.route('/')(dashboad_index)

#books
books.route('/', methods=['GET'])(books_index)
books.route('/create', methods=['POST'])(books_store)
books.route('/update', methods=['POST'])(books_update)
books.route('/delete', methods=['POST'])(books_destroy)
books.route('/show', methods=['GET'])(books_show)
books.route('/uptavail', methods=['POST'])(updete_available)


#status
status.route('/', methods=['GET'])(status_index)
status.route('/create', methods=['POST'])(status_store)
status.route('/update', methods=['POST'])(status_update)
status.route('/delete', methods=['POST'])(status_destroy)
status.route('/show', methods=['GET'])(status_show)
status.route('/rented', methods=['GET'])(status_rented)
status.route('/del_up', methods=['POST'])(updete_iddelete)



#users
users.route('/', methods=['GET'])(user_index)
users.route('/create', methods=['POST'])(user_store)
users.route('/update', methods=['POST'])(user_update)
users.route('/delete', methods=['POST'])(user_destroy)
users.route('/show', methods=['GET'])(user_show)

#histories
histories.route('/', methods=['GET'])(history_index)
histories.route('/create', methods=['POST'])(history_store)
histories.route('/update', methods=['POST'])(history_update)
histories.route('/delete', methods=['POST'])(history_destroy)
histories.route('/show', methods=['GET'])(history_show)


#rent
rents.route('/', methods=['GET'])(rents_index)



