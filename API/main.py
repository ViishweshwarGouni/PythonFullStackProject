from fastapi import FastAPI
from src import db, logic

app = FastAPI(title="EchoFootprintTracker API")

@app.post("/users/")
def create_user(name: str, email: str, password: str, age: int = None, location: str = None):
    return db.add_user(name, email, password, age, location)

@app.post("/activities/")
def create_activity(user_id: int, category_id: int, description: str, value: float, unit: str, emission_factor: float):
    emission = logic.log_activity(user_id, category_id, description, value, unit, emission_factor)
    return {"message": "Activity logged", "emission": emission}

@app.get("/users/{user_id}/activities")
def get_activities(user_id: int):
    return db.get_user_activities(user_id)

@app.get("/users/{user_id}/logs")
def get_logs(user_id: int):
    return db.get_user_logs(user_id)

@app.get("/users/{user_id}/recommendations")
def recommendations(user_id: int):
    return logic.get_recommendations(user_id)
