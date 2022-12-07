# opim-244-yelp-project
OPIM244 final project on Yelp. Created by Sachi Tejani, James Kim, Dominic Vogel

## Setup

Create and activate a virtual environment:
```sh
conda create -n yelp-env python=3.8

conda activate yelp-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration
[Obtain an API Key](https://www.yelp.com/developers/documentation/v3/authentication) from Yelp (i.e. `API_KEY`).

Then create a local ".env" file and provide the keys like this:

```sh
# this is the ".env" file...

API_KEY="_________"
```

## Usage 
Run Yelp Script:

```sh
python -m app.yelp_search
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run
# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

