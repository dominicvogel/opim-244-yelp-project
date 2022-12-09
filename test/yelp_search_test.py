# this is the "test/yelp_search_test.py" file...

from app.yelp_search import fetch_latenight, fetch_reviews, georgetown_yelp
import json
import requests
from app.yelp_load import API_KEY
 
def test_georgetown_yelp():
    result = georgetown_yelp("pizza", "georgetown")
    request_url = "https://api.yelp.com/v3/businesses/search?term=pizza&location=georgetown"
    headers = {'Authorization':'Bearer %s' % API_KEY}
    response = requests.get(request_url,headers=headers)
    data = json.loads(response.text)
    ids = []
  #for business in data["businesses"]:
  #    ids.append(business["id"])
    assert isinstance(data, dict)
    assert "businesses" in data.keys()

def test_fetch_reviews():
    headers = {'Authorization':'Bearer %s' % API_KEY}    
    result = fetch_reviews("9X0F8gl4mPSSFHkxSB2lXA", headers)
    review_url= "https://api.yelp.com/v3/businesses/9X0F8gl4mPSSFHkxSB2lXA/reviews"
    assert review_url == "https://api.yelp.com/v3/businesses/9X0F8gl4mPSSFHkxSB2lXA/reviews"
    review_response = requests.get(review_url,headers=headers)
    review_data = json.loads(review_response.text)
    assert isinstance(review_data, dict)

def test_fetch_latenight():
    headers = {'Authorization':'Bearer %s' % API_KEY}    
    result = fetch_reviews("9X0F8gl4mPSSFHkxSB2lXA", headers)
    specific_request_url = "https://api.yelp.com/v3/businesses/9X0F8gl4mPSSFHkxSB2lXA"
    specific_response = requests.get(specific_request_url,headers=headers)
    specific_data = json.loads(specific_response.text)
    assert isinstance(specific_data, dict)
    assert "hours" in specific_data.keys()

