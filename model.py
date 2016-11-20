"""Models and database functions."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """Site users."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(32), nullable=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    ucreated_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        """Provides helpful User object representation when printed"""

        return "<USER OBJ user_id: %s username: %s first_name: %s last_name: %s>" % (self.user_id, self.username, self.first_name, self.last_name)

class Restaurant(db.Model):
    """Restaurant information from Google Places Search and Google Places Details results."""

    __tablename__ = "restaurants"

    rest_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rest_name = db.Column(db.String(128), nullable=True)
    city = db.Column(db.String(58), nullable=True)
    address = db.Column(db.String(256), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)
    photo = db.Column(db.String(2000), nullable=True)
    placeid = db.Column(db.String(128), nullable=True)
    price = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    bus_hours = db.Column(db.String(500), nullable=True)
    rest_review = db.Column(db.Text, nullable=True)
    rcreated_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=True)

    def __repr__(self):
        """Provides helpful Restaurant object representation when printed"""

        return "<REST OBJ rest_id: %s rest_name: %s city: %s>" % (self.rest_id, self.rest_name, self.city)

class Tracking(db.Model):
    """Restaurants added and tracked by a user."""

    __tablename__ = "trackings"

    tracking_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurants.rest_id'), nullable=True)
    visited = db.Column(db.Boolean)
    tracking_note = db.Column(db.String(140), nullable=True)
    # User's short note to self before visiting restaurant (ex. "Must try mac n cheese!")
    tracking_review = db.Column(db.Text, nullable=True)
    # User's review after having visited restuarant
    tcreated_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=True)

    user = db.relationship("User", backref="trackings")
    restaurant = db.relationship("Restaurant", backref="trackings")

    def __repr__(self):
        """Provides helpful Tracking object representation when printed"""

        return "<TRACKING OBJ tracking_id: %s rest_id: %s user_id: %s visited: %s>" % (self.tracking_id, self.rest_id, self.user_id, self.visited)

class Friend(db.Model):

    __tablename__ = "friends"

    friend_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    friend_one = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    friend_two = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    status = db.Column(db.Integer, db.ForeignKey('statuses.status_id'), nullable=True)
    fcreated_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=True)

    # user = db.relationship("User", backref="friends")
    stat = db.relationship("Status", backref="friends")

    def __repr__(self):
        """Provides helpful Friend object representation when printed"""

        return "<FRIEND OBJ friend_id: %s friend_one: %s friend_two: %s status: %s>" % (self.friend_id, self.friend_one, self.friend_two, self.status)

class Status(db.Model):

    __tablename__ = "statuses"

    status_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    status_code = db.Column(db.String(10), nullable=False)

def example_data():
    """Creates sample data for unittests to use"""

    user1 = User(username="mgellar", 
                email="monica@monica.com", 
                password="$2b$12$HheQ3X.85awol9DLmPE6Ze2tpTaT.U1iCy1.BIKHPJebYoKCo6cOm", 
                first_name="Monica", 
                last_name="Gellar", 
                ucreated_at=datetime.now())

    user2 = User(username="cbing", 
                email="chandler@chandler.com", 
                password="$2b$13$HheQ3X.85awol9DLmPE6Ze2tpTaT.U1iCy1.BIKHPJebYoKCo6cOm", 
                first_name="Chandler", 
                last_name="Bing", 
                ucreated_at=datetime.now())

    user3 = User(username="pbuffet", 
                email="phoebe@phoebe.com", 
                password="$2b$14$HheQ3X.85awol9DLmPE6Ze2tpTaT.U1iCy1.BIKHPJebYoKCo6cOm", 
                first_name="Phoebe", 
                last_name="Buffet", 
                ucreated_at=datetime.now())

    user4 = User(username="jtribiani", 
                email="joey@joey.com", 
                password="$2b$15$HheQ3X.85awol9DLmPE6Ze2tpTaT.U1iCy1.BIKHPJebYoKCo6cOm", 
                first_name="Joey", 
                last_name="Tribiani", 
                ucreated_at=datetime.now())

    restaurant1 = Restaurant(rest_name="Mr. Holmes Bakehouse", 
                city="San Francisco",
                address="1042 Larkin St, San Francisco, CA 94109, United States",
                lat=37.7876365,
                lng=-122.4182803,
                photo="https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
                placeid="ChIJT0h_9pOAhYAR-3iNZNso3xk",
                price=1,
                rating=4.2,
                bus_hours=None,
                rest_review="Fantastic cruffins! Omg!",
                rcreated_at=datetime.now())

    restaurant2 = Restaurant(rest_name="Hot Cakes", 
                city="Seattle",
                address="1042 Market St, Seattle, WA 98000, United States",
                lat=36.7876365,
                lng=-120.4182803,
                photo="https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CmskewAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
                placeid="CABCT0h_9pOAhYAR-3iNZNso3xk",
                price=2,
                rating=4.5,
                bus_hours=None,
                rest_review="The pistachio cardamom shake! Yum!",
                rcreated_at=datetime.now())

    db.session.add_all([restaurant1, restaurant2])
    db.session.flush()


    tracking1 = Tracking(user_id=user1.user_id, 
                rest_id=restaurant1.rest_id, 
                visited=True, 
                tracking_note=None, 
                tracking_review="I loved the savory bread pudding.", 
                tcreated_at=datetime.now())

    tracking2 = Tracking(user_id=user1.user_id, 
                rest_id=restaurant2.rest_id, 
                visited=False, 
                tracking_note="The s'mores cake sounds fantastic.", 
                tracking_review=None, 
                tcreated_at=datetime.now())

    status1 = Status(status_code="Pending")
    
    status2 = Status(status_code="Confirmed")

    db.session.add_all([tracking1, tracking2, status1, status2])
    db.session.flush()

    friend1 = Friend(friend_one=user1.user_id, 
                friend_two=user2.user_id, 
                status=2, 
                fcreated_at=datetime.now())

    friend2 = Friend(friend_one=user1.user_id, 
                friend_two=user3.user_id, 
                status=1, 
                fcreated_at=datetime.now())

    db.session.add_all([friend1, friend2])
    db.session.commit()

def connect_to_db(app, db_URI='postgresql:///toeat'):
    """Connect the database to Flask app."""
    
    app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."


