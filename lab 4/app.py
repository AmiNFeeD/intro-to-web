from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():  # put application's code heres
    return 'Hello Flask!'

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
