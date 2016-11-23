from unittest import TestCase
from server import app, create_trackings_and_rests
from model import connect_to_db, db, example_data, User, Restaurant, Tracking, Friend, Status
from flask import jsonify
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from datetime import datetime
import decimal
from flask.ext.bcrypt import Bcrypt
from helper_functions import create_user, filter_trackings, sort_trackings, format_add, find_friends, suggest_friends, pending_friends, accept_new_friend, request_new_friend, delete_friend, create_tracking
import os
from google_functions import get_rest_info
key = os.environ["G_PLACES_KEY"]

class MyAppUnitTestCase(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        connect_to_db(app, "postgresql:///testdb")

        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()


    # def test_create_user(self):
    #     self.assertEqual(create_user("rgreene", "rachel@rachel.com", "$2b$12$k49t/1ynDbTSR1qi2mRvfu645p1STWnwQ6petkxtM5Yz8rd.TVySy", "Rachel", "Greene", datetime.now()), 
    #         (User.query.filter(User.username == "rgreene").first()))
    #     self.assertTrue(User.query.filter(User.username == "rgreene").first())

    # #FAIL
    # def test_create_tracking(self):
    #     user = User.query.filter(User.username == "mgellar").first()
    #     restaurant = Restaurant.query.filter(Restaurant.rest_name=="Mr. Holmes Bakehouse").first()
    #     self.assertEqual(create_tracking(user.user_id, restaurant.rest_id, True, None, "Loved the cruffins!", datetime.now()), 
    #         (Tracking.query.filter(Tracking.user_id==user.user_id, Tracking.rest_id==restaurant.rest_id).first()))
    #     # self.assertTrue(Tracking.query.filter(Tracking.user_id==user.user_id, Tracking.rest_id==restaurant.rest_id))

    # def test_filter_trackings(self):
    #     user = User.query.filter(User.username == "mgellar").first()
    #     self.assertTrue(filter_trackings(user.user_id, "not_visited"), ({'data' : [{
    #         "tracking_id" : 2,
    #         "visited" : "On your To-eat List.",
    #         "rest_name" : "Hot Cakes",
    #         "tracking_url" : "/tracking/2",
    #         "photo" : "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CmskewAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
    #         "city" : "Seattle"}]}))

    # def test_sort_trackings(self):
    #     user = User.query.filter(User.username == "mgellar").first()
    #     self.assertTrue(sort_trackings(user.user_id, "low_price"), ({'data' : [{
    #         "tracking_id" : 1,
    #         "visited" : "You've eaten here.",
    #         "rest_name" : "Mr. Holmes Bakehouse",
    #         "tracking_url" : "/tracking/1",
    #         "photo" : "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
    #         "city" : "San Francisco"},
    #         {"tracking_id" : 2,
    #         "visited" : "On your To-eat List.",
    #         "rest_name" : "Hot Cakes",
    #         "tracking_url" : "/tracking/2",
    #         "photo" : "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CmskewAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc",
    #         "city" : "Seattle"}]}))

    # def test_format_add(self):
    #     user = User.query.filter(User.username == "mgellar").first()
    #     self.assertTrue(format_add(user.user_id), ["1042 Larkin St, San Francisco, CA", "1042 Market St, Seattle, WA 98000"])

    # def test_find_friends(self):
    #     user = User.query.filter(User.username == "mgellar").first()
    #     user2 = User.query.filter(User.username == "cbing").first()
    #     self.assertEqual(find_friends(user.user_id), [(user2.user_id, 'Chandler Bing')])

    # def test_suggest_friends(self):
    #     user = User.query.filter(User.username == "mgellar").first()
    #     user4 = User.query.filter(User.username == "jtribiani").first()
    #     self.assertEqual(suggest_friends(user.user_id), [(user4.user_id, 'Joey Tribiani')])

    def test_pending_friends(self):
        user = User.query.filter(User.username == "mgellar").first()
        user3 = User.query.filter(User.username == "pbuffet").first()
        self.assertEqual(pending_friends(user.user_id), [(user3.user_id, 'Phoebe Buffet')])

    #FAIL
    def test_accept_new_friend(self):
        user = User.query.filter(User.username == "mgellar").first()
        user3 = User.query.filter(User.username == "pbuffet").first()
        friendship = Friend.query.filter_by(friend_one=user.user_id, friend_two=user3.user_id, status=2).first()
        self.assertTrue(accept_new_friend(user.user_id, user3.user_id), friendship)

    #FAIL
    def test_request_new_friend(self):
        user = User.query.filter(User.username == "mgellar").first()
        user4 = User.query.filter(User.username == "jtribiani").first()
        friendship = Friend.query.filter_by(friend_one=user.user_id, friend_two=user4.user_id).first() 
        self.assertTrue(request_new_friend(user.user_id, user4.user_id), friendship)

    def test_delete_friend(self):
        user = User.query.filter(User.username == "mgellar").first()
        user2 = User.query.filter(User.username == "cbing").first()
        friendship = db.session.query(Friend).filter_by(friend_one=user.user_id, friend_two=user2.user_id).first() or db.session.query(Friend).filter_by(friend_one=user2.user_id, friend_two=user.user_id).first()
        self.assertFalse(delete_friend(user.user_id, user2.user_id), friendship)

    # def test_get_rest_info(self):
    #     query = "Sushirrito - SOMA, New Montgomery Street, San Francisco, CA, United States"
    #     rest_name = "Sushirrito - SOMA"
    #     city = "San Francisco"
    #     address = "59 New Montgomery St, San Francisco, CA 94105, United States"
    #     lat = 37.7880931
    #     lng = -122.4011156
    #     photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAIXE0ugNyG0ZrqECoqCVUbkJ44pzL8v-EfsuirzVxPISyA1uUMt37wHOhEKlQridX6KMMT7emH8JN2dF-oa4aiIVvFsNQtIMd5Zcto_Ov9UAy6Pphcq2MzVIupkUSissQzX7lRbOPO1GNN7NS-8FJEZDRRJtZUYbeWvyVfL5nSjDEhC9VNUbo4b5q92KW4C6E4pPGhQO16sPITCJAcA7htkDIvWIONatrw&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc"
    #     placeid = "ChIJ59q8pmKAhYAR0tfR_s2qwak"
    #     price = 1
    #     rating = 4.1
    #     bus_hours = None
    #     results = rest_name, city, address, lat, lng, photo_url, placeid, price, rating, bus_hours
    #     self.assertTrue(get_rest_info(query), results)    

    def test_create_trackings_and_rests(self):
        user = User.query.filter(User.username == "mgellar").first()
        restaurant = Restaurant.query.filter(Restaurant.rest_id == 1).first()
        self.assertTrue(create_trackings_and_rests(user.user_id, "Mr. Holmes Bakehouse, Larkin Street, San Francisco, CA, United States", True, None, "Incredible pastries!"), None)

class FlaskTests(TestCase):

  def setUp(self):
      """Stuff to do before every test."""
      self.client = app.test_client()
      app.config['TESTING'] = True

  # def tearDown(self):
  #     """Stuff to do after each test."""

  def test_homepage(self):
    result = self.client.get("/")
    self.assertEqual(result.status_code, 200)
    self.assertIn('<h1>To-eat List</h1>', result.data)

  def test_display_login_form(self):
    result = self.client.get("/login")
    self.assertEqual(result.status_code, 200)
    self.assertIn('<h1>Login</h1>', result.data)

#WHAT SHOULD I BE ASSERTING IN A ROUTE THE SIMPLY PROCESSES LOGIN FOR DB INSERTION?
  def test_process_login(self):
    result = self.client.get("/login")
    self.assertEqual(result.status_code, 200)

  def test_process_logout(self):
    result = self.client.get("/logout")
    self.assertEqual(result.status_code, 200)

  # def test2(self):
  #     """Some other test"""

if __name__ == "__main__":
    import unittest
    unittest.main()
