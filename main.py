from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
    response.raise_for_status()
    data = response.json()
    return render_template("index.html", blogs=data)


@app.route("/blog/<id_number>")
def get_post(id_number):
    response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
    response.raise_for_status()
    data = response.json()
    print(data)
    for blog in data:
        if blog["id"] == int(id_number):
            return render_template("post.html", blog=blog,)


if __name__ == "__main__":
    app.run(debug=True)
