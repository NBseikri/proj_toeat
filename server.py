import os
from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Restaurant, Tracking, Friend, Status
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from datetime import datetime
import requests
import decimal
from functions import get_rest_info

key = os.environ["G_PLACES_KEY"]

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Renders homepage"""
    if session['user_id'] != None:
        user_id = session['user_id']
        return redirect('/profile/{}'.format(user_id))
    else:
        return render_template('homepage.html')

@app.route('/login', methods=['GET'])
def display_login_form():
    """Displays homepage"""

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def process_login():
    """Processes login"""

    email = request.form.get('email')
    password = request.form.get('password')

    user_query = db.session.query(User).filter_by(email=email)
    try:
        user = user_query.one()
    except NoResultFound:
        print "No user instance found for this email in db."
        user = None
    except MultipleResultsFound:
        print "Multiple user instances found for this email in db."
        user = user_query.first()

    if user:
        if user.password == password:
            flash('You have successfully logged in.')
            session['user_id'] = user.user_id
            return redirect('/profile/{}'.format(user.user_id))
        else:
            flash("Sorry, that password is incorrect. Please try again.")
            return redirect('/login')

    else:
        flash("""I'm sorry that email is not in our system. Please try again
                or go to our registration page to create a new account.""")
        return redirect('/login')

@app.route('/logout')
def process_logout():

    session['user_id'] = None
    flash("You've successfully logged out!")
    return redirect('/')

@app.route('/registration', methods=['GET'])
def display_registration_form():
    """Displays registration form"""

    return render_template('registration.html')

@app.route('/registration', methods=['POST'])
def process_registration():
    """Processes registration form"""

    username = request.form.get('username')
    email = request.form.get('email').encode('utf-8')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    ucreated_at = datetime.now()

    emails = User.query.filter_by(email=email).all()

    if emails:
        flash('An account is already associated with the email address you entered. Please login.')
        return redirect('/login')
    else: 
        user = User(username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            ucreated_at=ucreated_at)

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.user_id
        flash('You have successfully created an account.')
        return redirect('/')

@app.route('/profile/<user_id>', methods=['GET'])
def display_profile(user_id):
    """Displays user's profile page"""

    user = User.query.get(user_id)
    friend_id_names = find_friends(user_id)
    sugg_id_names = suggest_friends(user_id)
    pend_id_names = pending_friends(user_id)

    return render_template('profile.html', user=user, 
                                        friend_id_names=friend_id_names, 
                                        sugg_id_names=sugg_id_names,
                                        pend_id_names=pend_id_names,
                                        key=key)

# @app.route('/profile/<user_id>', methods=['POST'])
# def process_add_rest(user_id):
#     """Adds a restaurant to a user's To-eat List"""

#     user_id = session['user_id']
#     # Gets user_id from session
#     query = request.form.get('search')
#     query = query.split(',')
#     # Gets autocompleted search from form
#     tracking_note = request.form.get('tracking_note')
#     # Gets tracking note from form
#     info = get_rest_info(query)
#     # Using separate function, gets all restaurant details from Google Places
#     rest_name, city, address, lat, lng, photo, placeid, price, rating, bus_hours, rest_review = info
#     # Unpacks all information into separate variables for use in db insertions below
#     current_time = datetime.now()
#     # Current time for db insertions below

