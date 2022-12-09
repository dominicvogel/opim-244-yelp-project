
# this is the "web_app/routes/input_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.yelp_search import fetch_latenight, fetch_reviews, georgetown_yelp

input_routes = Blueprint("input_routes", __name__)

@input_routes.route("/input/form")
def input_form():
    print("INPUT FORM...")
    return render_template("input_form.html")

# default is only responding to GET requests so we need to specify POST
@input_routes.route("/input/display", methods=["GET", "POST"])
def input_display():
    print("DISPLAYING OPTIONS...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)
    print(type(request_data))
    term = request_data["term"]
    location = request_data["location"]
    print(term)
    try:
        ids = georgetown_yelp(term, location)
        businesses = fetch_latenight(ids[0],ids[1])
        if(len(businesses))==0:
            flash("No food found, try something else", "danger")
            return redirect("/input/form")


        for biz in businesses:
            review_data = fetch_reviews(biz["id"], ids[1])
            current_reviews=[]
            countreviews = 1
            for review in review_data["reviews"]:
                current_reviews.append(review["text"])
                countreviews+=1
                if countreviews>3:
                    break
            biz["reviews"] = current_reviews
        flash("Fetched Yelp Data", "success")   
        return render_template("input_display.html",
            businesses = businesses
        )

    except Exception as err:
        print('OOPS', err)

        flash("Error, these inputs displayed no results. Check your inputs and try again.", "danger")
        return redirect("/input/form")

#
# API ROUTES
#

# @stocks_routes.route("/api/stocks.json")
# def stocks_api():
#     print("STOCKS DATA (API)...")

#     # for data supplied via GET request, url params are in request.args:
#     url_params = dict(request.args)
#     print("URL PARAMS:", url_params)
#     symbol = url_params.get("symbol") or "NFLX"

#     try:
#         df = fetch_stocks_data(symbol=symbol)
#         data = df.to_dict("records")
#         return {"symbol": symbol, "data": data }
#     except Exception as err:
#         print('OOPS', err)
#         return {"message":"Market Data Error. Please try again."}, 404