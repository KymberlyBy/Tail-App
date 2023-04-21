from .auth import auth_view
from .users import users_view


#add blueprints must be added here!

views = [auth_view, users_view]