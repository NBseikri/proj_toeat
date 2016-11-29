import os
from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session, Markup
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Restaurant, Tracking, Friend, Status
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from datetime import datetime
import requests
import decimal
from google_functions import get_rest_info
from helper_functions import create_user, filter_trackings, sort_trackings, format_add, find_friends, suggest_friends, pending_friends, accept_new_friend, request_new_friend, delete_friend, tracking_cities, create_tracking, create_restaurant, get_all_trackings, get_match
from flask.ext.bcrypt import Bcrypt


key = os.environ["G_PLACES_KEY"]
app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined
bcrypt = Bcrypt(app)

@app.route('/')
def homepage():
    """Renders homepage"""

    if 'user_id' in session and session['user_id'] is not None:
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
    user = User.query.filter_by(email=email).first()

    if user:
        if bcrypt.check_password_hash(user.password, password):
            flash('You have successfully logged in.')
            session['user_id'] = user.user_id
            return redirect('/profile/{}'.format(user.user_id))
        else:
            flash("Sorry, that password is incorrect. Please try again.")
            return redirect('/login')

    else:
        flash("I'm sorry that email is not in our system. Please try again.")
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
    """Process registration form"""

    username = request.form.get('username')
    email = request.form.get('email').encode('utf-8')
    password = request.form.get('password')
    encrypted_pw = bcrypt.generate_password_hash(password)
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    ucreated_at = datetime.now()
    emails = User.query.filter_by(email=email).all()

    if emails:
        flash('An account is already associated with the email address you entered. Please login.')
        return redirect('/login')
    else:
        user = create_user(username, email, encrypted_pw, first_name, last_name, ucreated_at)
        session['user_id'] = user.user_id
        flash('You have successfully created an account.')
        return redirect('/')

@app.route('/profile/<user_id>', methods=['GET'])
def display_profile(user_id):
    """Displays user's profile page"""

    user = User.query.get(user_id)
    friend_id_names = find_friends(user.user_id)
    sugg_id_names = suggest_friends(user.user_id)
    pend_id_names = pending_friends(user.user_id)
    cities = tracking_cities(user.user_id)
    if session['user_id'] == user.user_id:
        return render_template('profile2.html', user=user, 
                                        friend_id_names=friend_id_names, 
                                        sugg_id_names=sugg_id_names,
                                        pend_id_names=pend_id_names,
                                        cities=cities,
                                        key=key)
    else: 
        flash('Please return to your profile or login.')
        return redirect('/login')

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


@app.route('/filter_rest', methods=['GET'])
def filter_rest():

    user_id = session['user_id']
    user = User.query.get(user_id)
    filter_by = request.args.get('filter')
    return jsonify(filter_trackings(user_id, filter_by))

@app.route('/sort_rest', methods=['GET'])
def sort_rest():

    user_id = session['user_id']
    user = User.query.get(user_id)
    cities = tracking_cities(user.user_id)
    sort_by = request.args.get('sort')

    if sort_by in cities:
        for city in cities:
            if sort_by == city:
                sort_by = city

    return jsonify(sort_trackings(user_id, sort_by))

@app.route('/accept_friend', methods=['GET'])
def process_accept_friend():
    """Accepts a friends request"""

    accept_id = request.args.get('accept_id')
    user_id = session['user_id']
    accept_new_friend(accept_id, user_id)
    ###AJAX ATTEMPT###
                # friend = User.query.get(accept_id)

                # friend_dict = {"friend_id" : friend.user_id,
                #         "name" : friend.first_name + " " + friend.last_name}
                # return jsonify(friend_dict)
                # # return "Now friends!"
    ###END AJAX ATTEMPT###
    return redirect('/profile/{}'.format(user_id))


@app.route('/request_friend', methods=['GET'])
def process_request_friend():
    """Requests a friend"""

    user_id = session['user_id']
    request_id = request.args.get('request_id')
    request_new_friend(user_id, request_id)
    return redirect('/profile/{}'.format(user_id))

@app.route('/delete', methods=['GET'])
def process_delete_friend():
    """Deletes a friend from a user's friend list"""

    user_id = session['user_id']
    friend_id = request.args.get('friend_id')
    delete_friend(user_id, friend_id)
    return redirect('/profile/{}'.format(user_id))

