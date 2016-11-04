import os
from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Restaurant, Tracking, Friend, Status
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from datetime import datetime

key = os.environ["G_PLACES_KEY"]

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """Renders homepage"""

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

@app.route('/profile/<user_id>')
def display_profile(user_id):
    """Displays user's profile page"""

    user = User.query.get(user_id)
    friend_id_names = find_friends(user_id)

    return render_template('profile.html', user=user, friend_id_names=friend_id_names)

@app.route('/public_profile/<user_id>')
def display_public_profile(user_id):
    """Displays user's public profile page"""

    return 'Public Profile'

###QUERIES BELOW###
###TODO: Move to separate file###
def find_friends(user_id):
    """Given a user_id, returns a list of tuples with a friend's full name and user_id"""

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

if __name__ == "__main__":

    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")