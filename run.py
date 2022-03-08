import os
import json
from flask import Flask, render_template, request, flash # import Flask class and libraries
if os.path.exists("env.py"):
    import env

app = Flask(__name__)  # create an instance and store in a variable 'app'
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")  # decorator (a way of wrapping functions)
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
    # page_title is a var name, could be called almost anything else


@app.route("/about/<member_name>")  # The angle brackets will pass in data from the URL path, into our view below
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)  
    # 1st member is the variable name being passed through into our html file
    # 2nd member is the member object we created above on line 25.


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received you message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "192.168.1.6"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)