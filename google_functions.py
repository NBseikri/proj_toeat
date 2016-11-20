import os
from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Restaurant, Tracking, Friend, Status
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from datetime import datetime
import requests
import decimal
import functions

key = os.environ["G_PLACES_KEY"]

def get_rest_info(query):
    """Pulls Search and Detail info from Google Places based on a query"""

    search_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    details_url = 'https://maps.googleapis.com/maps/api/place/details/json'
    gphotos_url = 'https://maps.googleapis.com/maps/api/place/photo/json'

    # Google Places Search payload
    payload = {
        'key': key,
        'query': query
    }

    search_req = requests.get(search_url, params=payload)
    search_json = search_req.json()
    results = search_json['results']

    # Accessing just the results dictionary from the results
    results_dict = results[0]
    
    # Restaurant name from search
    rest_name = results_dict['name']

    # Address from search
    address = results_dict['formatted_address']

    # Lat from search 
    lat = results_dict['geometry']['location']['lat']

    # Lng from search
    lng = results_dict['geometry']['location']['lng']

    # Photo from search
    photos = results_dict['photos']
    if photos is not []:
        photo_dict = photos[0]
        photo_reference = photo_dict.get('photo_reference', None)

    # Payload for photo payload that includes photo reference from search
    gphoto_payload = {
        'key' : key,
        'photoreference' : photo_reference,
        'maxwidth' : 200
    }

    if photo_reference:
        photo_url = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=%s&photoreference=%s&key=%s' % (gphoto_payload.get('maxwidth'), gphoto_payload.get('photoreference'), gphoto_payload.get('key'))
    else:
        photo_url = None

    # Place ID from search; needed for Google Places Details call below
    placeid = results_dict['place_id']

    # Price level from search
    price = results_dict.get('price_level', None)
    if price == "":
        price = None

    # Rating from search
    rating = results_dict['rating']
    if rating == "":
        rating = None

    # Google Places Details payload using Place ID from Google Places Search 
    id_payload = {
        'key' : key,
        'placeid' : placeid
    }

    details_req = requests.get(details_url, params=id_payload)
    details_json = details_req.json()
    d_results = details_json['result']

    #City from details
    city = d_results['address_components'][3]['long_name']
    if city == "":
        city = None

    # Business hours from details
    bus_hours = d_results.get('weekday_text', None)
    # Used .get() here because weekday_text appears to be the only Place Search
    # result that isn't always a key in the dictionary
    if bus_hours is None:
        bus_hours = None

    # Reviews from details
    reviews = d_results['reviews']
    all_reviews = ""
    if reviews != []:
        for review in reviews:
            text = review['text']
            if text: 
                # enc_text = text.encode("utf-8")
                # all_reviews = all_reviews + enc_text + '|'
                all_reviews = all_reviews + text + '|'
            else:
                all_reviews = None
    else:
        all_reviews = None
    
    return rest_name, city, address, lat, lng, photo_url, placeid, price, rating, bus_hours, all_reviews