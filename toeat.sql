--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.4
-- Dumped by pg_dump version 9.5.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'LATIN1';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: friends; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE friends (
    friend_id integer NOT NULL,
    friend_one integer,
    friend_two integer,
    status integer,
    fcreated_at timestamp without time zone
);


ALTER TABLE friends OWNER TO vagrant;

--
-- Name: friends_friend_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE friends_friend_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE friends_friend_id_seq OWNER TO vagrant;

--
-- Name: friends_friend_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE friends_friend_id_seq OWNED BY friends.friend_id;


--
-- Name: restaurants; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE restaurants (
    rest_id integer NOT NULL,
    rest_name character varying(128),
    city character varying(58),
    address character varying(256),
    lat double precision,
    lng double precision,
    photo character varying(2000),
    placeid character varying(128),
    price integer,
    rating double precision,
    bus_hours character varying(500),
    rest_review text,
    rcreated_at timestamp without time zone
);


ALTER TABLE restaurants OWNER TO vagrant;

--
-- Name: restaurants_rest_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE restaurants_rest_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE restaurants_rest_id_seq OWNER TO vagrant;

--
-- Name: restaurants_rest_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE restaurants_rest_id_seq OWNED BY restaurants.rest_id;


--
-- Name: statuses; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE statuses (
    status_id integer NOT NULL,
    status_code character varying(10) NOT NULL
);


ALTER TABLE statuses OWNER TO vagrant;

--
-- Name: statuses_status_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE statuses_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE statuses_status_id_seq OWNER TO vagrant;

--
-- Name: statuses_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE statuses_status_id_seq OWNED BY statuses.status_id;


--
-- Name: trackings; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE trackings (
    tracking_id integer NOT NULL,
    user_id integer,
    rest_id integer,
    visited boolean,
    tracking_note character varying(140),
    tracking_review text,
    tcreated_at timestamp without time zone
);


ALTER TABLE trackings OWNER TO vagrant;

--
-- Name: trackings_tracking_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE trackings_tracking_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE trackings_tracking_id_seq OWNER TO vagrant;

--
-- Name: trackings_tracking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE trackings_tracking_id_seq OWNED BY trackings.tracking_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE users (
    user_id integer NOT NULL,
    username character varying(20) NOT NULL,
    email character varying(32),
    password character varying(100) NOT NULL,
    first_name character varying(32) NOT NULL,
    last_name character varying(32) NOT NULL,
    ucreated_at timestamp without time zone NOT NULL
);


ALTER TABLE users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE users_user_id_seq OWNED BY users.user_id;


--
-- Name: friend_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY friends ALTER COLUMN friend_id SET DEFAULT nextval('friends_friend_id_seq'::regclass);


--
-- Name: rest_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY restaurants ALTER COLUMN rest_id SET DEFAULT nextval('restaurants_rest_id_seq'::regclass);


--
-- Name: status_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY statuses ALTER COLUMN status_id SET DEFAULT nextval('statuses_status_id_seq'::regclass);


--
-- Name: tracking_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY trackings ALTER COLUMN tracking_id SET DEFAULT nextval('trackings_tracking_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq'::regclass);


--
-- Data for Name: friends; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY friends (friend_id, friend_one, friend_two, status, fcreated_at) FROM stdin;
4	1	10	2	2016-11-16 23:53:26.765437
8	1	6	1	2016-11-19 22:14:54.952142
9	1	8	1	2016-11-19 22:14:57.41327
10	1	9	1	2016-11-19 22:14:59.479816
12	1	7	1	2016-11-19 22:15:53.512926
13	1	12	1	2016-11-19 22:16:01.680664
15	2	3	1	2016-11-22 01:37:30.346774
21	3	1	1	2016-11-22 23:25:07.639334
20	4	1	2	2016-11-22 23:23:24.971094
\.


--
-- Name: friends_friend_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('friends_friend_id_seq', 21, true);


