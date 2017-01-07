from flask import jsonify
from model import connect_to_db, db, User, Restaurant, Tracking, Friend, Status
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from datetime import datetime
import decimal
from flask.ext.bcrypt import Bcrypt
import random

def create_user(username, email, encrypted_pw, first_name, last_name, ucreated_at):
    """Creates user instance in db"""

    user = User(username=username,
        email=email,
        password=encrypted_pw,
        first_name=first_name,
        last_name=last_name,
        ucreated_at=ucreated_at)
    db.session.add(user)
    db.session.commit()
    return user

def create_tracking(user_id, rest_id, visited, tracking_note, tracking_review, tcreated_at):
    """Creates tracking instance in db"""

    tracking = Tracking(user_id=user_id,
        rest_id=rest_id,
        visited=visited,
        tracking_note=tracking_note,
        tracking_review=tracking_review,
        tcreated_at=tcreated_at)
    db.session.add(tracking)
    db.session.commit()
    return tracking

#NEW - NEEDS TEST
def create_restaurant(rest_name, city, address, lat, lng, photo, placeid, price, rating, bus_hours, rest_review, current_time):
    """Creates restaurant instance in db"""

    restaurant = Restaurant(rest_name=rest_name, 
                                city=city, 
                                address=address, 
                                lat=lat, 
                                lng=lng, 
                                photo=photo, 
                                placeid=placeid, 
                                price=price, 
                                rating=rating, 
                                bus_hours=bus_hours, 
                                rest_review=rest_review,
                                rcreated_at=current_time)
    db.session.add(restaurant)
    db.session.commit()
    return restaurant

def get_all_trackings(user_id, rest_id):
    """Returns a user's trackings by user_id and rest_id"""

    return db.session.query(Tracking).filter_by(user_id=user_id, rest_id=rest_id).all()

#FAILED
def get_match(query):
    """Given a user's autocomplete query, returns a matching restaurant in the restaurants table"""

    match = Restaurant.query.filter_by(rest_name=query[0]).all()
    return match

def filter_trackings(user_id, filter_by):
    """Returns filtered trackings as JSON by user_id and user input"""

    if filter_by == "visited":
        trackings = Tracking.query.filter(Tracking.user_id==user_id, Tracking.visited==True).all()
    elif filter_by == "not_visited":
        trackings = Tracking.query.filter(Tracking.user_id==user_id, Tracking.visited==False).all()
    else:
        trackings = Tracking.query.join(Restaurant).filter(Tracking.user_id==user_id, Restaurant.city==filter_by).all()


    tracking_json = {'data' : []}
    if len(trackings) > 0:
        for tracking in trackings:
            if tracking.visited == True:
                visited = "You've eaten here"
            else:
                visited = "On your To-eat List"
            track_dict = {
            "tracking_id" : tracking.tracking_id,
            "visited" : visited,
            "rest_name" : tracking.restaurant.rest_name,
            "tracking_url" : '/tracking/{}'.format(tracking.tracking_id),
            "photo" : tracking.restaurant.photo,
            "city" : tracking.restaurant.city}
            tracking_json['data'].append(track_dict)
    
    return tracking_json

def tracking_cities(user_id):
    """Returns a list of cities in which a user is tracking restaurants by user_id"""

    all_cities = db.session.query(Restaurant.city).join(Tracking).filter(Tracking.user_id==user_id).group_by(Restaurant.city).all()
    cities = []
    for city in all_cities:
        cities.append(city[0].encode('utf-8'))

    return cities

def sort_trackings(user_id, sort_by):
    """Returns sorted trackings as JSON by user_id and user input"""

    if sort_by == "low_price":
        trackings = Tracking.query.join(Restaurant).filter(Tracking.user_id==user_id).order_by(Restaurant.price).all()
    elif sort_by == "high_price":
        trackings = Tracking.query.join(Restaurant).filter(Tracking.user_id==user_id).order_by(Restaurant.price.desc()).all()
    elif sort_by == "low_rating":
        trackings = Tracking.query.join(Restaurant).filter(Tracking.user_id==user_id).order_by(Restaurant.rating).all()
    elif sort_by == "high_rating":
        trackings = Tracking.query.join(Restaurant).filter(Tracking.user_id==user_id).order_by(Restaurant.rating.desc()).all()
    elif sort_by == "newest":
        trackings = Tracking.query.filter(Tracking.user_id==user_id).order_by(Tracking.tcreated_at.desc()).all()
    elif sort_by == "oldest":
        trackings = Tracking.query.filter(Tracking.user_id==user_id).order_by(Tracking.tcreated_at).all()
        
    tracking_json = {'data' : []}
    if len(trackings) > 0:
        for tracking in trackings:
            if tracking.visited == True:
                visited = "You've eaten here."
            else:
                visited = "On your To-eat List."
            track_dict = {
            "tracking_id" : tracking.tracking_id,
            "visited" : visited,
            "rest_name" : tracking.restaurant.rest_name,
            "tracking_url" : '/tracking/{}'.format(tracking.tracking_id),
            "photo" : tracking.restaurant.photo,
            "city" : tracking.restaurant.city}
            tracking_json['data'].append(track_dict)
    
    return tracking_json

