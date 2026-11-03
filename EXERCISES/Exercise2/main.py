from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():

    query = request.args.get("q", "")

    results = []

    if query:
        url = "https://images-api.nasa.gov/search"
        
        response = requests.get(url,params={"q":query, "media_type" : "image"})
        data=response.json()

        results = data["collection"]["items"]

    return render_template("index.html", results=results, query=query)


app.run(debug=True)