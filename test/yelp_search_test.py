# this is the "test/yelp_search_test.py" file...

from app.yelp_search import fetch_latenight, fetch_reviews, georgetown_yelp
import json
import requests
from app.yelp_load import API_KEY
 
def test_georgetown_yelp():
    result = georgetown_yelp("pizza", "georgetown")
    request_url = "https://api.yelp.com/v3/businesses/search?term=pizza&location=georgetown"
    headers = {
        'Authorization':'Bearer %s' % API_KEY
        }
    response = requests.get(request_url,headers=headers)
    data = json.loads(response.text)
    ids = []
    for business in data["businesses"]:
        ids.append(business["id"])
        print(business["id"])
    assert isinstance(business["id"], str)

#def test_fetch_reviews():
#    result = fetch_reviews("9X0F8gl4mPSSFHkxSB2lXA", API_KEY)
#    review_url= "https://api.yelp.com/v3/businesses/9X0F8gl4mPSSFHkxSB2lXA/reviews"
#    assert isinstance(id, dict)
#    assert review_url == "https://api.yelp.com/v3/businesses//reviews"
#
#def fetch_reviews(id, headers):
#    review_url=f"https://api.yelp.com/v3/businesses/{id}/reviews"
#    review_response = requests.get(review_url,headers=headers)
#    review_data = json.loads(review_response.text)
#    return review_data
    
    
#def test_fetch_latenight(ids, headers):
#   result = fetch_latenight(ids, headers)
#   business = result["businesses"]
#   assert isinstance(business, json)
#   assert "hours" in business.keys()
#   assert "open" in business.hours()
#
#   assert len(result) >= 20
#
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