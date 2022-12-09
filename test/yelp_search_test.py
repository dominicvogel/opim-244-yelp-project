# this is the "test/yelp_search_test.py" file...

from app.yelp_search import fetch_latenight, fetch_reviews, georgetown_yelp
import json

#def test_fetch_latenight():

    #assert 2 + 2 == 4

 #   assert fetch_latenight() == late_night_options
 
 
def georgetown_yelp_test(term, location):
    result = georgetown_yelp("pizza", "georgetown")
    assert isinstance(result, dict)
    assert "businesses" in result.keys()
    assert isinstance(result["businesses"], str)

#def fetch_reviews_test(id, headers):
    result = fetch_reviews(id, headers)
    review_url=f"https://api.yelp.com/v3/businesses/{id}/reviews"
    assert isinstance(id, dict)
    assert review_url == "https://api.yelp.com/v3/businesses//reviews"

    
#def test_fetch_latenight(ids, headers):
    result = fetch_latenight(ids, headers)
    business = result["businesses"]
    assert isinstance(business, json)
    assert "hours" in business.keys()
    assert "open" in business.hours()

    assert len(result) >= 20

#def test_data_fetching():
#    result = fetch_stocks_data("NFLX")
#    assert isinstance(result, DataFrame)
#
#    assert "timestamp" in result.columns
#    assert "adjusted_close" in result.columns
#    assert "high" in result.columns
#    assert "low" in result.columns
#
#    assert len(result) >= 100
#