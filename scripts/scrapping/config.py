from dotenv.main import load_dotenv
import os

load_dotenv()

mk2_home = os.getenv("mk2_home")
all_movies = os.getenv("all_movies")
api_url = os.getenv("api_url")
movie_url = os.getenv("movie_url")
theaters_url = os.getenv("theaters_url")