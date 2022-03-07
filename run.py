import os
from flask import Flask, render_template # import Flask class


app = Flask(__name__)  # create an instance and store in a variable 'app'


@app.route("/")  # decorator (a way of wrapping functions)
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")
    # page_title is a var name, could be called almost anything else


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "192.168.1.6"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)