--
-- Data for Name: restaurants; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY restaurants (rest_id, rest_name, city, address, lat, lng, photo, placeid, price, rating, bus_hours, rest_review, rcreated_at) FROM stdin;
2	The Pink Door	Seattle	1919 Post Alley, Seattle, WA 98101, United States	47.6103651999999968	-122.342560399999996	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAJ6aTMKK4bKimUko2uMJjqRwt5OOZPVRPKfWeiRGOCVO_dKH9MM_z4LHNMo_vDcEJqt4LWTkhayI1f7sAilCbE9xZd_M0v4bpdIkRH3kDqn1QS0M7o-U-5Rz0ORPSasyR4EnRqDHttOBXWvFyCI84i-8Eqa-SBXhQHqaYyR3sqdHEhBd8Fh9t7JSwG4tMaIIXuk9GhRKaxrvg2rih-YoAi06XO6jitdJ2A&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJ91YOzrJqkFQRKmSW0B1qrbo	2	4.29999999999999982	\N	Amazing atmosphere. Delicious food. Fun drinks and bartenders. Really cool acts. Perfect for fun night out, date, drinks with friends. There is a resident tarot card reader named Eugenia who is a Seattle treasure. Highly recommend this place!|Absolutely delicious!! I saw this place on Yelp an wanted to give it a try. I'm a vegetarian and they have a few options or us folks! I ate the lasagna and the noodles literally melted in my mouth. If your down town Seattle and you want a place elegance and wonderful ambiance, look no further!|Fantastic fish! Excellent patio with view of the bay! Incredible bread! We came for a late lunch and I plan on returning for the dinner experience!  Tricky to find.. inside the building and upstairs to the Pink Door. lol|First trip to Seattle- this place was a great choice for dinner on our first night in town. Lasagna was fantastic, and the meat and cheese plate was amazing. Great choice.|Excellent excellent Italian restaurant! Cozy and romantic setting inside, and an amazing patio looking over the waterfront! For cocktail, I had Baby & Co which was just right amount of sweetness and bubbles. For dinner, I tried their risotto which changes seasonally - they currently have crabmeat risotto. It was very light and delicious! |	2016-11-14 04:33:53.989719
3	Hot Cakes - Molten Chocolate Cakery	Seattle	5427 Ballard Ave NW, Seattle, WA 98107, United States	47.6679510000000022	-122.385726399999996	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAD1OFFsMLX65j0rZ0bQvGJqgzbuSJWMZXVl9D5yK93hDtLI5IJyle0HQ1Hvhe6QA-bO7YMETZVAuMFNg5MNxzpk8kDmgTJKqyS8wyx6ARk8tHTmOePeURgacfLlgIjS0lak-XnvIoOrr43XFakCUIPF_AyqGm65UMqnXvL595GH0EhBPebbum_mZI5zWgQ2Cdfa5GhSAj7-NyvWvjUedyOv8bnpeiww9GQ&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJw6tae8YVkFQRxW883XdVQJ4	2	4.40000000000000036	\N	They had an amazing 2 for 1 cookie deal at the end of the night and after we closed the place they gave us like 4 more cookies for free... What kind of demon would I have to br to NOT rate this place 5 stars after that kind of love? One without a soul, that's what kind. Oh, it was ridiculicious, too.|Absolutely love both Hot Cakes locations! Fresh Minimal ingredient Chocolate Molten Cakes with Vegan options! Love their Boozy milkshakes! Everytime we have visitors we take them to Hot Cakes. The Capitol Hill location has more seating than Ballard but quality is the same. |I am definitely a chocolate lover. The molten chocolate cake is just ok. Dont know why it is so famous. But in general, the store is very good for a friends hang out for young people.|It was crowded, with the line to order food pouring out on to the street, so you know it's good. We ordered almost everything off the menu to sample and it was all delicious. My favorites were the chocolate pannini and the chocolate pudding but the menu changes regularly so I'm sure each visit would be a new experience. A new favorite dessert spot! |Pretty good place for a stop, but maybe a little expensive for what you get. The drinks are good, but not as good as the prices would make you hope for.|	2016-11-14 04:39:11.916067
4	Mr. Holmes Bakehouse	San Francisco	1042 Larkin St, San Francisco, CA 94109, United States	37.7876364999999979	-122.418280300000006	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAALKdzsZZRxZKMABWW8M5vqJ370gpobkT5lGzTBpaeTyr_cynudP0n5TMaPYxn8fasSd2sGpkYwv6NmMeteCe32UJJsi7NuD4mdO7w4Q5fzx2ZX63onqjbgheoYt-lOVIsRIo-Ul7oXx55lIBZIgw4EnI7U5Hw0PAub6KHZkfBj53EhBkRETSGKZ8yUcT49thy6TaGhQ7v0xIe8nA-c1y6KeZbnJ30at9wg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJT0h_9pOAhYAR-3iNZNso3xk	1	4.20000000000000018	\N	Cool options with awesome tastes! A lot of reviewers said if you don't go when it opens you won't get the best one, but we were there at around 10:30 and still enjoyed it!\n\nThey don't have too many seats. It's pretty much of a pick-up store where u order and go.\n\nThey don't have too many drinks options either, so if u want some drinks you will probably need to go somewhere else.\n\nBut the taste worths your visit!|It's a tiny little place that houses a lot of deliciousness. \n\nThere is usually a crowd in here as if they're not using the very limited standing room to tuck into treats then they are taking photos with the infamous 'I got baked in SF' sign. \n\nThe baked goods themselves are wonderful, we bought a few things including the ube puff, coffee cream bomb among others and everything was amazing. They're really good at what they do and their popularity is well earned. \n\nIf you have time, it is well worth the trip!|Cool bakery, but you probably don't wanna stay here too long since it's incredibly cozy. Best for a quick trip and to enjoy elsewhere. I particularly enjoyed the kouign amann. They have a rotating menu all of which are great! Definitely worth checking out! |Preferred the kouign-amann more than the cruffin which was too sweet for me|My favorite spot when I visit the fam-bam!  The absolute best custard filled doughnuts in the world- NO UNIVERSE lol\nThey are amazing regardless what you order  My brother loves the carmel rolls.  He demolished off two before I was done savoring mine!|	2016-11-15 01:44:40.897399
6	Smitten Ice Cream	Hayes Valley	432 Octavia St #1a, San Francisco, CA 94102, United States	37.7763629000000023	-122.424191800000003	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAGIb2sIDpvwMbTV6CBXcdiXuVsgI8Big22WqfbFXLlaXQc_fqYOevwh7Q-sqbYBf83RG8N6bJmea6Yl3zIduOGgg9INgU3rhU08DfCJgrlzOB4BwXvAVF-N2J1uOKnBi87gUMegaRSmVSgKyX_t8vsGPNTzKhcKnDTA2XGrtDdu0EhCRtv9SBTidO-gYiuGwwRGlGhQk1PIlT-kuAsn5cPCZkIhslFJ2ow&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJ70taCKKAhYAR5IMmYwQT4Ts	1	4.5	\N	The creme fraiche and pear caramel was delicious! Made with liquid nitrogen, it seems to be very hyped. Doesn't disappoint! One thing that was odd.. We can can't mix flavors even in a regular scoop. Otherwise we could have tried two flavors. |Think you have had good ice-cream?\nThink again.\n\nThis place gives Berthillion on isle st Lois in Paris a run for their money. Never thought it possible.\n\nCookie dough is amazing. \n\nIt is all smooth and creamy because it's made a la minute with liquid nitrogen.\n|The TCHO was amazing with the spiced caramel! Definitely something new and worth trying! Ice cream was great! Very rich and creamy with a nice smooth texture! Another good flavor is the salted caramel!|Earl Grey is good! But I recommend you get small size if you are alone. After having 3 balls of them, I don't feel that good anymore.|Icecream was okay. It's nice, definitely. But in my honest opinion not worth the hype amd queues (if any long ones). They make the icecream fresh, so you can see them while they're pumping liquid nitrogen into the milk while mixing everything together. |	2016-11-15 20:22:19.830032
7	Lemonade	Los Angeles	1661 Abbot Kinney Blvd, Venice, CA 90291, United States	33.9893387999999987	-118.462593100000007	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAADMGKxt347aVMy8BnyyZy8lrHCmY34Akw2zWpjpAwzVcyf7Gb6gC0-Bpt4-O04_XwU0Lh9-9xvQPbfnd4C24oXm4ZrKey7U9jILM8ZOTfh5c-wqka19S0MOKcElhsd6-UAyW6wPvdtymJYxHZtPxoWBB4KhBkoFR055KwNR8YNigEhCIA_vA-nb7ts9NvhG2gs-VGhRuBjBgNT9onW_nNanPMWq-4wZl4Q&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJmzV7iJW6woARuBK1wxcBNJE	2	4.29999999999999982	\N	at first i thought lemonade seemed a bit too complicated with their portion method of choosing how much to eat, but the items on offer are so delicious that i soon got over it. really tasty, fresh, and healthy options. i have found the best way to experience lemonade is to go with friends and share a bunch of various plates. and, of course, the lemonade itself is quite good as well!|very fast and friendly service. Amazing food and lemonade! Parking is a bit hard to find though.|Very good food. Price is reasonable. Health food should always taste this good!|Ofcourse this place has many choices in lemonade. However they also have alot of healthy food choices. Usually crowded, but alot better then all the other fast food restaurants.|I love the cafeteria concept and the free samples. Staff is friendly and price is okay for the food you're getting. Stopped in for a lemonade, Mac and cheese and a macaroon. Lemonade was please, I think I mixed two and have the blueberry guava one. In the end it was too sweet and started drying out my throat/ still overall I liked it and would give a 2.5-3 out of 5. The Mac and cheese was tasteless and the consistency was too mushy for my liking. The macaron was okay. The filling was not solid enough so it didn't hold the cookies and I think the cookies were slightly too thick. But I do enjoy the size of the macaron. Overall, sweet little spot to spot and get a drink and a little bit. Nothing mind blowing|	2016-11-15 20:22:49.702521
8	Skillet - Capitol Hill	Seattle	1400 E Union St, Seattle, WA 98122, United States	47.613124599999999	-122.313858300000007	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAIFnvnVHIOccL74XJ4-Bi2Z58GbSjn5UVu0Khq74sj8U1a9ToxEr6C3Xq_4-yzjQJ8cXorI3Yww_LP4YgDCI5dt6L-5pZ9Pb5vwxOq6OETDT1r8rRbNslFg7PnECicRyf8-8T-NQZq4SXFPEaf6-TI7yiq1rLBMnNHbHOpIJsM2PEhB9-Hd0bTgoUFRS6LxVMpDNGhTuO2US3ey4uJM8H0Gvc7N0veMEGA&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJpzOka85qkFQR2U4oqZ7q_Rg	2	4.29999999999999982	\N	Incredible breakfast joint. They definitely get comfort food right.\n\nThis was recommended to me several times and I'm super glad we opted to give the brunch a shot.\n\nFood was phenomenal and feeling. Coffee was great (as expected). Ended up sitting at the bar since the wait was long, but it was a lot of fun and our server was friendly despite the business. I was super impressed by their ability to handle such high traffic. \n\nHighly recommended for brunch |I liked this place.  It could've used a deeper menu, but I think it's somewhat seasonal.  The portions were decent and they put together some interesting stuff. I'd recommend this place for the aspiring foodie.  It's fun food that tries some different combinations if you want to try something only a little outside the box before becoming more adventurous. \n\nI believe this place started as a food truck and I can totally see that in their menu and attitude.  And that's a compliment, not a knock.  It feels fun and authentic to their perspective.  \n\nEverything was fresh, fairly fast, and well prepared.  Their cocktails were also good.|My first time here I was hung over and the greasy/gourmet/diner food hit the spot.  I was so excited to see such good diner food I never really paid attention to the price.  First time around I ordered the PB & J with bananas AND the grilled cheese sandwich with a side of poutine.  I know i'm fat. don't judge.  Paid the bill and didn't think anything of it.  \n\nThe second time I came, I had the pork belly.  And the third time I brought my gf and I had the mac n cheese and she had a salad and a milk shake. \n\nIt wasn't til the 3rd time I came here did I notice the prices.  I realized then I paid $10 for a PB & J, $9 for a grilled cheese... sheesh... pricey...  I don't remember the pork belly price because I was shocked that a salad, milk shake, and mac n cheese costed my $52.  \n\nIs the food good?  Yes, it was all very delicious... is it worth the price tag? hardly so.  For that kind of money I would rather have a fancy dinner... not have just fancy diner.|It's a very good American style cafe. The coffee, food and drinks are just fine. The Chicken Sammy is about the best fried chicken sandwich I've ever had. Some of the portions of the dishes are way too big so go with friends and share or stick with the sandwiches and salad. I don't like spending so much on three times as much food as I can eat in one sitting.|Love this place! They certainly know their meats. Their apple butter pork chop is amazing and mention the chub is the best.\n\nDefinitely suggest you check this place out.|	2016-11-16 20:15:03.849415
9	Tsukushinbo	Seattle	515 S Main St, Seattle, WA 98104, United States	47.5998558999999872	-122.326784700000005	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAKCfeIOZij5O1O_nigA2VKapEXNCBhNLL8yFykHGShlcOIPFwQaTYGgMygX1Qqi3fOfiLgRYTnuRSSzOs-R4ZS97oVbPL-SZFGv9R8zACLJi3_ZdsKwLQy0gao339B5hb0ovFAOARTvaR7gWiiHVQXNvRzkqR3RfkZnJR2Qxx-dTEhALx-2PL7QWoSG_R52_RwQgGhTErcxVfDZ2QzLJo3dgFs4MUXRhMA&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJnc-QmrtqkFQRlFnDTZSfac8	2	4.59999999999999964	\N	I've been there 3-4 times now and has never disappointed. Sashimi was fresh and tempura was perfectly cooked. You make a reservation or have to wait more than 20 min. |Awesome spot! The pho was decent not a huge pho fan.The pork ram en was amazing!  Loved the crispy onion and tender pork they put in.The unending was also very good.Service was extremely friendly and generous.I'm a fan.Truly excited that I have a new place to go to with my family.|Love this little sushi restaurant, reasonable priced and food quality is great. Love their Omakase Sashimi set, (chef prepared sashimi) well displayed with 12 different kind of fish, some of them you can't get at other restaurants, it was so delicious, totally worth the price I am paying ($45) too had this place is so small it fills up quick, have to wait in line for 30 minutes before we can get our table, but it was worth the wait.|I had lunch with my wife and mother-in-law a few months ago. The service was very slow, and they were very inattentive. I am not sure why. The food was good but the inattentiveness was disappointing. |Delightful!  I have a list of sushi places I frequent and Tsukushinbo is one of the top places.  Cozy hole in the wall setting, prompt service, fresh sushi.  I'll keep going back.  Be sure to make reservations, even on a Monday night it can be a full house.|	2016-11-16 23:28:38.428736
10	Cassava	San Francisco	3519 Balboa St, San Francisco, CA 94121, United States	37.7756346999999977	-122.496629499999997	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAACaEACJDtK41x6vrufe2YGdXWfudoSUtWmOWpQUuCWwE2YgOD0gdY5fkGeE-8s4XlyhbLD8dRFeFS6BSOPSKyt0gZ9dceY61XLErJcDtYVYUbJJkoP3WITctqUlIee75WCfAl7CUdysM6H7-oPAJ6qvsPch0ny24qD7ajaY7NZowEhCIgb0TpZyUp1lL4AvkTDeiGhS6n52c-vEgGIdTMa4Zafc2rPji8w&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJmRarFKaHhYAR7Rzri1MQfK0	2	4.40000000000000036	\N	Cassava is a terrific neighborhood spot offering delicious food with local ingredients and a friendly atmosphere. Their food is always on point and really flavorful. They also collaborate with the Balboa Theater to offer a 3 course menu for those watching a movie on Thursdays.|Great Japanese style breakfast.\nGood prices for quality and portions.\nOdd hours makes it difficult to not plan to eat here, but hey, it's worth the plan.|*** In Short ***\n\nBrunch. Cute. Tasty. Takes reservations. Need I really say more? Okay, fine: if they have it, be sure to try the Merguez lamb sausage.\n\n*** In Depth ***\n\nMy friend, who absolutely loves Cassava, has been telling me she wants to take me here since, oh, my birthday last year? So, after more than a year, I decided to just go myself, with a different friend. Oops.\n\nAnyway, I ordered their:\n\n* Merguez Lamb Sausage - This was just divine. Flavorful? Yup. Rich? Oh, definitely. Greasy? Very much so. Delicious? Hells yeah. \n\n* Braised Short Rib "Hash" - Not so much a hash as it was a quinoa and potato bowl topped with a poached egg and fall off the bone tender rib deliciousness.\n\nCute little brunch spot, with a simple, but fantastic color scheme, and a combination of indoor and outdoor seating. Oh, and my favorite part? They take reservations. For brunch. WIN!\n\n***Accessibility Info***\n\nVenue - We were seated on the border of their in/outdoor seating, so I didn't pay too much attention to the interior seating arrangement. If memory serves me, I remember the place being a little on the smaller side, with the border seating actually being the best option. That said, my end of the table was on a slight decline backwards, which made for slightly awkward seating. \n\nBathroom - Didn't try.|Great food with diverse culinary backgrounds. I enjoy the food both as a fine taste and as an art, even. I've had a couple meals before; most recently, I had the Mr & Mrs Croque sandwich, bread and contents toasted together in a coherent yet fluid sensation. Highly recommend if nearby. |I had just landed in San Francisco an hour before me and my friend (from Vancouver) ate here -- we were extremely hungry. We were staying in the Richmond District so we quickly yelped breakfast spots around the neighbourhood where we could walk to; Cassava was recommended. \n\nWhen we got there, I spent at least 10 minutes deciding against their brunch menu or the Randwich. I asked the server which one she liked better and she told me that the Randwich was a messy favourite. She did not lie. \n\nWith my last name also being "Rand", I truly feel like my life changed after eating this sandwich. I took an uber home from the bar later that evening and was told that I spent 15 minutes drunk-explaining my love for this sandwich. It's THAT good. \n\n10/10 Recommend.|	2016-11-17 01:41:39.637431
11	State Bird Provisions	San Francisco	1529 Fillmore St, San Francisco, CA 94115, United States	37.7837089000000006	-122.432993699999997	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAACNX4RjNl-UBp5YZUU-Zn7EeXchZvCRKAk1SbwCJk8DIvgtfIvGOu6Y5THqGSxxc-rAHGHae_s5MAyRvrZfeJFhRqz8CdfQlWNO6h1CNxlR3mX5vac1KVUBlNTEDoqusIMh4nvwqabar3OzJ1JhqVyWGKYyUTCme92IyqvnLADRvEhDfbjXBG8M2VvPHStggn8v5GhQ5fhFctrlohS47kj_-LPZ4s1meWQ&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJQ7kGpLmAhYARKeCe2pDobWk	4	4.59999999999999964	\N	If you're a local, or from out of town, this is the best place in SF to go to right now. \n\nMake the reservation 60 days out, or expect to wait in line for several hours. I'm sorry, this is San Francisco. It's well worth it.\n\nAll the dishes are spectacular and flavorful - I recommend the State Bird and the mushroom toasts especially. The Vietnamese dumplings are great too. Be warned though- the price per dish is deceptive and expect to pay upwards of $100 per person for a kick-ass dinner.|This restaurant is among the best dim sum experience in the city! I would highly recommend sitting at the countertop, where you get the most out of the experience. You get to see all the dishes being cooked (restaurant is dim sum style), and chat with the chefs. The owner is even behind the counter cooking and is happy to chat about the restaurant, the food, or whatever. Food is delicious, won’t disappoint you. My favorites ones are quail and the oysters with spicy sauce. So hard to get in, though! I would come here more often if it wasn’t|Wow, what a disappointment!  Hate to say that as it took 3 years to secure a reservation.  Like the concept, loved the ambiance.  But.....the food was okay at best and downright bad in parts.  Still can't believe it.  Potato chips ? really? c'mon.  I don't care what fancy dipping sauce you pair them with, DON"T serve me that sh_t!  Biggest disappointment in SF eating for the past 28 years.|Casual and energetic ambience where they serve creative, seasonal and eclectic food, whose flavors are reminiscent of French, Asian and California cuisine. I don't say this lightly, it is something worth waiting in line for.|Awesome place to eat in the city... Just outside of Japan town. The restaurant offers fusion type dishes served tapas/dim sum style. They feature a slightly consistent menu but the real food come a la carte... Great for a date night|	2016-11-20 00:00:14.26848
12	La Serre Bistro & Boulangerie	United Arab Emirates	Vida Hotel,Mohammed Bin Rashid Boulevard, Downtown - Dubai - United Arab Emirates	25.190176000000001	55.2745389999999972	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAABRq9C2ltpo0jAFyN7A5XBabHzJY-AGYynpquSm-2GAzRn8HlJTKgMCvxgtVWzIk52XCkjuS_ZWGm00VktY5lk4vfdJaWZhhjSjbuRG2ltLyz0l7cEbV-pi2d8ky8_7wxjhh5vGabMqiBIj2HJwn68kD81Udn4ciAWXSOq0RoA3gEhCQWsn_J1TKwz2m9w_yLcqEGhSOCwHHWrZWJCy10o4ruBa54LmSvg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJNd_GFSxoXz4RgBYJNedNxTY	\N	4.09999999999999964	\N	Great place for breakfast or for a coffee catch up with friends. Went on a Friday morning and it was fairly busy and almost couldn't get a table. Despite it being busy, our server was attentive and took the time to make recommendations. Will definitely be back again.|Expensive with small portion of food. but with nice decorated environment. Good for couples|Please Note: La Serre is split into the fine dinning restaurant on the top floor and bakery on the lower floor, this is a review of the lower floor bakery.\n\nThis is actually one of my favorite restaurants in Dubai.  In the morning they service what I consider to be the best breakfast in Downtown, this can be further seen by the fact that by 10 am the on the weekend the place is packed and you will be required to wait for a table.  Their coffee and tea selection is very good as are the breakfast dishes they serve.  During the winter they offer outdoor seating on the Boulevard in addition to indoor seating where one can watch their kitchen team creating the dishes.  They have plenty of attentive waiting staff and the service is accurate and very swift, even when they are busy.  My principle complaint regard this establishment is the cost of dishes and the portion size.  All their dishes, including the coffee, are above average in terms of cost yet they does not translate into portion size.  Although, I do love the food, I rarely leave feeling full always feeling they could be more generous especially when one considers the cost they are charging.  What I will say though, is that this is one of the most consistent restaurants in Dubai.  Dishes always look and taste the same, a feat that many restaurants in Dubai cannot even come close too.|One of the best pastas i have had so far.. located in down town with a great view.. looking froward to my next visit..|I have been coming to this restaurant almost every month to hold client meetings. The boulangerie is mostly busy in the morning but they have a special spot in the corner where it is very quiet. \n\nFood wise, there's nothing about La Serre that I don't like. As you will notice most of their customers are locals and they do really appreciate good food - La Serre is serving the best having been named BEST RESTAURANT IN DUBAI from What'sOn awards.\n\nWhat you must try on your first visit : salmon eggs benedict, freshly baked croissant, cappuccino, tart flambeé, and well... everything!|	2016-11-20 00:10:42.643505
13	Tarsan I Jane	Seattle	4012 Leary Way NW, Seattle, WA 98107, United States	47.6564633999999998	-122.361839200000006	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAEkKXcBVhzCjMsnAQFqstak5Omh_Ubtav24AJz6oTh1YsHjLQ7HXEORUXtH6P38SrauXSjRftJg5LcYExn9bUt1439HbKOviRfr69v2CwTH18tJCad7Mj495yy5pnWXNmlFUTK2qhwkVSUFTNn0n1tbGXAuSXN5kvlPn8gi3Lt_8EhCxw6-s8P9bQISlaT70y--_GhSGDF3A0yWLvtp754k7kYGlVyx9cA&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJwz3XAa8VkFQRsgaf-9zfWIg	2	4.29999999999999982	\N	The 7 course tasting menu is the move. Each dish has strong flavour / texture profiles. Absolutely delicious. The real star at Tarsan I Jane is the front of house though. It's all in the details and they are all over the little things. Highly recommended.|Went for Sunday Paella. We were served a vegetarian Paella, which was was average tasting at best - the rice was good, but the fava beans and other ingredients didn't mesh well. The other courses were good, and the dessert was good too; but I expected the Paella to be the winning dish. Furthermore, the service was not great. It took us a really long time to get water; we had to ask twice and still waited after that. |We went there for paella. Service was great. Food is of good quality. It's VERY different from food that I am used to. Every dish was strong. The experience eating here is like listening to rock music... I would have given 3 stars.  The last dish, which has an ingredient of "trust me" worths the fourth star.|The food and entire experience was incredible. The paella is cooked over an open flame, appetizers are incredible.|Amazing Spanish restaurant, often with a celebrity chef dining in the corner. Come to this place for an experience--it's not just for sustenance, although the pre fix will certainly fill you up.|	2016-11-20 01:30:01.312891
15	MBar	Seattle	400 Fairview Ave N, Seattle, WA 98109, United States	47.6225469999999973	-122.333918699999998	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAEQeZWo_8Awl3VH1pUb4KFWXVVicdrFEZjEmYosZ6VWsaYTdKrrCsOJMrCYnykHKZ4jgC6hVs2RsgdusjZAnhn8Q3TPWh2C0lTV7lI0spqmVwieOdT6I-VR2OF24ag2HxkroL8gTx-DIi5xtpal_pGk3r_YSrRPKGzBKpa0M-ZVZEhDfpyeoIM8APsK9IQOlbZ5AGhSFOE82-evoh1HXRk9PRJ20ayGFYg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJc_jpMDcVkFQR0lmokXEdXDI	3	4.5	\N	\N	2016-11-20 01:44:51.585674
26	Li'l Woody's	Seattle	1211 Pine St, Seattle, WA 98101, United States	47.6149610000000081	-122.328182999999996	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAPUTWhahkUkFs99jRJ9uuFdaVgS37OrwDWaIiAFtTbOQyvtXxB4Thj6P4osO5F2oIWoPOrMymZIp7qoLkiJ71OLJo-ksUSp0yLDN7mRazCmq_ysroTq8TGg8cIwMe3KvFjQU5mwbfUYFkjZBLjGSqf27zKjOAhUz9XeLXXqH4VOzEhA-UAEEOoofdsXtaWCI8JNmGhSuAgR1923g3AqAi70P2Zc9MtG2ig&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJlc-91cpqkFQR7py8rj_H1eQ	1	4.40000000000000036	\N	I don't always have the budget for a burger meal that's more than eleven bucks, but when I do, Li'l Woody's has not disappointed yet! The Big Woody (1/3 lb. Burger with cheddar cheese, bacon lettuce, tomato, onions, pickles ketchup and mayo) is my favorite. They play decent music, and the atmosphere is chill. Check them out when you can.|Honestly not sure how this place has so many positive reviews. The food was OK, but very underwhelming for the price you pay. \n\nBurgers had good toppings, but they had more salt then I've ever had on a burger. They meat was way over cooked. There is a lot of potential, but they failed to deliver in terms of actual cooking of the meet. \n\nThe sides were huge. We got a side of fries and it was an entire basket. The onion rings were probably an entire onion. The problem though is that they tasted like they were soaked in grease instead of being properly cooked. The onion rings were not very crisp, so probably not too fresh. \n\nThe place has an interesting decor and nice vibe. The bathroom is pretty disgusting, but fortunately you can see the kitchen and it looked clean. \n\nVery underwhelming and not deserving of the current 4.4 star rating on Google. |Good burgers and fries, the special (Beecher's mac&cheese burger) was delicious. There is a decent dining area and they are open till the early morning; however, the dining area is closed during the late night hours and you are also not allowed to consume food inside during those hours. |This is THE burger place to go to in Seattle! Li'l Woody's doesn't have fantastic burgers, they have the BEST burgers. \n\nGreat food, fast service, and a cool loft area! \n\nOnly downside is parking. I usually have to park 5-10 blocks away. Still, it's worth it.|The burgers are just okay. Not overly impressed per the cost. I would look elsewhere.|	2016-11-20 02:04:19.596473
28	Brenda's French Soul Food	San Francisco	652 Polk St, San Francisco, CA 94102, United States	37.7829023000000035	-122.419035800000003	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAANeH8AJStkJyBaErXb6NEX9veG8Ugu0pX52S5rWxais7MVzI2NHerFtBxztY12aNm_9uloF09rqBwpopw7lmGYst10900kRsXcczFylizbHoZ_C2r5h1LBu-j8ZcZADaagUJhJ1mo5wkEPICEgAv9-612WcpbHSg44l1nHW3gqz6EhDAQ0xr6KjRw32_B3_v9wYRGhTp7GHgyMs3vBLYGWZ0DMvDXe2iUg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJZ9s5SJeAhYARIX3Fxl6oj6c	2	4.40000000000000036	\N	~20 minute wait on a Sunday morning, which was really impressive considering there were at least 25 parties in front of us when we arrived. Very impressive service and speed. Food was delicious. Menu offers many unique & uncommon selections.|Must-try brunch spot! Love their beignet flight, french toast, savory dishes that come with the divine biscuit. Love their homemade jam too. Good sized proportions which make for delicious leftovers. Relaxed interior with live music at times. The neighborhood isn't the best...being at the edge of the Tenderloin. And the line is a daunting 1+ hour wait during the busy times on the weekends. Luckily, they have brunch all day Sundays!|Delicious food, seriously amazing. Great customer service. You really need to book a table though! The fried chicken was amazing. You could probably share portions because they are HUGE! Would go back to again and again.|To start friendly staff with a warm atmosphere. I had the andouille omelette which was awesome. I'm not usually a biscuit person, but tried it anyways as the waitress told me it was the norm for that meal. Very glad I listened , because it did compliment the meal along with the freshly made peach and also strawberry preserve one on each side. I suggest you do the same and try them both. I will be back!|While in line, I was ready to post that the food was good but not worth the 45 minute wait. Couldn't have been more wrong! This is my new favorite brunch spot in the city. Hands down.|	2016-11-21 04:44:24.0606
16	Paseo Caribbean Restaurant	Seattle	4225 Fremont Ave N, Seattle, WA 98103, United States	47.6584939999999975	-122.350312000000002	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBcwAAAHu2vZBYxEA-Swv0sq3_iDnMiBxv-mpQ8EFVTE3DmEQcIbme5VyZ6OFyVOonVoahBPNjX_gORLGSyB_SyGomCBsfjAKKeQCPEK0yLmDSZG4_M0EL5_puTT-XjT7Q8348O-dQwCVpzEPinuzAvbmNUfllZY_5ZBOLaIn-cXKrVV7tEhAeD8qyw-22NR-K0rOX0A0IGhQh_TWq_9J0ZRYPX0UgdydFSyFPUg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJI9abTFMUkFQRjkoqvmG4eWY	1	4.59999999999999964	\N	Amazing happy hour menu! There bar set up is amazing-beautiful! Scallops delicious. Fried Chicken with corn gravy is a must. I have no complaints beside our super slow server. I would go here again.|First time at Paseo. Sandwiches are as good as what I've heard. Totally lived up to their name. And best of all there was no line for a Sunday lunch. They did not have any tables available though. So got it to go. Definitely will go again. Just wish they had more space.|These sandwiches were pretty tasty! The corn was also good - but don't get it to go! We unwrapped it and all the toppings had come off onto the foil. :( The pork on the sandwiches was kinda dry, but all the flavors and toppings were delicious. Super filling and satisfying dinner.|Juicy, messy, meaty goodness. Something overshadowed here is that parking tends to be really good for where it is located. Wait time is not too long, but depends on how long the line is. Just make sure you eat carefully, not wearing white, have a lot of napkins, and are in a controlled environment so the mess isn't a problem.|Cannot go wrong... unless you show up late!  Get there early.  There is often a line, and they sell out fast.  Food is amazing!|	2016-11-20 01:48:29.041957
17	Tacos Chukis	Seattle	219 Broadway E, Seattle, WA 98102, United States	47.6205587999999977	-122.321272500000006	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAOflGfZ-mXrzYyhycpq6173pDN5MjCWkctv1NtIO21ht4JdDq8ey-xCzydoDVe2hrev7sroKOwDPup2h0pls5SkxlamfQ2LsN98b1-dDWrQjIhjWVZFaYZNUmsRwA7sYIC1ONw9uzuF5ct-bN27CcPxEt7i-k0kFck70xPyKxfUCEhCi7i4X1cc66jHuo1DMSjP8GhTwALqnGJwHJ6yx_2rjUWPhE2iVGw&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJL2gQeTIVkFQREoqp0MpRH1U	2	4.70000000000000018	\N	Taco Chukis is a small taco shop on Capitol Hill with a small and simple menu and simple yet amazing tacos. There's seriously like 3 or 4 ingredients - all amazing and high quality. Very very cheap as well.\n\nSeating can be tough, but even getting take out is worth it. I come here at least once a week and the tacos and other items are are very consistent.|Tacos Chukis' business has grown considerably over the last couple years, and with good reason: they make great tacos. The good news is, even if it's a little harder to get a seat, the tacos (and horchata) are still worth the wait.\n\nIf you're lucky, you can even see the top of the Space Needle -- just the tip -- from your seat. One of the better hidden views in town. ;)\n\nDon't be afraid to duck into the busy mall-like building that fronts for Chukis; they're upstairs, in back, beyond the tattoo and piercing parlor. The only downside is they may not be wheelchair accessible -- anyone know if there's an elevator?|So tasty and not expensive! This tiny little place in the upstairs of the building is definitely worth the wait if they're busy. The house tacos are my favorite tacos ever and you can even get a beer to go with your tacos. The rest of the menu looks great as well although I can't seem to stop ordering the same thing every time I come since it's so good.|Great and inexpensive tacos. Can't believe I just found out about. The flavors are so good. |Delicious tacos, great prices. I have and will continue to come here every time I'm in Seattle. \n\nParking is easy on the streets, although not too cheap--about $3 per hour. \n\nTacos are less than $2 each. \n\nNice casual environment with well prepared tacos. \n\nI think about 4 tacos equals a meal for me, personally. |	2016-11-20 01:49:00.344397
18	Ma'ono	Seattle	4437 California Ave SW, Seattle, WA 98116, United States	47.5636166999999972	-122.387122399999996	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAGU1LOndRLLF1i_45ARQOmHltQ5kW-eLjZliQ8KNO4aqBS4UbtM3c5e1jf0bxh9MbaNE1qrng8SJfMRIs9MF92BXQ2v0apifOSup1zmEYgyZZHspWYDxG-ZZ90XhGJiFl5YqfyNfMRDpsqOvgZmKnjvEworUJZRwVX82Ms9KGeJREhCUfYfMCKSkK4igYimOajqPGhTvTlAZZSzMwnKUe6DmtKijTe5mNg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJR9EYf_dAkFQRLLICaK8K6_w	3	4.29999999999999982	\N	The fried chicken is everything you've heard it is, but don't discount the rest of the menu here. Amazing Hawaiian inspired dishes. It's hard to order a burger at a place like this, but here it's the famous burger from when they were Spring Hill. THE. BEST.|'Too Cool for skool' local eatery,  reputed for its fried chicken which is good but nothing to get REALLY excited about. \n\nInteresting Asian/Hawaiian inspired menu.\nWe have been several time and have enjoyed our meals here each time, but each time I find the place expensive and a little lacking in atmosphere.|Best fried chicken I've ever had. They tell me it's a 48 hr process, and it comes out tender, rich in flavor, and crisp all over. I absolutely love it. The price tag is kinda high, but I definitely appreciate it's value. |Fantastic service, really great food, quick turnaround on reservation.\n\nWill be back, soon!  thank you for a great evening!|The fried chicken really good but come for the authentic Hawaiian food. The loco Moco was delicious|	2016-11-20 01:55:47.131645
19	Cafe Munir	Seattle	2408 NW 80th St, Seattle, WA 98117, United States	47.6869589000000005	-122.388014999999996	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAIXVoKr7En9M7EVV3pUF6yCwLG6e61BRb-Pfa8MH6frwjXF-u6LDAIu_PcfxcwHQLLlFDFLzBxkjHMY5v_NfFbRgTowTxgV5aXIo61HW34ALaud6WUzuTJKdZjLzfKqHo7wZOhavKZ2KecynIY6ptFZ84VA0wwZscu3k9ptwFP9EEhB9NFuwa0LaXnPyt5xsnEBdGhS_mN5xXCmD6sFTVacMheLlGMmgzA&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJ9-NYM34WkFQRunbcbbDHD5g	2	4.79999999999999982	\N	Been here at least 5 times already.Menu doesn't try to look sophisticated but it is sophisticated. The largest Arak selection I've seen in Seattle. Service was always good. Try the lamb hummus and stuffed pita with lamb.|Cozy atmosphere, tasty authentic food, great drinks and amazing customer service. Love it!|Amazing flavor and divine atmosphere. |Fantastic, great service, great drinks, everything on the menu is delicious|The best lebanese restaurant in the town and I try all of them.... The chef is amazing..... the service warm and professional.... the food is a culinary experience and the price is great..... Is a reference for tasty, authentic and  healthy meal.... You have to enjoy it!!!!!!!|	2016-11-20 01:56:45.992088
27	Sushirrito - SOMA	San Francisco	59 New Montgomery St, San Francisco, CA 94105, United States	37.7880930999999975	-122.401115599999997	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAIXE0ugNyG0ZrqECoqCVUbkJ44pzL8v-EfsuirzVxPISyA1uUMt37wHOhEKlQridX6KMMT7emH8JN2dF-oa4aiIVvFsNQtIMd5Zcto_Ov9UAy6Pphcq2MzVIupkUSissQzX7lRbOPO1GNN7NS-8FJEZDRRJtZUYbeWvyVfL5nSjDEhC9VNUbo4b5q92KW4C6E4pPGhQO16sPITCJAcA7htkDIvWIONatrw&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJ59q8pmKAhYAR0tfR_s2qwak	1	4.09999999999999964	\N	Love this place, but they only use one prep-station for both "dine in" and "online" orders. As a result you may find yourself waiting 20-25 minutes during lunch hour to order. There is no real "dining area" save a few folding tables attached to the wall but you would not want to eat there as lobby is typically packed like sardines. A more efficient method of pre-order and pickup and pre-prep should be implemented during rush hours to keep wait down. Won't keep me away unless I find a comparable product with a shorter wait.|I have been wanting to try this for years and to be honest I don't think it lived up to the hype I built up for it in my head. Don't get me wrong, it was definitely good. I still like regular sushi better, but if your in a hurry and in the mood for some sushi style food this place is pretty good.\n\nSide note: I thought the drop-down tables that double as wall art when not in use were pretty cool.|I was in town with my husband on a business trip. I heard about this place and had to check it out. The Yelp reviews made it seem like there would be a line, so I went early at 10:30 (it opens at 11AM).  I was first\nIn line and super excited to try their signature Geisha's Kiss. I ordered half the rice than normal so it wouldn't overpower the fish and other tastes. It was everything I expected and MORE.  I look forward to going again!!!|It's okay. The original Sushi Burrito joint servers up some complex combinations in a fast casual way. Perfect for lunchtime take away eats. \n|This is first-time I was trying sushurrito. I took Salmon Samba. I liked it! It seems very fresh and high quality ingredients. Big size. Good for takeaways.|	2016-11-21 03:48:57.86002
35	Fritz European Fry House	Vancouver	718 Davie St, Vancouver, BC V6Z 1B6, Canada	49.2772701000000026	-123.126756299999997	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAANbCfYKft8enlNcqsduIWVrsKsePo8c78l_odEq6aGO2HwGhyYMs1u_Qkxl2Fb-dSUBS36gYrqMCjcocW-vZ_Q-cuT9doScHvjMn5AcDc3bcN-OyX-WhQ9idmKBHaWc0z_2uBfbb2fojx316oEefgohaTI9Y_IlBhkD3yxtbtlchEhB3sQKwZjm7VkL_OY9T3oswGhS94SYrOwt-YGFN-X_9EwZsbdG6MA&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJB2dabNRzhlQR8uUmA5w0nTQ	1	4.29999999999999982	\N	Some solid, friendly, comfy poutine. Enjoyed the Garlic Lovers sauce with a small size (easy to share for two). A fun little place to enjoy a Canadian snack!|The best souvenirs when I was drunk :)\nBest late night food when you need something warm and heavy :)|I didn't even like poutine before this place. The fries are so fresh. Favourite guilty pleasure place in the area!|The fries taste good but aren't very healthy. There is no washroom here|The place was crammed full of people and still it was fast service and amazing fries. I'll wait in the rain for that again for sure! |	2016-11-22 07:53:39.284799
20	Sam Choy's Poke to the Max	Seattle	5300 Rainier Ave S, Seattle, WA 98118, United States	47.5539897000000025	-122.280322699999999	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAALF2NYadk7LajjEm87vh1zHP82ut8dHOu7o7H0EgDjCPxlH8MzLPqfIJgpvGbvG96YVzswjlZxy1BrV3xyvoZWQFa6q6Utp6m-8QzQeH7Wcc3JgAX41gI88Zl0Y-iy84ZhQnJL5i784-Gdr4eqLZVFuNzc7_wBPbgo7zuMMFdGaQEhChjJYvu_U_CSXt0kJtbrZ_GhQLBc8S_JbJN-HuTsSviXPIa8P8HA&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJMSG7ZA9qkFQRCn8iYSD0tJg	1	4.5	\N	Decent poke, pretty good fish and a reasonable price. You definitely fill up quickly on the poke. Avocado's probably not worth it - it wasn't a great avocado, kind of underripe. The staff was really friendly too. One thing I didn't like was that drivers parking in the lot end up shining their headlights right into the restaurant at patrons. Otherwise, decent venue.|My third time being there and trying to go through their menu selection one by one.  Food is very good though it takes a bit of time getting.  Very friendly and good looking waitstaff.  Fun atmosphere and they offer a parking lot so always a good thing.  I will return many times.|So happy that Poke to the Max has it's brick-and-mortar location in the neighborhood. Prices are reasonable, food is fresh and delicious, service is great! I'm a huge fan of their reconstructed musubi, which is really just a spam musubi re-imagined in roll form. Messy but oh-so-delicious! Check it out. :)|Very awesome food, the fish was delicious. It was quick, reasonably priced, and I liked the feel of the place (good music too).|Incredible poke! If you like fish, but have not yet had the pleasure of trying poke (pronounced "po-kay), do yourself a favor and try Sam Choy's. The spicy oysters are really spicy, and the salmon is out of this world, but everything on the menu is brilliant. Try it; your mouth will love you for the rest of your life!|	2016-11-20 01:57:12.451546
21	Bateau	Seattle	1040 E Union St, Seattle, WA 98122, United States	47.6132707000000011	-122.318478099999993	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAKz9JeIxS9J5n2X0PB3bhPjAfCG9_ATIZu0gxcviMqzzRl7JbpycvjB5DAkSd8fC9CbiEkvY9zyIOVSb2Y-HrW7opExKf602HF1G3mmhbgnXZIAjs-zCg4vDwLEE4i_x2ELkxQSPO9mR3m2YRqvRUY3eK9D0RU-se1pVHOegC58BEhBluJrBsL_xWqVT2s_FmlV9GhRLcAJvjf8691or6w6YTi6PDgtWOA&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJI5PDGcxqkFQRdwpp6UPUjyk	3	4.20000000000000018	\N	The steaks were delicious - but overpriced. And the menu definitely lacked vegetables! Please offer a few veggie sides & complimentary bread/butter. Dessert list could be improved with some classic offerings too.|Expensive but so worth it.  They serve incredibly unique cuts of beef here, with most being served family style.   Highly recommend trying this place out, but make sure your wallet can take it.|Bateau's website directly links to a Resy app for reservations, but they don't honor reservations from it. Despite directly linking to it, they say the app "isn't legit," whatever that means. Supposedly they only honor reservations from Open Table, but they can't be found there and don't link to it anyways. Guess where I won't be eating.|Amazing filet mignon! And don't skip the fries :) We had a bunch of different appetizers, sides, and sauces, and the whole table was definitely happy.|Very overpriced for what you get, which is supposed to extraordinary but was just okay. My steak was full of gristle and was not all that good. A small bowl of mashed potatoes that were undersalted and bland was $10. Nice concept, good service, but epic fail.|	2016-11-20 01:58:42.20541
22	The Butcher's Table	Seattle	810 Blanchard St, 2121 Westlake Ave, Seattle, WA 98121, United States	47.6175396000000006	-122.338528699999998	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAC_SX7rJQwg6AEpUPGpp8pu46BLAYZ6DWUOMKKnEeQUXYj86LRUZ9Pwta-UisdsmjHjwrPjOEcHy07AxL9mLvZ9Lsv_e-TaisEn6Ly-CHycK6xg0kl_ca-n4qu3I-2T1GZK23QHXvn4HvSYbaKOygegONe1UhqPHoaBdz7U8H6wvEhBJW0TNcOw0RL9ul-4U1uUgGhRgpXQT7LtC5Ev0j3eUbqlD9cINpw&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJpylJiEkVkFQRNfzgg6jksp8	3	4.29999999999999982	\N	From the makers of famous Beecher's Cheese is this gem 'The Butcher's Table', one of our new favorites. Had the skirt steak sandwich and one order made as a salad. The skirt steak was grilled to a perfect medium rare with a nice char that made it incredibly good. It appears that they use a wood-fire grill. The steak was of high quality. It was flavorful, tender and we couldn't get enough. Can't wait to try other things. (Note: We sat at the raw bar which appeared to have a few things you'd find at a sushi bar, but wouldn't call this a sushi bar.  However, the raw bar has some remarkable-looking food.)|If I could give them a higher rating I TOTALLY would!!!! \nservice was excellent, the place was beautiful atmosphere just perfect, I chose this place for my last night in Seattle. We are from California and we have been here for a full week. tried many restaurants in our time here. Very glad we came here last. Nice closing to a very nice getaway. Thank you Katherine for taking care of us. We will definitely be back again. 1st on our list now|A great place for sandwiches on the go during lunch time. Their take-out section is open from 11am to 3pm and they are the tastiest sandwiches in town.  The beet sandwich is my favorite and highly recommend. The high quality and friendly service is definitely worth the price.  It doesn't get any better than the Butcher's Table.|AMAZING food.\n\nTERRIBLE customer service.\n\nWas here for a business dinner, where the beers delivered were not what was ordered, we had to ask repeatedly for menus and then waited an extraordinarily long time for food. Which was actually quite good.\n\nthe service however was poor enough that i would not return unless no other option presented itself.|Fantastic skirt steak lunch sandwich! The beef fat fries were also amazing. Pricey but I think worth it|	2016-11-20 01:59:29.542453
23	Spinasse	Seattle	1531 14th Ave, Seattle, WA 98122, United States	47.615079999999999	-122.314477999999994	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAABYov3zxyZNoi1RqEMHBZWpoNoYITiQK9QRShVcyWqZ-wOe3tM_4fGL9A2EBBt5jUOmhCXpxYfQrb_EYLyLSlhwiLrRB_xM005KZeGal84q4TiasxUAZyx_yfgUYUVD7nP7ZsibfcxFOC2dBAFQHDqCR-pzRXD5VbzGCiex_f90XEhAKZv0BqL3MnCFE7sWQxp-lGhRrzWBb0CprHD3RyBcDvWxBeRR-9Q&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJy73n9s1qkFQRRslGmCZxvv8	3	4.5	\N	This place was awesome.Despite it being super busy we got in fairly quickly and while we were waiting we enjoyed watching them make pasta by hand. Most delicious pasta we've ever eaten, all cooked perfectly al dent. The truffle sausage special was a flavor we've never experienced, the gnocchi was perfectly sized and cooked, and their bologna sauce was the tastiest red sauce we've ever tried.It was also fun to listen to all the staff talk with their Italian accents and sometimes in Italian to each other as well. Five stars hands down.|Sounds is amazing. We've been twice now and each time, the dishes were inventive, seasonal and delicious. It's pricey, but worth it and great small menu so you can go with a group and try everything. The simple pasta with butter and sage is out of this world!|Incredible pasta! You can even watch as they make the pasta. Very delicious but fairly pricy.|Seattle has a lot of great restaurants but Spinasse was the highlight of our trip. It is a Northern Italian restaurant so the menu is hearty. My boyfriend is from Mlian and he said this place could easily be a successful restaurant in Italy. The pastas were unbelievable, so even though there are so many delish starters to try, save room for the main attraction. We loved the prosciutto starter, which could easily feed 5 people, and the stuffed zucchini blossoms. If you can get a reservation, Spinasse is a must!|A wonderful family-style dining experience. Everything on offer is utterly delectable - even just the spaghetti and butter will have your mouth orgasming. |	2016-11-20 02:01:53.423222
24	The Harvest Vine	Seattle	2701 E Madison St, Seattle, WA 98112, United States	47.6225807000000003	-122.297287100000005	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBcwAAAPT2cKoqUMALLaAUEgC1DBL6ccgReBwKhJDyEnsy7_DGMHuZSRqmfHy6bDsgb8sdIDD_RQstc-mEjOOFzg-7dLMte1h6LwRMk5xv5DngSklWGuD3HCbv5_G0Qu1pN7jg4-4ug-fRzXF9YuL-B18AUj7qv5KLn8zJAkEv6swswOq6EhA8i4CTHcgyKk0rqvrnz63lGhS-ZTrwy-t_W1cD4TQJ_9Tk_yv8Cw&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJeSiRdCtrkFQRJ3TrP453MpE	3	4.40000000000000036	\N	This is a great date night spot! Awesome food! Amazing staff! Great ambiance! This is the Queso Tri Pack and it was phenomenal. Servers suggestion and it was spot on!|Very high quality tapas. Love the space as much as the food, whether you are at the bar, on the patio or in the lower dining room, they all have a unique character. |The Harvest Vine has very good and authentic tapas, but very small portions have a huge price tag. The tortilla was the best Spanish tortilla that I have ever had. All of the dishes are extremely flavorful.|Great atmosphere and service. Very good food in a unique setting.|Very cute restaurant.  A bit pricey.|	2016-11-20 02:02:31.120492
25	Mamnoon	Seattle	1508 Melrose Ave, Seattle, WA 98122, United States	47.6143864000000008	-122.327599800000002	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAADE3rxNjryBn5Jm5XI-zHaUqtMgtNLUERWVs2M4JpVKol3FKJjQLE2khfy-cEh0NtHbVhRVaTVv8-TWCI6r-xPeDt_HWN0zsMeYpFLm4RBe1olqS3bMhUpeH2ctm2hc4IGPytmDEbP9Z4abZdlUwm4pIxppF68xXwgVS9bSzn-AxEhCzkCgxLkUcLG4m2Jz2zkHkGhQL2flkVf9ZcnZRO1vT6kFSzxAr4A&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJPUFs2cpqkFQRi34BjPyrnqU	3	4.29999999999999982	\N	It's a nice place along the Pike/Pine corridor with a friendly staff and a different, but good menu. Don't be shy asking your wait staff about the menu as the names of all the dishes are in transliterated Arabic (pretty sure it was Arabic, but may have been another Middle Eastern language). Regardless, the dishes were pretty good and it was a nice atmosphere. It wasn't too busy when we were there, but it was just two of us and I think we beat the crowd.|Very nice atmosphere with lots of yummy foods! A little over-priced based on the size, but totally satisfying experience!|Excellent Lebanese restaurant with interesting menu full of less common dishes. The decor, too, is very creative. Mamnoon has now opened a second location (this is the original location). |Mamnoon serves food that is not quite as good as back home... according to my friend. If that's true, I can't even imagine what the food back home is like. \n\nWhile my first experience with middle eastern cuisine, the restaurant servers dishes that are Syrian and Lebanese with a little local flair added. The result is tasty and restrains a exciting foreignness that is very fresh to me. \n\nThe service is also very friendly and full of tidbits of information about where the food comes. Quite the education. |Great happy hour food prices and quality. Solid cocktails, but not much discount for happy hour.|	2016-11-20 02:03:28.022444
29	The French Laundry	Napa County	6640 Washington St, Yountville, CA 94599, United States	38.4044230000000084	-122.364977600000003	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAALbJRuszyNAEgQhQrGpvHdSK-VZCxXlrtrufRFLm7-obogzeB7If_1f7iBPauqaMvpYykAoFSp_blCQ7XyV4v3EFx5p_a7alWpR-5YIH5xvOYC4w8ZDz6dgMAbmxMmhgESP8kT0fa1KxEBXaFcxbja30h53b-rduDLfTlYcLSQIPEhAmJgy7KdVQu7v2iDYaIY_gGhTX9D4cUrz3upnkJjgUkBui06TLlQ&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJAAAAAERVhIARYeTLvbbzAxs	4	4.40000000000000036	\N	The food was exquisite and both the setting and atmosphere were remarkable. The staff were fun. But our table service was a little rusty, which was important considering the cost.|13 great courses with amazing presentation. Probably some of the greatest place I have eaten. The food tastes very exquisite with a wide variety of flavor. Great location and the restaurant has a great setting. I would definitely recommend it for big occasions. |Believe the hype! Best overall dining experience of my life. The courses came in like fireworks, saturating my senses with curated and carefully designed compositions blending the best culinary art and science I've experienced. The service was beyond impeccable, going above and beyond what we could have wanted. \nMake no mistake, you'll pay a premium for the experience, but what an experience it was! Highly recommended for any special occasion|Service was excellent! Unfortunately that's all that my group really felt was worth the money. Each course looked fancy but they were all over salted. Out of the 5 main courses the group was only able to clean 2 out of the 5 dishes. \n\nNot worth the money but... it was an experience.|Eating at French Laundry was on my bucket list and was happy  to be able to do that. Food was extraordinary. The person who greeted us and seated us seemed indifferent and aloof which was upsetting. But our sever was very nice. 5 stars for food .|	2016-11-22 07:36:53.209127
30	Atelier Crenn	San Francisco	3127 Fillmore St, San Francisco, CA 94123, United States	37.7983340999999982	-122.435944599999999	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBcwAAAEIbbElhzctKcbjcODbmBQc9OhnXFSw79I7ChVLFmRPXTtTYoOC0_yR6SES2YM7rxk-ag1sczuDi5BNRh47umQJJBtE0q6_D5yR4WOCfHYQGCwWyHSSokC8oV7JKxihap8-KK2WE8vTfw1HiANdLjoUSH9vlBKxLDqbQcqSZBbwREhC_QY20sreM_eJtbcjtcUFfGhQfh05zsU-5veQk8fZJaibCj1cM_Q&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJx1ULhNCAhYARSRq9NDWTeqI	4	4.59999999999999964	\N	This is possibly the best restaurant we have ever eaten at.  And we have been to most of the Michelin starred restaurants throughout the bay.  The food was inventive and delicious.  The service impeccable.  The length of the meal was just at around 2 hours, which we appreciate for a meal with so many courses.  Go to lazy bear and you are committing to a 3 hour event (although well worth it).  French laundry, 4 hours (not so worth it).  \n\nThe only thing I wish would have changed, was knowledge that I would be eating a few courses with my hand.  If I would have known that, I would have made sure to wash my hands first thing upon arrival (took public transit to get there).|Atelier Crenn is the restaurant I've eaten at in SF. And will likely remain so. Aside from Dominique Crenn earning the much deserved Best Female Chef in the World title, her flagship restaurant exemplifies peak culinary mastery. With an intimidate and boutique dining room buzzing with service, AC offers a culinary experience that makes you believe you are somewhere else. The food service is an exquisite balance of art, seasonally optimal ingredients and flavor. The wine service is nothing short of incredible, offering bespoke pairings and variety to suit all pallets. I was recently asked if the experience was worth the investment. My answer was an undoubtedly "Yes." If you are considering a two or three star Michelin restaurant, Atelier Crenn should be at the the top of your list for SF, and the Bay Area. |This restaurant is by far my favorite in San Francisco. I went there with my family to celebrate graduating college and it was the perfect choice. If you want to impress a date (someone who appreciates food, of course), THIS is the place. It's not like any other restaurant I've ever been to. Open minds are necessary for this experience, to fully enjoy it and take it for what it is: A culinary journey that delights both your eyes and taste buds. \n\nThe food was so good that I had to eat slow in order to take in all the different flavor pairings.\n\nThis restaurant is pushing boundaries that too many restaurants are afraid to in this city. If you want tomato soup with croutons, mac and cheese or steak and fries- this is not your place! I'm so sick of all the new 'popular' hot spots in this city that do nothing but imitate each other by pairing fresh seasonal ingredients in a conventional way. Finally a place that can surprise and make a good impression!\n\nThe atmosphere is understated and quiet. It makes the food be the centerpiece. I can't wait to go back. Every foodie in the bay area NEEDS to try this spot, I promise you won't be disappointed :)\n\nPossible negatives: This is by no means comfort food, it's culinary art at it's finest. It's pricey. It's not a quick in and out dining experience. But, I swear it's all worth it! :)|Took my gf here after hearing tons of hype. I love to try new and unusual things. Some of the food was good, but the price just isn't worth what you get. The clientele is also the snobbiest I have ever encountered. Save your money. Plenty of better and cheaper restaurants in San Francisco.|You get the show and the place has excellent service as expected in a two star restaurant. However, it appears that the show was more important than the food and as a result the food looked better than it tasted. The price per value was surprisingly low. Two groups of friends described similar experience.|	2016-11-22 07:38:34.554994
31	Le Bernardin	Manhattan	155 W 51st St, New York, NY 10019, United States	40.7615691000000027	-73.9818047999999919	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBcwAAAOnn2uwTI5rTSWm0-h2EOGWXz_xAmA4tlbYOE5GzLzHLfATJr2Dtwg2qE5ipZ8MihULREWzLLyRz2PoRfdTKmba9tB29FvmN6FsG0UhXDYdUC9c9eCRkDPFUGu9dckHle7RcenLl17VMAVhdLaRg60yiiAmM7xfDcl9c9_Zuc6Q_EhBr0D_nV8qQ7a5FO6l0PK4eGhQVPhA6Ida-DkpslrMBJ4oHMY9H7Q&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJVSKXkPhYwokRVgXdrRfFxh0	4	4.59999999999999964	\N	This is a place that everyone should go to at least once in your life.   Japanese and Spanish ingredients with French techniques.   More staff than patrons moving in precision dance like patterns.  Excellent service making everyone feel like royalty.   Better eat before you go there otherwise you'll leave hungry.  Lol.  Not a chow down type restaurant.  Elegant and refined.   I suggest the Chef's Menu as opposed to the A La Carte selection.   Better save up for this experience, it's more then expensive,  but worth every penny. |The food was delicious and the service was amazing. The attention to detail is phenomenal! Congratulations to Le Bernardin on their 3 Michelin Star rating. It is well deserved.|My goal in life is to eat at Michelin restaurants wherever I travel. Of course I had to try this 3 star. Meal was great but I've had meals from 1 or 2 stars that were just as good at less a price. If you are into 3 stars then check it out, but I'm not sure I will revisit this as there are so many good places in NYC to visit.\n\nPs it is really hard to get a reservation. \n|Didn't flinch at gluten and dairy free. Impeccable service and exquisite food elevate meals into experiences. Masterful.|Fantastic seafood dishes and amazing service. The menu is creative but has familiar ingredients. Be sure to arrive hungry and leave plenty of time. |	2016-11-22 07:41:20.56547
32	Canlis	Seattle	2576 Aurora Ave N, Seattle, WA 98109, United States	47.6430890000000034	-122.346780800000005	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAALcRSN2mMFeZ7VEiEL5jPu_LIXuBWoH7l6sbisLcHnUdW7BvWl-ch9JHfDXNpIBbf6O_rIyickOoA2-t2kLsLN0WcWYt05J2UYIEMuNpnVOtszi1ebAEdJFqfsswwmEQw-FCqkC9QCw66sV_u7Pd17KeyuxGhw1CaSKzSqn3-yS-EhCOyttuph5EdNr-ZSjQR_GBGhRYvMbrQK2_N0ykgufmOqcx2ekTpg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJRXCfNwUVkFQRxraD8U-dANE	4	4.5	\N	Went here for my Dads 50th Birthday celebration and it was absolutely amazing. I've never been to such a nice, classy, delicious restaurant before. The service was excellent and they even brought out a piece of dessert for my dad. Highly recommend going here!|Such a great first experience at Canlis! A lot of expectation can be built up from all you here about Canlis, and they completely met, and exceeded, those expectations. Thank you especially, Anna and Kyle, for a night to remember. Will be back! |Wonderful atmosphere food and drink. We celebrated an anniversary here and it was \ngreat. They accommodated my wife's food allergies with no trouble at all. Great for any occasion especially a special occasion. |Called to make a reservation and was on hold for 20 minutes. Hostess who finally answered was unapologetic and said she was having a busy night. Not impressed. This is getting a habit at Canlis. Been there many times for 15 years but not worth the attitude anymore. Many other places with better food, better views and most of all better service. Not what it used to be. They obviously don't need my business anymore and it is time to move on.|Upscale restaurant. Fantastic wine list and the cocktails are really good too. Really enjoyed our meal here.|	2016-11-22 07:42:05.836877
33	Septime	Paris	80 Rue de Charonne, 75011 Paris, France	48.8535388000000026	2.38066939999999994	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAJwvA2smgQflF_2kD9aIBslV5RKoqH_cu4OmLgxXObX6ZZrBIqeWS9CKLO5hZG8k9YJQRqROa-dxFAQPTm6YIyMlsQC34XTdYo_WKUnD4gZqmEpVQh9-GGZf36A38yOuzhNtm_z5EISzg5VHv-jBa2LLP33mrHP7AcbwxzwzlTwDEhCsAVjpQMw-EOi0XbLxBuiOGhSw3uLhe2XNKa9RcdthigIPEpxkAg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJE6kCUghy5kcRmWSg3RUHIwM	3	4.5	\N	I hoped this place lived to its hype, but not really. So it is an affordable Michelin starred restaurant in Paris, for sure. You have to wait 2 or 3 weeks in general to get a table. I waited, oh I waited.\nBut then. The d�cor is minimalist, a bit like the food. Yes the dishes are perfectly cooked, but they lack fanciness. I was surprised nor amused. Service is great, though the place is small, obviously crowded and very noisy. It's a good 4 on 5 stars for sure, but I am not looking to go back anytime soon.|This place had good food, but nothing very inventive or that wowed me when I had lunch. Maybe dinner service is better?.. Overall Quite a bit different atmosphere from other Paris restaurants which I have eaten with single Michelin stars, I think they are getting extra credit for being different.. was hipster just as that started to be a thing.. |Didn't feel the creativity and quality of the dishes lived up to its hype (world's 50 best and michelin star). Main course of quail with blackberry was not that inspiring and just as commonplace as similar pairing of poultry and berry fruit found in states. Another main course has perfectly cooked fish but overwhelmed by accompanied herbs. Didn't feel like the quality of the ingredients gets to shine through after the manipulation.|Note that this review is for Clamato, the restaurant next door to Septime and under the same management. For some reason this restaurant does not appear on Google maps yet. Unlike Septime, Clamato does not take reservations and the focus is entirely on seafood. It's also a la carte. This was one of the best meals we had in Paris. Incredibly fresh, bright flavors enlivened but not overwhelmed by intriguing seasonings such as the paprika with the cooked mussels served chilled out of the shell. Arrive early if you want a seat. A great consolation if you can't get a seat at Septime. |The Michelin Star chef Bertrand is just amazing. One of the best table I ever eat at|	2016-11-22 07:43:38.844022
34	L'Abattoir	Vancouver	217 Carrall St, Vancouver, BC V6B 2J2, Canada	49.2831024999999983	-123.104437599999997	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAJ6rEaIbsYmfvOX5PjqykTy_am1WzJTnCXFLC0ZCME0DoE1-WiZh_pgUsNIw8uZsuzu-gwSmCd7l22IK_SugRXBz9Qk-zjb06kpli9jB2NpYnIeLlD1SSl4wVEyTPvQgIe4h3Nde_On4X-3A0A-dk06SCUMe0uHZUYBj5m1ij4FKEhCntXjk1U5U_dgR6L85tHY3GhThISrL1dvHJnGjh94MEdo3cxoNIA&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJJy1TTHdxhlQRgQQZgi9ga9o	3	4.5	\N	Amazing food and amazing cocktails! Yes, this place is expensive, but you get your money's worth. . . beyond the food and drinks, the ambiance and service are both stellar. This is an ideal place for an anniversary or a special date. You can also get a taste of the good life during their happy hour, from 5:30 to 6:30 at the bar. They have specials on their house red and white wine, a lager, and a rotating specialty cocktail. On top of that, all of their appetizers are half off (they're listed as "cold dishes"and "hot dishes"). The portions are small, but that's to be expected somewhere as fancy as this. We listened to the recommendations of our excellent bartender, Katie, and had the mushroom risotto, the nectarine gazpacho, the steelhead sushi roll, and the octopus--and each one was a hit! Honestly, we were thrilled with every aspect of our experience. I'll confess that as a former bartender and server I can be a little hard to impress when it comes to customer service, but Katie was definitely impressive! L'Abattoir was the culinary highlight of our week in Vancouver. |Really a special place. We dined here twice (dinner & brunch). Both meals were outstanding. The dining area in the back looks out on the bricks of the old jail house courtyard. Service was impeccable and the food well thought out and executed. |Go here every time I can when visiting from Victoria. This little gem in Gastown, Vancouver has beautifully crafted drinks and a creative dinner menu. Everything is really good in quality. Yes, this place is expensive, but it's totally worth going every time I visit. The menu changes quite frequently. Nice urban-rustic-chic atmosphere.|As a vegetarian there's not a whole lot on the menu I can eat, but the cocktails are fantastic. I go back repeatedly when waiting for restaurants in the area as there are usually spots at the bar and they have a great selection of drinks. It's a really nice space and the staff are very friendly.|A perennial favourite for casual fine dining. Completely unpretentious, but impeccable service in a beautiful space - get a table in the rear atrium for a more secluded, quiet dinner. Beautiful plates of impeccable-quality and inventive food, with a great cocktail and wine menu to go with it.|	2016-11-22 07:53:08.358744
36	Bongo Room	Chicago	1470 N Milwaukee Ave, Chicago, IL 60622, United States	41.9085328999999973	-87.6749296999999927	https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference=CoQBdwAAAChqXD9Tu2TKZF4UgwH5G-aFFxL_xeoK1-WwM0clt7nkshSoUp5_RVltIbjXz8fd96NUczhmct_zD-bHZ-KhTIgDmtT2FT5XW6dhauNMtxl6CqPie1QWQKFUmRlADbGnHXfxLPqZqXWQDLDSqXAL8u3ltwqJ0UrSv4x5u4BpyhRAEhDHgcd1ntIK5tL0cGrL485SGhQOA-xsXIETgX9UAKMchEvRVS-0Fg&key=AIzaSyDA_1IcTtbdm68wu8-OQUkChoe7FlXhVgc	ChIJI3njV8bSD4gR2aImx5J3HEg	2	4.29999999999999982	\N	I tagged along on my boyfriend's pancake pilgrimage to the Bongo Room. The Nutella banana pancakes were tasty but not divine. If you worship pancakes then you will adore this holy mountain of flapjacks. For others, the rest of healthy American-style menu has something for everyone from Cobb salads to classic diner sandwiches. Good price. Good portions. Friendly service. |The food is wonderfully creative and seems to be healthy. You ABSOLUTELY have to try the pancakes (triple berry cheesecake is my favorite).  I wouldn't go just for the bloody Mary's or mimosas. They are a little pricey but the food is delicious|Always very hard to get a seat, but for good reason. Food is amazing with a ton of great choices. They will be very accomodating to you on portion size as well, and will price accordingly... (Say they have an order of special pancakes, you can get 1 instead of 3)|Most people come here for breakfast and it's great but a little secret...the lunches are really good as well. They sell a Greek salad with chicken as a half salad for $9.50 that is truly one of the best deals in the area. Big, fresh and healthy. Check it out|Standard brunch place. I really didn't find anything that special about the food. Standard run of the mil brunch fare. Service was fast which was nice!|	2016-11-22 07:54:43.96126
\.


--
-- Name: restaurants_rest_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('restaurants_rest_id_seq', 36, true);


--
-- Data for Name: statuses; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY statuses (status_id, status_code) FROM stdin;
1	Pending
2	Confirmed
\.


--
-- Name: statuses_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('statuses_status_id_seq', 2, true);


--
-- Data for Name: trackings; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY trackings (tracking_id, user_id, rest_id, visited, tracking_note, tracking_review, tcreated_at) FROM stdin;
4	1	3	t	\N	The s'mores cake and the pistachio shake were so good! There's always a long line but the desserts are worth the wait.	2016-11-14 05:05:14.902048
5	8	3	t	\N	I loved their Reese's inspired cake!	2016-11-14 05:06:31.163129
9	1	7	t	\N	Brisket and truffle mac n cheese are an amazing combo!	2016-11-15 20:22:49.702521
10	1	8	t	\N	All the fries!	2016-11-16 20:15:03.849415
11	1	9	t	\N	The June Roll was incredible. The restaurant is easy to miss because it doesn't have a sign hanging outside.	2016-11-16 23:28:38.428736
13	1	10	f	Go with Jill!	\N	2016-11-17 01:57:32.732832
14	1	11	t	\N	The namesake State Bird (quail) was fantastic!	2016-11-20 00:00:14.26848
16	2	13	f	\N	\N	2016-11-20 01:30:01.312891
20	2	16	f	I want to try their chicken sandwich.	\N	2016-11-20 01:48:29.041957
25	2	20	f	They have poke bowls!	\N	2016-11-20 01:57:12.451546
27	2	22	f	Great reviews in Seattle Magazine. 	\N	2016-11-20 01:59:29.542453
28	2	23	f	\N	\N	2016-11-20 02:01:53.423222
29	2	24	f	Everyone at work loves The Harvest Vine.	\N	2016-11-20 02:02:31.120492
30	2	25	t	\N	Loved the muhammarah and the desserts. Modern take on Middle Eastern classics.	2016-11-20 02:03:28.022444
31	2	26	t	\N	Great late-night burgers in Cap Hill. 	2016-11-20 02:04:19.596473
23	2	18	t	\N	Awesome meal. Will definitely go again!	2016-11-20 01:55:47.131645
26	2	21	t	Lots of different steak cuts on their menu. 	The skirt steak served with marrow butter was incredible.	2016-11-20 01:58:42.20541
24	2	19	t	\N	\N	2016-11-20 01:56:45.992088
32	1	27	f	You need to go before 4pm - they close early!	\N	2016-11-21 03:48:57.86002
33	1	28	f	Go with Yasmien when she's in SF next!	\N	2016-11-21 04:46:35.339845
34	1	22	f	Go with Nimmy when I'm home next!	\N	2016-11-21 04:50:11.723031
35	2	4	f	Nada suggested the sweet and savory bread puddings.	\N	2016-11-21 04:58:20.557553
38	10	29	t	\N	Had a wonderful meal prepared by Thomas Keller himself. It was wonderful catching up with Tom. The dessert was heavenly!	2016-11-22 07:36:53.209127
39	10	30	t	\N	So glad that Chef Crenn invited us to her private dinner at Altelier Crenn. Really innovative!	2016-11-22 07:38:34.554994
40	10	31	f	Must go with Jay-Z and Blue when we're in NYC next!	\N	2016-11-22 07:41:20.56547
41	10	32	f	Nada really recommends this restaurant. Will have to invite her to join.	\N	2016-11-22 07:42:05.836877
42	10	33	t	\N	My favorite in Paris!	2016-11-22 07:43:38.844022
44	1	34	f	\N	\N	2016-11-22 07:53:08.358744
45	1	35	f	Their poutine sounds amazing.	\N	2016-11-22 07:53:39.284799
46	1	36	t	\N	My absolute favorite breakfast restaurant - think dessert masquerading as breakfast!	2016-11-22 07:54:43.96126
\.


--
-- Name: trackings_tracking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('trackings_tracking_id_seq', 56, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY users (user_id, username, email, password, first_name, last_name, ucreated_at) FROM stdin;
1	nbseikri	nada@nada.com	$2b$12$k49t/1ynDbTSR1qi2mRvfu645p1STWnwQ6petkxtM5Yz8rd.TVySy	Nada	Bseikri	2016-11-13 05:31:31.625805
2	nbulale	nimco@nimco.com	$2b$12$HheQ3X.85awol9DLmPE6Ze2tpTaT.U1iCy1.BIKHPJebYoKCo6cOm	Nimco	Bulale	2016-11-13 05:33:57.096919
3	abulale	amal@amal.com	$2b$12$GE5PYNo8FCSWeYwubwYRCeyNo8Guel12BjKrs5Eu9aaasMV/fZCjS	Amal	Bulale	2016-11-13 05:34:22.153736
4	falmo	falmo@falmo.com	$2b$12$Rtlt3tzPq1AjNd7RlRg81.RQ.nnNtP7VdRCE/vIWqQi.CNXl5ovvu	Farah	Almo	2016-11-13 05:34:57.562258
6	mbseikri	malik@malik.com	$2b$12$rYfSLTxFvDIrEBCb5fezKuF1iHEz7jhCwIjxpyYILY6q92kzkF4Mi	Malik	Bseikri	2016-11-13 05:37:11.178342
7	mustbseikri	must@must.com	$2b$12$7NRPWmmY9i.hp57HrdFwiebV2j9pMtKwCzOwNszQin4dXPXCipVcC	Mustafa	Bseikri	2016-11-13 05:38:00.988758
8	relias	rainier@rainier.com	$2b$12$OzFw3p4/t8ExZHxunqRpRua3X7JweVSMtDbgXKxhWikFQldRfUSDi	Rainier	Elias	2016-11-13 05:38:33.171028
9	ssoleimani	sara@sara.com	$2b$12$rSgAGQQtH39i.3gu0DDtnOKrX2VvvCT.B9p7yLiULr9OWDpyqSZ.W	Sara	Soleimani	2016-11-13 05:56:27.556622
10	bknowles	bey@bey.com	$2b$12$XG8n8cDp8zwwZFeRd2yCOuO50pg5NLfN8mR5xKHizn/l3VKAdHxsy	Beyonce	Knowles-Carter	2016-11-13 06:01:37.450728
12	krowland	kelly@kelly.com	$2b$12$qin4WYqqQ8nAogcCHOKxC.fS6mXomFODSR3Du1UGs82Ks8KXdw5la	Kelly	Rowland	2016-11-16 23:44:12.747171
14	fhawasli	farah@farah.com	$2b$12$JSCHNrtXpHS97nZfUv6KQ.oqR2hkh/p2ng96PheHJk1GwFSHjP4VC	Farah	Hawasli	2016-11-19 22:51:46.47615
15	mgellar	mgellar@mgellar.com	$2b$12$oOu.cjlgY5EWRYu1YkQIoOpJ/hyGDXx154fyLSAFpKySTNWjFnl0y	Monica	Gellar	2016-11-22 19:37:24.850587
16	cbing	cbing@cbing.com	$2b$12$BBjTcyuHCfySlLH5YETLNO4S0AkUdLGkTrQ8xMvaW8PIh05lUOR/W	Chandler 	Bing	2016-11-22 19:37:52.593719
17	pbuffet	pbuffet@pbuffet.com	$2b$12$UO6flb1Ke.Yuz8CYggnLqOH7IpRkfzKmf19wESJif0X5OYcDXKVLK	Phoebe	Buffet	2016-11-22 19:39:08.321935
18	jtribiani	jtribiani@jtribiani.com	$2b$12$/TnINavkI4CCFOv.S1X2cuQadmos8n3Va55uL7DUE.aOE.6dj/Mii	Joey	Tribiani	2016-11-22 19:40:02.165687
19	rgreen	rgreen@rgreen.com	$2b$12$DrczV90PI2fAXzUZ1jOTDOvuDvTAcc5LZmr0aNg7VhhkSEJZenN3G	Rachel	Green	2016-11-22 19:40:46.404339
20	rgellar	rgellar@rgellar.com	$2b$12$lW/11EtbP5P82uYFM3VhDeD3Y1IlYPbi0uzMSSYEySt6m8A1qJLwK	Ross	Gellar	2016-11-22 19:41:48.782377
21	mscott	mscott@mscott.com	$2b$12$Wno1TgRjxV1BSLq.j4Dl4eH.6xxJs2JAjX1VswJJKm4IR8qH3luWu	Michael	Scott	2016-11-22 19:42:33.748119
22	pbeesly	pbeesly@pbeesly.com	$2b$12$BJ6cOyZtHlR7k5gE9D6Rq.u99j/QlIHz2H//h210fBM848vGbYJgm	Pam 	Beesly	2016-11-22 19:44:04.93344
23	jhalpert	jhalpert@jhalpert.com	$2b$12$73Ta0cnPmK4xn6p3XJEecOq4MPleIu7iLqP3HUq/3FZuUhHPPkjIu	Jim 	Halpert	2016-11-22 19:44:37.155912
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('users_user_id_seq', 23, true);


--
-- Name: friends_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY friends
    ADD CONSTRAINT friends_pkey PRIMARY KEY (friend_id);


--
-- Name: restaurants_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY restaurants
    ADD CONSTRAINT restaurants_pkey PRIMARY KEY (rest_id);


--
-- Name: statuses_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY statuses
    ADD CONSTRAINT statuses_pkey PRIMARY KEY (status_id);


--
-- Name: trackings_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY trackings
    ADD CONSTRAINT trackings_pkey PRIMARY KEY (tracking_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: friends_friend_one_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY friends
    ADD CONSTRAINT friends_friend_one_fkey FOREIGN KEY (friend_one) REFERENCES users(user_id);


--
-- Name: friends_friend_two_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY friends
    ADD CONSTRAINT friends_friend_two_fkey FOREIGN KEY (friend_two) REFERENCES users(user_id);


--
-- Name: friends_status_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY friends
    ADD CONSTRAINT friends_status_fkey FOREIGN KEY (status) REFERENCES statuses(status_id);


--
-- Name: trackings_rest_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY trackings
    ADD CONSTRAINT trackings_rest_id_fkey FOREIGN KEY (rest_id) REFERENCES restaurants(rest_id);


--
-- Name: trackings_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY trackings
    ADD CONSTRAINT trackings_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

