import os
from flask import Flask, render_template # import Flask class


app = Flask(__name__)  # create an instance and store in a variable 'app'


@app.route("/")  # decorator (a way of wrapping functions)
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "192.168.1.6"),
        port=int(os.environ.get("PORT", "8080")),
        debug=True)