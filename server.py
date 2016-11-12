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

    friend_id_names = find_friends(user_id)
    sugg_id_names = suggest_friends(user_id)
    pend_id_names = pending_friends(user_id)

    return render_template('profile.html', user=user, 
                                        friend_id_names=friend_id_names, 
                                        sugg_id_names=sugg_id_names,
                                        pend_id_names=pend_id_names,
                                        key=key,
                                        rest_add=rest_add)

@app.route('/profile/<user_id>', methods=['POST'])
def process_add_rest(user_id):
    """Adds a restaurant to a user's To-eat List"""

    user_id = session['user_id']
    query = request.form.get('search')
    yes = request.form.get('yes')
    no = request.form.get('no')
    tracking_review = request.form.get('tracking_review')
    tracking_note = request.form.get('tracking_note')

    if yes:
        response = True
    if no:
        response = False

    create_trackings_and_rests(user_id, query, response, tracking_note, tracking_review)

    return redirect('/profile/{}'.format(user_id))

@app.route('/accept_friend', methods=['GET'])
def process_accept_friend():
    """Accepts a friends request"""

    accept_id = request.args.get('accept_id')
    user_id = session['user_id']
    accept_new_friend(accept_id, user_id)
    return redirect('/profile/{}'.format(user_id))

@app.route('/request_friend', methods=['GET'])
def process_request_friend():
    """Requests a friend"""

    user_id = session['user_id']
    request_id = request.args.get('request_id')
    request_new_friend(user_id, request_id)
    return redirect('/profile/{}'.format(user_id))

@app.route('/tracking/<tracking_id>')
def display_tracked_rest(tracking_id):
    """Show details for a user's tracked restaurant."""

    user_id = session['user_id']
    user = User.query.get(user_id)
    tracking = Tracking.query.get(tracking_id)
    address = tracking.restaurant.address
    price = int(tracking.restaurant.price)
    hours = tracking.restaurant.bus_hours
   
    formatted_add = address.split(',')
    add_1 = ''

    if address != None:
        if formatted_add[-1] == ' United States':
            for add in formatted_add[:-1]:
                add_1 = add_1 + add.encode('utf-8') + ','
        else:
            for add in formatted_add:
                add_1 = add_1 + add.encode('utf-8') + ','

    add_1 = add_1[:-1]

    db_reviews = tracking.restaurant.rest_review
    db_reviews = db_reviews.split('|')

    all_reviews = []

    if db_reviews != None:
        for rev in db_reviews:
            rev = rev.encode('utf-8')
            all_reviews.append(rev)

    price = '$' * price

    return render_template('tracking.html', user=user, tracking=tracking, key=key, add_1=add_1, all_reviews=all_reviews, price=price, hours=hours)

@app.route('/manage/<tracking_id>', methods=['GET'])
def manage_tracking(tracking_id):
    """Allows a user to update visited status or delete a tracking"""
    user_id = session['user_id']
    update = request.args.get('update')
    tracking_id = request.args.get('tracking_id')
    managed_tracking = Tracking.query.get(tracking_id)
   
    if update == 'True':
        managed_tracking.visited = True
        db.session.commit()
    elif update == 'Delete':
        db.session.delete(managed_tracking)
        db.session.commit()
    flash('Your To-Eat list has been updated with your changes.')
    return redirect('/profile/{}'.format(user_id))  

@app.route('/friend_profile')
def display_friend_profile():
    """Displays user's public profile page"""
    user_id = session['user_id']
    friend_id = request.args.get('friend_id')
    friend = User.query.get(friend_id)
    friend_id_names = find_friends(friend_id)

    rest_add = []
    for ft in friend.trackings:
        address = ''
        if ft.restaurant.address != None:
            formatted_add = ft.restaurant.address.split(',')
            if formatted_add[-1] == ' United States':
                for fa in formatted_add[:-1]:
                    address = address + fa.encode('utf-8') + ','
            else:
                for fa in formatted_add:
                    address = address + fa.encode('utf-8') + ','
        rest_add.append(address[:-1])

    return render_template('friend.html', friend=friend, 
                                    rest_add=rest_add, 
                                    friend_id_names=friend_id_names)


###QUERIES & FUNCTIONS BELOW###
###TODO: Move to separate file###
def create_trackings_and_rests(user_id, query, response, tracking_note, tracking_review):
    """Checks for existing trackings and restaurants and adds new entries"""

    query = query.split(',')
    info = get_rest_info(query)
    # Using separate function, gets all restaurant details from Google Places
    rest_name, city, address, lat, lng, photo, placeid, price, rating, bus_hours, rest_review = info
    # Unpacks all information into separate variables for use in db insertions below
    rest_review = rest_review.encode('utf-8')
    current_time = datetime.now()
    # Current time for db insertions below
    match = Restaurant.query.filter_by(rest_name=query[0]).all()
    # Gets a list of all restaurant objects that have a name that
    # matches the queried restaurant.
    if len(match) == 1:
    # Handles when there is one match for the query in the db.
        rest = match[0]
        # Isolates the single object in the match list
        all_trackings = db.session.query(Tracking).filter_by(user_id=user_id, rest_id=rest.rest_id).all()
        # Gets a list of all tracking objects that 
        # have the user's user_id and the queried rest's rest_id
        if len(all_trackings) == 1:
        # Handles when there is already one tracking for the restaurant
            flash('This restaurant already exists in your To-eat List.')
        elif len(all_trackings) == 0:
        # Handles when there is no tracking for the restaurant
            if response == False:
                if len(tracking_note) == 0:
                    tracking_note = None
                tracking = Tracking(user_id=user_id,
                    rest_id=rest.rest_id,
                    visited=response,
                    tracking_note=tracking_note,
                    tracking_review=None,
                    tcreated_at=current_time)
                db.session.add(tracking)
                db.session.commit()
                flash('You have successfully added a restaurant.')
            elif response == True:
                if len(tracking_review) == 0:
                    tracking_review = None
                tracking = Tracking(user_id=user_id,
                    rest_id=rest.rest_id,
                    visited=response,
                    tracking_note=None,
                    tracking_review=tracking_review,
                    tcreated_at=current_time)
                db.session.add(tracking)
                db.session.commit()
                flash('You have successfully added a restaurant.')
        else:
        # Handles when there are duplicate trackings for a restaurant
        # Deletes all but the first trackings
            for at in all_trackings[1:]:
                db.session.delete(at)
                db.session.commit() 
    elif len(match) == 0:
    # Handles when there are no matches for the query in the db.
    # Inserts into both restaurants table and trackings table.
    # When there is no match in the restaurants table, there is necessarily
    # no tracking for that queried restaurant. 
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
        # Creates a new restaurant object
        new_rest_id = restaurant.rest_id
        # Gets newly created rest_id for the tracking instantiation below
        tracking = Tracking(user_id=user_id,
                        rest_id=new_rest_id,
                        visited=False,
                        tracking_note=tracking_note,
                        tracking_review=None,
                        tcreated_at=current_time)
        db.session.add(tracking)
        db.session.commit()
        # Creates new tracking object 
        flash('You have successfully added a restaurant.')
        # return redirect('/profile/{}'.format(user_id)) 
    else:
    # Handles if there are duplicate matches in the rest table.
        for m in match[1:]:
            db.session.delete(m)
            db.session.commit()

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
    

if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0", debug=True)