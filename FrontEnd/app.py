# FrontEnd/app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_URL = "http://127.0.0.1:8000"  # FastAPI server


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            user_id = int(request.form["user_id"])
            category = request.form["category"].strip()
            value = float(request.form["value"])
        except Exception as e:
            error = "Invalid input: " + str(e)
            return render_template("index.html", result=None, error=error)

        resp = requests.post(f"{API_URL}/activities/", params={
            "user_id": user_id, "category": category, "value": value
        })
        if resp.status_code != 200:
            error = resp.text
        else:
            result = resp.json()
    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
