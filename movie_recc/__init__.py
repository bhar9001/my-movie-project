import os
from flask import Flask
from movie_recc.routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://bharat:6i7pGJwI9JI2rfzx@cluster0.kumjka8.mongodb.net/movie")
    app.db = client.get_default_database()
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
    )

    app.register_blueprint(pages)
    return app