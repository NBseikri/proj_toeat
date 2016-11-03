"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func
from model import User, Restaurant, Tracking, Friend, Status, connect_to_db, db
from server import app


# def load_users():
#     """Load users from u.user into database."""

#     print "Users"

#     for i, row in enumerate(open("seed_data/users.csv")):
#         row = row.rstrip()
#         user_id, password, first_name, last_name, email = row.split(",")

#         user = User(password=password,
#                     first_name=first_name,
#                     last_name=last_name,
#                     email=email)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(user)

#         # provide some sense of progress
#         if i % 100 == 0:
#             print i

#     # Once we're done, we should commit our work
#     db.session.commit()


# def load_restaurants():
#     """Load movies from u.item into database."""

#     print "Restaurants"

#     for i, row in enumerate(open("seed_data/restaurants.csv")):
#         row = row.rstrip()

#         # clever -- we can unpack part of the row!
#         rest_id, name, city  = row.split(",")

#         restaurant = Restaurant(name=name, city=city)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(restaurant)

#         # provide some sense of progress
#         if i % 100 == 0:
#             print i

#     # Once we're done, we should commit our work
#     db.session.commit()


def load_restaurants():
    """Load ratings from u.data into database."""

    print "Restaurant"

    for row in open("restaurants_ex.csv"):
        row = row.rstrip()

        rest_id, rest_name, city, address, lat, lng, photo, placeid, price, rating, bus_hours, rest_review, rcreated_at = row.split(",")

        rest_id = int(rest_id)
        lat = float(lat)
        lng = float(lng)
        price = int(price)
        rating = float(rating)
        rcreated_at = None

        restaurant = Restaurant(rest_id=rest_id,
                            rest_name=rest_name,
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
                            rcreated_at=rcreated_at)

        # We need to add to the session or it won't ever be stored
        db.session.add(restaurant)

        # provide some sense of progress
        if i % 1000 == 0:
            print i

            # An optimization: if we commit after every add, the database
            # will do a lot of work committing each record. However, if we
            # wait until the end, on computers with smaller amounts of
            # memory, it might thrash around. By committing every 1,000th
            # add, we'll strike a good balance.

            # db.session.commit()

    # Once we're done, we should commit our work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_restaurants()
