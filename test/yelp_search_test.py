# this is the "test/yelp_search_test.py" file...

from app.yelp_search import fetch_latenight, fetch_reviews, georgetown_yelp, late_night_options

def test_fetch_latenight():

    #assert 2 + 2 == 4

    assert fetch_latenight() == late_night_options