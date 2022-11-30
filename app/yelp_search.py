from requests import cookies
from copy import Error
import requests
import json
from yelp_load import API_KEY

# from IPython.display import Image, display 

def georgetown_yelp(TERM="sandwiches",LOCATION="georgetown"):
    request_url = f"https://api.yelp.com/v3/businesses/search?term={TERM}&location={LOCATION}"
    headers = {
        'Authorization': 'Bearer %s' % API_KEY
        }
    response = requests.get(request_url,headers=headers)
    data = json.loads(response.text)
    # print(len(data["businesses"]))
    # print(type(data))
    # print(data.keys())
    # print(data["businesses"][0])
    # print(data["businesses"][0]["id"])

    # list of ids for all search results that meet the parameters
    ids = []
    for business in data["businesses"]:
        ids.append(business["id"])
    # print(ids)
    # id = ids[0]
    
    # parse through the list of ids for businesses that are open overnight
    # use different request url to receive specific overnight parameters
    late_night_options = []
    for id in ids:
        specific_request_url = f"https://api.yelp.com/v3/businesses/{id}"
        #review_url=f"https://api.yelp.com/v3/businesses/{id}/reviews"
        response = requests.get(specific_request_url,headers=headers)
        #review_response = requests.get(review_url,headers=headers)
        data = json.loads(response.text)
        #review_data = json.loads(review_response.text)


        # check if the business is open overnight for each day of the week if it is for 3 or more days then
        # we add to the late night options
        count = 0
        # print(data.keys())
        try:
            daily_hours = data["hours"][0]["open"]
            # print(daily_hours)
            for day in daily_hours:
                if day["is_overnight"]==True:
                    count+=1
                if count>=2:
                    late_night_options.append(data)
                    break
        # keyerrors arise when the hours are not listed for a location
        except KeyError as e:
            print()
    # print(late_night_options)
    # display information from the late night options
    print("Here are your late night options: ")
    for option in late_night_options:
        # print(option.keys())
        print("NAME: ", option["name"])
        print("RATING: ", option["rating"])
        print("LOCATION: ", option["location"]["display_address"])
        print("PRICE: ", option["price"])
        print()
        reviewid=option["id"]
        review_url=f"https://api.yelp.com/v3/businesses/{reviewid}/reviews"
        review_response = requests.get(review_url,headers=headers)
        review_data = json.loads(review_response.text)
        # print(review_data)
        countreviews = 1
        # review_list = []
        # print(review_data["reviews"])
        for review in review_data["reviews"]:
            print("REVIEW", countreviews, ":")
            print(review["text"])
            print()
            countreviews+=1
        #   review_list.append(review["text"])
        #   countreviews+=1
        #   if countreviews==5:
        #     break

        # print(review_list)
        # print(review_data["reviews"][0]["text"])




georgetown_yelp(TERM="crepes")


