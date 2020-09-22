import os
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

    
app = Flask(__name__)
app.secret_key = 'SECRET_KEY'


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html", page_title='About')

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
              request.form["name"]))

    return render_template("contact.html", page_title='Contact')

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title='Careers')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)