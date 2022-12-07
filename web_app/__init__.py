# this is the "web_app/__init__.py" file...

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.input_routes import input_routes
# from web_app.routes.display_routes import display_routes
# SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(input_routes)
    # app.register_blueprint(display_routes)

    
    # app.config["SECRET_KEY"] = SECRET_KEY
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)