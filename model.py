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
    password = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    ucreated_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        """Provides helpful User object representation when printed"""

        return "<USER OBJ user_id: %s username: %s first_name: %s last_name: %s>" % (self.user_id, self.username, self.first_name, self.last_name)

class Restaurant(db.Model):
    """Restaurants added by a user based on Google Places Search and Places Details results."""

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
    # TODO Remove order_by tracking_id

    def __repr__(self):
        """Provides helpful Tracking object representation when printed"""

        return "<TRACKING OBJ tracking_id: %s visited: %s>" % (self.tracking_id, self.visited)

class Friend(db.Model):

    __tablename__ = "friends"

    friend_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    friend_one = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    friend_two = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    status = db.Column(db.Integer, db.ForeignKey('statuses.status_id'), nullable=True)
    fcreated_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=True)

    user = db.relationship("User", backref="friends")
    status = db.relationship("Status", backref="friends")

    def __repr__(self):
        """Provides helpful Friend object representation when printed"""

        return "<FRIEND OBJ friend_id: %s friend_one: %s friend_two: %s status: %s>" % (self.friend_id, self.friend_one, self.friend_two, self.status)

class Status(db.Model):

    __tablename__ = "statuses"

    status_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    status_code = db.Column(db.String(10), nullable=False)


def connect_to_db(app):
    """Connect the database to Flask app."""
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///toeat'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."


