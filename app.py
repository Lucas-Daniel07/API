from flask import Flask, render_template
import requests

api_url = "https://jsonplaceholder.typicode.com/users/"
user_list = requests.get(api_url).json()
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('templates/index.html', users = user_list)

@app.route("/teste")
def second_test():
    return "<p> Outro teste! </p>"

if __name__ == "__main__":
    app.run()
