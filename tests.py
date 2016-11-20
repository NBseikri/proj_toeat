from unittest import TestCase
from server import app
from model import connect_to_db, db, example_data, User, Restaurant, Tracking, Friend, Status
from flask import jsonify
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from datetime import datetime
import decimal
from flask.ext.bcrypt import Bcrypt
from helper_functions import create_user, filter_trackings, sort_trackings, format_add, find_friends, suggest_friends, pending_friends

class MyAppUnitTestCase(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        # import pdb; pdb.set_trace()

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        # connect_to_db("postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()


    def test_create_user(self):
        self.assertEqual(create_user("rgreene", "rachel@rachel.com", "$2b$12$k49t/1ynDbTSR1qi2mRvfu645p1STWnwQ6petkxtM5Yz8rd.TVySy", "Rachel", "Greene", datetime.now()), 
            (User.query.filter(User.username == "rgreene").first()))
        self.assertTrue(User.query.filter(User.username == "rgreene").first())

    def test_filter_trackings(self):
        user = User.query.filter(User.username == "mgellar").first()
        self.assertTrue(filter_trackings(user.user_id, "not_visited"), ({'data' : [{
            "tracking_id" : 2,
            "visited" : "On your To-eat List.",
            "rest_name" : "Hot Cakes",
            "tracking_url" : "/tracking/2",
            "photo" : "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CmskewAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
            "city" : "Seattle"}]}))

    def test_sort_trackings(self):
        user = User.query.filter(User.username == "mgellar").first()
        self.assertTrue(sort_trackings(user.user_id, "low_price"), ({'data' : [{
            "tracking_id" : 1,
            "visited" : "You've eaten here.",
            "rest_name" : "Mr. Holmes Bakehouse",
            "tracking_url" : "/tracking/1",
            "photo" : "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
            "city" : "San Francisco"},
            {"tracking_id" : 2,
            "visited" : "On your To-eat List.",
            "rest_name" : "Hot Cakes",
            "tracking_url" : "/tracking/2",
            "photo" : "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CmskewAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
            "city" : "Seattle"}]}))

    def test_format_add(self):
        user = User.query.filter(User.username == "mgellar").first()
        self.assertTrue(format_add(user.user_id), ["1042 Larkin St, San Francisco, CA", "1042 Market St, Seattle, WA 98000"])

    def test_find_friends(self):
        user = User.query.filter(User.username == "mgellar").first()
        user2 = User.query.filter(User.username == "cbing").first()
        self.assertEqual(find_friends(user.user_id), [(user2.user_id, 'Chandler Bing')])

    def test_suggest_friends(self):
        user = User.query.filter(User.username == "mgellar").first()
        user4 = User.query.filter(User.username == "jtribiani").first()
        self.assertEqual(suggest_friends(user.user_id), [(user4.user_id, 'Joey Tribiani')])

    def test_pending_friends(self):
        user = User.query.filter(User.username == "mgellar").first()
        user3 = User.query.filter(User.username == "pbuffet").first()
        self.assertEqual(pending_friends(user.user_id), [(user3.user_id, 'Phoebe Buffet')])

if __name__ == "__main__":
    import unittest
    unittest.main()
