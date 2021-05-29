from flask import Flask, render_template, url_for, jsonify, request
import requests

import Percentage
import Data


app = Flask(__name__)

result = None

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ajax", methods = ['POST', 'GET'])
def ajax():
    global result

    print(request)

    df = Data.get_data('data\\instagram.json')
    term = request.args.get('query')
    percentage = Percentage.percentage(term, df)

    response = percentage
    print(response)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)