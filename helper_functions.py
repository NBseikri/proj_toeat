from flask import jsonify
from model import connect_to_db, db, User, Restaurant, Tracking, Friend, Status
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from datetime import datetime
import decimal
from flask.ext.bcrypt import Bcrypt
import random

def create_user(username, email, encrypted_pw, first_name, last_name, ucreated_at):
    """Creates user instance""" 
    user = User(username=username,
        email=email,
        password=encrypted_pw,
        first_name=first_name,
        last_name=last_name,
        ucreated_at=ucreated_at)
    db.session.add(user)
    db.session.commit()
    return user

def filter_trackings(user_id, filter_by):
    """Given user input, returns filtered trackings as JSON"""

    if filter_by == "visited":
        trackings = Tracking.query.filter(Tracking.user_id==user_id, Tracking.visited==True).all()
    else:
        trackings = Tracking.query.filter(Tracking.user_id==user_id, Tracking.visited==False).all()

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

def tracking_cities(user_id):
    """Given a user_id, returns a list of cities for which a user is tracking restaurants"""
    all_cities = db.session.query(Restaurant.city).join(Tracking).filter(Tracking.user_id==1).group_by(Restaurant.city).all()
    cities = []
    for city in all_cities:
        cities.append(city[0].encode('utf-8'))

    return cities

def sort_trackings(user_id, sort_by):
    """Given user input, returns sorted trackings as JSON"""

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
        print "NEWEST"
        print "#####"
        for tracking in trackings:
            print tracking.restaurant.rest_name
    elif sort_by == "oldest":
        print "OLDEST"
        print "#####"
        trackings = Tracking.query.filter(Tracking.user_id==user_id).order_by(Tracking.tcreated_at).all()
        for tracking in trackings:
            print tracking.restaurant.rest_name
    else:
        trackings = Tracking.query.join(Restaurant).filter(Tracking.user_id==user_id, Restaurant.city==sort_by).all()

        
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
    """Returns list of formatted addresses for restaurants"""
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
    """Given a user_id, returns a list of tuples with a friend's user_id and full name"""

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
    """Given a user_id, returns a list of tuples with a suggested friend's user_id and full name"""
    # Returns x for y (the passed in info) #

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

    return random.sample(set(sugg_id_names), len(sugg_id_names)/2)

def pending_friends(user_id):
    """Given a user_id, returns a list of tuples with a pending friend's user_id and full name"""

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
    # friend.accept_new_friend(accept_id)
    # create a method on the Friend class instead of imported functions
    """Accept a friend request by changing the status from pending (1) to confirmed (2)"""

    friendship = db.session.query(Friend).filter_by(friend_one=accept_id, friend_two=user_id, status=1).all()

    friendship[0].status = 2
    db.session.commit()

def request_new_friend(user_id, request_id):
    """Accept a friend request by changing the status from pending (1) to confirmed (2)"""
    current_time = datetime.now()
    friend = Friend(friend_one=user_id, 
                                friend_two=request_id, 
                                status=1,
                                fcreated_at=current_time)
    db.session.add(friend)
    db.session.commit()

def delete_friend(user_id, friend_id):

    friendship = db.session.query(Friend).filter_by(friend_one=friend_id, friend_two=user_id).first() or db.session.query(Friend).filter_by(friend_one=user_id, friend_two=friend_id).first()

    db.session.delete(friendship)
    db.session.commit()

