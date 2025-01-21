from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():  # put application's code heres
    return 'Hello Flask!'

@app.route("/hello/<name>")
def hello_name(name):
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