#     rests = Restaurant.query.all()
#     # Returns list all restaurant objects
#     # I previously had a query that searched on the name of the queried restaurant
#     # but it threw an error when a restaurant was not in the db so I am now
#     # iterating through a list of restuarant objects to avoid the error. 
#     for r in rests:
#         print r
#         print r.rest_name
#         print 'THIS IS THE REST_ID!!!!!!', r.rest_id
#         print query[0]
#         print r.rest_name == query[0]
#         print '**************************'
#         # Iterates through list and evaluates each restaurant object
#         if r.rest_name == query[0]:
#         # Checks to see if an existing restaurant name matches the queried restaurant
#             print '====================='
#             exists = check_existing_trackings(user_id, r.rest_id)
#             print exists
#             print '&&&&&&&&&&&&&&&&&&&'
#             # When there is a match, checks whether user already has a tracking for
#             # the queried restaurant
#             print "The rest already exists in this tracking: ", exists
#             if exists:
#             # Handles if the user is already tracking the restaurant    
#                 flash('This restaurant is already in your To-eat List.')
#                 return redirect('/profile/{}'.format(user_id))
#                 # TODO: BUILD FEATURE TO UPDATE TRACKING
#             else:
#             # Handles when the user is not already tracking a restaurant in the db
#                 tracking = Tracking(user_id=user_id,
#                                         rest_id=r.rest_id,
#                                         visited=False,
#                                         tracking_note=tracking_note,
#                                         tracking_review=None,
#                                         tcreated_at=current_time)
#                 db.session.add(tracking)
#                 db.session.commit()
#                 # Adds tracking to db
#                 flash('You have successfully added a restaurant.')
#                 #return redirect('/profile/{}'.format(user_id))
#         else:
#             print 'ELSE**********************'
#         # Handles a queried restaurant that is not already in the db 
#             # restaurant = Restaurant(rest_name=rest_name, 
#             #                         city=city, 
#             #                         address=address, 
#             #                         lat=lat, 
#             #                         lng=lng, 
#             #                         photo=photo, 
#             #                         placeid=placeid, 
#             #                         price=price, 
#             #                         rating=rating, 
#             #                         bus_hours=bus_hours, 
#             #                         rest_review=rest_review,
#             #                         rcreated_at=current_time)
#             # # Creates a new restaurant object
#             # # db.session.add(restaurant)
#             # # db.session.commit()
#             # new_rest_id = restaurant.rest_id
#             # tracking = Tracking(user_id=user_id,
#             #                 rest_id=new_rest_id,
#             #                 visited=False,
#             #                 tracking_note=tracking_note,
#             #                 tracking_review=None,
#             #                 tcreated_at=current_time)
#             # # Creates new tracking object for the newly added restaurant 
#             # # for the user
#             # # db.session.add(tracking)
#             # # db.session.commit()
#             # flash('You have successfully added a restaurant.')
#             #return redirect('/profile/{}'.format(user_id)) 
#         return 'Hi'      

# @app.route('/add_friend/<user_id>', methods=['POST'])
# def add_friend(user_id):

#     user_id = session['user_id']
#     other_friend = request.form.get('add')
#     accept_new_friend(user_id, other_friend)

#     flash('This restaurant is already in your To-eat List.')
#     return redirect('/profile/{}'.format(user_id))

@app.route('/public_profile/<user_id>')
def display_public_profile(user_id):
    """Displays user's public profile page"""

    return 'Public Profile'

###QUERIES BELOW###
###TODO: Move to separate file###
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

    return sugg_id_names

def pending_friends(user_id):
    """Given a user_id, returns a list of tuples with a pending friend's user_id and full name"""

    all_friends = Friend.query.filter(Friend.status==1).all()
    
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

# def add_new_friend(passed_user_id, other_friend):

#     current_time = datetime.now()
    
#     friend = Friend(friend_one=passed_user_id,
#                         friend_two=other_friend,
#                         status=1,
#                         fcreated_at=current_time)
#     db.session.add(friend)
#     db.session.commit()

# def accept_new_friend(passed_user_id, other_friend):


def check_existing_trackings(passed_user_id, passed_rest_id):
    """Returns true or false if a user is already tracking a specific restaurant"""

    all_trackings = Tracking.query.filter(Tracking.user_id==passed_user_id).all()

    for tracking in all_trackings:
        print tracking.rest_id, passed_rest_id
        if tracking.rest_id == passed_rest_id:
            return True
        else:
            return False

if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")