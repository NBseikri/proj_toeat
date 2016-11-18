from unittest import TestCase
from server import app
from model import connect_to_db, db, example_data, User, Restaurant, Tracking, Friend, Status
from flask import jsonify
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from datetime import datetime
import decimal
from flask.ext.bcrypt import Bcrypt
from helper_functions import create_user, filter_trackings, sort_trackings

class MyAppUnitTestCase(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        # connect_to_db("postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

        #COMMENT
        #ANOTHER COMMENT

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_create_user(self):
        self.assertEqual(create_user("rgreene", "rachel@rachel.com", "$2b$12$k49t/1ynDbTSR1qi2mRvfu645p1STWnwQ6petkxtM5Yz8rd.TVySy", "Rachel", "Greene", datetime.now()), 
            (User.query.filter(User.username == "rgreene").first()))
        self.assertTrue(User.query.filter(User.username == "rgreene").first())

    def test_filter_trackings(self):
        self.assertTrue(filter_trackings(1, "not_visited"), ({'data' : [{
            "tracking_id" : 2,
            "visited" : "On your To-eat List.",
            "rest_name" : "Hot Cakes",
            "tracking_url" : "/tracking/2",
            "photo" : "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CmskewAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
            "city" : "Seattle"}]}))

    def test_sort_trackings(self):
        self.assertTrue(sort_trackings(1, "low_price"), ({'data' : [{
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


    # restaurant1 = Restaurant(rest_name="Mr. Holmes Bakehouse", 
    #             city="San Francisco",
    #             address="1042 Larkin St, San Francisco, CA 94109, United States",
    #             lat=37.7876365,
    #             lng=-122.4182803,
    #             photo="https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
    #             placeid="ChIJT0h_9pOAhYAR-3iNZNso3xk",
    #             price=1,
    #             rating=4.2,
    #             bus_hours=None,
    #             rest_review="Fantastic cruffins! Omg!",
    #             rcreated_at=datetim

if __name__ == "__main__":
    import unittest
    unittest.main()