@app.route('/tracking/<tracking_id>')
def display_tracked_rest(tracking_id):
    """Show details for a user's tracked restaurant."""

    user_id = session['user_id']
    user = User.query.get(user_id)
    tracking = Tracking.query.get(tracking_id)
    address = tracking.restaurant.address
    if tracking.restaurant.price:
        price = (int(tracking.restaurant.price))
        price = '$' * price
    else: 
        price = None
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
    all_reviews = []
  
    if db_reviews:
        db_reviews = db_reviews.split('|')
        for rev in db_reviews:
            # rev = rev.decode('utf-8')
            all_reviews.append(rev)

    return render_template('tracking.html', user=user, tracking=tracking, key=key, add_1=add_1, all_reviews=all_reviews, price=price, hours=hours)

@app.route('/manage/<tracking_id>', methods=['GET'])
def manage_tracking(tracking_id):
    """Allows a user to update visited status or delete a tracking"""
    user_id = session['user_id']
    update = request.args.get('update')
    tracking_id = request.args.get('tracking_id')
    updated_review = request.args.get('up_tracking_review')
    managed_tracking = Tracking.query.get(tracking_id)
   
    if update == 'True':
        managed_tracking.visited = True
        if len(updated_review) > 0 and updated_review != " ":
            managed_tracking.tracking_review = updated_review
        else: 
            managed_tracking.tracking_review = None
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
    rest_add = format_add(friend_id)
    return render_template('friend.html', friend=friend, 
                                    rest_add=rest_add, 
                                    friend_id_names=friend_id_names)

def create_trackings_and_rests(user_id, query, response, tracking_note, tracking_review):
    """Given user input, creates trackings and restaurants"""

    query = query.split(',')
    info = get_rest_info(query)
    # Using separate function, gets all restaurant details from Google Places
    rest_name, city, address, lat, lng, photo, placeid, price, rating, bus_hours, rest_review = info
    # Unpacks all information into separate variables for use in db insertions below
    # rest_review = rest_review.encode('utf-8')
    current_time = datetime.now()
    # Current time for db insertions below
    match = get_match(query)
    # Gets a list of all restaurant objects that have a name that
    # matches the queried restaurant.
    if len(match) == 1:
    # Handles when there is one match for the query in the db.
        rest = match[0]
        # Isolates the single object in the match list
        all_trackings = get_all_trackings(user_id, rest.rest_id)
        # Gets a list of all tracking objects that 
        # have the user's user_id and the queried rest's rest_id
        if len(all_trackings) == 1:
        # Handles when there is already one tracking for the restaurant
            flash('This restaurant already exists in your To-eat List.')
        elif len(all_trackings) == 0:
        # Handles when there is no tracking for the restaurant
            if response == False:
                # Handles if user has not been the restaurant
                if len(tracking_note) == 0:
                    tracking_note = None
                    # Converts an empty tracking note to None for db consistency
                create_tracking(user_id, rest.rest_id, False, tracking_note, None, current_time)
                # Creates a new tracking object; inserts tracking into db 
                flash('You have successfully added a restaurant.')
                # Confirms update upon redirect
            elif response == True:
                # Handles when a user has been to a restaurant
                if len(tracking_review) == 0:
                    tracking_review = None
                    # Converts an empty tracking review to None for db consistency
                create_tracking(user_id, rest.rest_id, True, None, tracking_review, current_time)
                # Creates a new tracking object; insterts tracking into db
                flash('You have successfully added a restaurant.')
                # Confirms update upon redirect
    elif len(match) == 0:
    # Isolates the single object in the match list.
    # Handles when there are no matches for the query in the db.
    # Inserts into both restaurants table and trackings tables.
    # When there is no match in the restaurants table, there is necessarily
    # no tracking for that queried restaurant. 
        restaurant = create_restaurant(rest_name, city, address, lat, lng, photo, placeid, price, rating, bus_hours, rest_review, current_time)
        # Creates a new restaurant object
        new_rest_id = restaurant.rest_id
        # Gets newly created rest_id for the tracking instantiations below
        if response == False:
            # Handles if the user has not been to a restaurant
            if len(tracking_note) == 0:
                tracking_note = None
                # Converts an empty tracking note to None for db consistency
            create_tracking(user_id, new_rest_id, False, tracking_note, None, current_time)
            # Creates a new tracking object; insterts tracking into db
            flash('You have successfully added a restaurant.')
            # Confirms update upon redirect
        elif response == True:
            # Handles if the user has been to a restaurant
            if len(tracking_review) == 0:
                tracking_review = None
                # Converts to an empty tracking review to None for db consistency
            create_tracking(user_id, restaurant.rest_id, True, None, tracking_review, current_time)
            # Creates new tracking object; inserts tracking into db
            flash('You have successfully added a restaurant.')


if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = True
    connect_to_db(app)
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0", debug=True)