def format_add(user_id):
    """Returns list of formatted addresses for restaurants for a user's tracked restaurants by user_id"""

    user = User.query.get(user_id)
    rest_add = []
    for ut in user.trackings:
        address = ''
        if ut.restaurant.address != None:
            formatted_add = ut.restaurant.address.split(',')
            if formatted_add[-1] == ' United States':
                for fa in formatted_add[:-1]:
                    address = address + fa.encode('utf-8') + ','
            else:
                for fa in formatted_add:
                    address = address + fa.encode('utf-8') + ','
        rest_add.append(address[:-1])

    return rest_add

def find_friends(user_id):
    """Returns a list of tuples with a friend's user_id and full name by the user's user_id"""

    all_friends = Friend.query.filter(Friend.status==2).all()
    
    user_friends = []
    for friend in all_friends:
        if friend.friend_one == int(user_id):
            user_friends.append(friend.friend_two)
        elif friend.friend_two == int(user_id):
            user_friends.append(friend.friend_one)

    friend_id_names = []
    for fid in user_friends:
        other_friend = User.query.get(fid)
        id_and_name = fid, (other_friend.first_name.encode('utf-8') + ' ' + other_friend.last_name.encode('utf-8'))
        friend_id_names.append(id_and_name)
    
    return friend_id_names

def suggest_friends(passed_user_id):
    """Returns a list of tuples with a suggested friend's user_id and full name by user's user_id"""

    all_friends = Friend.query.all()
    
    user_friends = []
    for friend in all_friends:
        if friend.friend_one == int(passed_user_id):
            user_friends.append(friend.friend_two)
        elif friend.friend_two == int(passed_user_id):
            user_friends.append(friend.friend_one)

    others = User.query.filter(User.user_id!=passed_user_id).all()

    sugg_id_names = []
    for other in others:
        if other.user_id not in user_friends:
            id_and_name = other.user_id, (other.first_name.encode('utf-8') + ' ' + other.last_name.encode('utf-8'))
            sugg_id_names.append(id_and_name)

    if len(sugg_id_names) >= 5:
        return random.sample(set(sugg_id_names), 5)
    else:
        return sugg_id_names

def pending_friends(user_id):
    """Returns a list of tuples with a pending friend's user_id and full name by user's user_id"""

    all_friends = db.session.query(Friend).filter_by(friend_two=user_id, status=1).all()
    
    user_friends = []

    if all_friends:
        for friend in all_friends:
            user_friends.append(friend.friend_one)

    friend_id_names = []
    for fid in user_friends:
        other_friend = User.query.get(fid)
        id_and_name = fid, (other_friend.first_name.encode('utf-8') + ' ' + other_friend.last_name.encode('utf-8'))
        friend_id_names.append(id_and_name)

    return friend_id_names

def accept_new_friend(accept_id, user_id):
    """Accepts a friend request by changing the friend status from pending (1) to confirmed (2) on friend obj"""

    friendship = db.session.query(Friend).filter_by(friend_one=accept_id, friend_two=user_id, status=1).all()
    friendship[0].status = 2
    db.session.commit()

def request_new_friend(user_id, request_id):
    """Creates a friend request by creating a friend object with a pending status (1)"""
    current_time = datetime.now()
    friend = Friend(friend_one=user_id, 
                                friend_two=request_id, 
                                status=1,
                                fcreated_at=current_time)
    db.session.add(friend)
    db.session.commit()

def delete_friend(user_id, friend_id):
    """Deletes friend by removing friend object from the db"""

    friendship = db.session.query(Friend).filter_by(friend_one=friend_id, friend_two=user_id).first() or db.session.query(Friend).filter_by(friend_one=user_id, friend_two=friend_id).first()

    db.session.delete(friendship)
    db.session.commit()

