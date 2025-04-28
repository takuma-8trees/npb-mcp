from fastapi import FastAPI
from tracker.client import OkaHiromiTracker 

app = FastAPI()
tracker = OkaHiromiTracker()  

@app.get("/profile")
def get_profile():
    return tracker.get_profile()

@app.get("/career")
def get_career():
    return tracker.get_career_hitting_stats()

@app.get("/season")
def get_season(year: int):
    return tracker.get_season_hitting_stats(year)

@app.get("/monthly")
def get_monthly(year: int):
    return tracker.get_monthly_hitting_stats(year)

@app.get("/game")
def get_game(year: int):
    return tracker.get_game_by_game_hitting_stats(year)

