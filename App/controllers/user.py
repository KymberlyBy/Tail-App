from App.models import User
from App import db

def new_user(username, firstName, lastName, email, password, home_address): #no lat and long currently
    user = User(username=username, firstName=firstName, lastName=lastName, email=email, password=password, home_address=home_address)
    db.session.add(user)
    db.session.commit()
    return user

def find_user(username):
    return User.query.filter_by(username=username).first()

def find_user_by_id(ID):
    return User.query.get(ID)


def update_address(ID, home_address):
    user = find_user_by_id(ID)
    if user:
        user.home_address = home_address
        db.session.add(user)
        return db.session.commit()
    return None    