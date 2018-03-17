from flask import Flask, render_template

web_app = Flask(__name__)

@web_app.route("/<string:name>/")
def index(name):
    return render_template("index.html", name=name)

web_app.run()
