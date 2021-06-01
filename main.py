from flask import Flask, render_template, url_for, jsonify, request
import requests

import Percentage
import Data
import Interest_by_date


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

    term = request.args.get('query')

    insta = Data.get_data('data\\instagram.json')
    insta_percent = Percentage.percentage(term, insta, 'text')

    recipe = Data.get_data('data\\recipe.json')
    recipe_percent = Percentage.percentage(term, recipe, 'text')

    packaged = Data.get_data('data\\packaged.json')
    packaged_percent = Percentage.percentage(term, packaged, 'Name')

    line_insta = Interest_by_date.group_by_date(term, insta)
    line_recipe = Interest_by_date.group_by_date(term, recipe)

    response = {"percentage": [insta_percent, recipe_percent, packaged_percent],
                "interest": [line_insta, line_recipe]}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)