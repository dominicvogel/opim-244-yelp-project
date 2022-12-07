# from copy import Error
import requests
import json
from app.yelp_load import API_KEY

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
    return review_data
    


def georgetown_yelp(term,location):

    request_url = f"https://api.yelp.com/v3/businesses/search?term={term}&location={location}"
    headers = {
        'Authorization':'Bearer %s' % API_KEY
        }
    response = requests.get(request_url,headers=headers)
    data = json.loads(response.text)
    # breakpoint()
    # create a list of ids for all search results that meet the parameters
    ids = []
    # print(data)
    for business in data["businesses"]:
        ids.append(business["id"])
    
    return ids, headers


if __name__ == "__main__":

    term = input("Please input what food you are craving (default: 'burgers'): ") or "burgers"
    location = input("\nSearching late night food options near Georgetown\nIf you would like to search another location please input or press enter: ") or "georgetown"
    search_options = georgetown_yelp(term, location)
    late_night_options = fetch_latenight(search_options[0], search_options[1])
    if len(late_night_options) == 0:
        print("Sorry, no options found.")
    else:
        print("Here are your late night options in", location,": ")
        for option in late_night_options:
            print("NAME: ", option["name"])
            print("RATING: ", option["rating"])
            print("LOCATION: ", option["location"]["display_address"])
            try:
                print("PRICE: ", option["price"])
            except KeyError as e:
                print()
            print()
            review_data = fetch_reviews(option["id"], search_options[1])
            countreviews = 1
            for review in review_data["reviews"]:
                print("REVIEW", countreviews, ":")
                print(review["text"])
                print()
                countreviews+=1
                if countreviews>3:
                    break

