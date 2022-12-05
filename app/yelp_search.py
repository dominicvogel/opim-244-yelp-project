from copy import Error
import requests
import json
from yelp_load import API_KEY

# from IPython.display import Image, display 

def fetch_latenight(ids, headers):
# parse through the list of ids for businesses that are open overnight
# use different request url to receive specific overnight parameters
    late_night_options = []
    
    for id in ids:
        specific_request_url = f"https://api.yelp.com/v3/businesses/{id}"
        specific_response = requests.get(specific_request_url,headers=headers)
        specific_data = json.loads(specific_response.text)
        count = 0
        try:
            daily_hours = specific_data["hours"][0]["open"]
            for day in daily_hours:
                if day["is_overnight"]==True:
                    count+=1
                if count>=2:
                    late_night_options.append(specific_data)
                    break
        # keyerrors arise when the hours are not listed for a location
        except KeyError as e:
            print()
    
    return late_night_options



def fetch_reviews(id, headers):
    review_url=f"https://api.yelp.com/v3/businesses/{id}/reviews"
    review_response = requests.get(review_url,headers=headers)
    review_data = json.loads(review_response.text)
    countreviews = 1
    for review in review_data["reviews"]:
        print("REVIEW", countreviews, ":")
        print(review["text"])
        print()
        countreviews+=1
        if countreviews>3:
            break


def georgetown_yelp(TERM="sandwiches",LOCATION="Georgetown"):
    request_url = f"https://api.yelp.com/v3/businesses/search?term={TERM}&location={LOCATION}"
    headers = {
        'Authorization': 'Bearer %s' % API_KEY
        }
    response = requests.get(request_url,headers=headers)
    data = json.loads(response.text)
    
    # create a list of ids for all search results that meet the parameters
    ids = []
    for business in data["businesses"]:
        ids.append(business["id"])

    late_night_options = fetch_latenight(ids, headers)
    
    if len(late_night_options) == 0:
        print("Sorry, no options found. What else are you craving?")

    # display information from the late night options
    print("Here are your late night options in", LOCATION,": ")
    for option in late_night_options:
        print("NAME: ", option["name"])
        print("RATING: ", option["rating"])
        print("LOCATION: ", option["location"]["display_address"])
        try:
            print("PRICE: ", option["price"])
        except KeyError as e:
            print()
        print()
        fetch_reviews(option["id"], headers)


georgetown_yelp(TERM="hummus")


