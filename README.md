# opim-244-yelp-project
OPIM244 final project on Yelp. Created by Sachi Tejani, James Kim, Dominic Vogel

## Setup

Create and activate a virtual environment:
```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
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
pthon app/yelp_search.py