from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Welcome to Flask!</h1>"

@app.route("/welcome")
def welcome():
    return "<h2>Welcome navigation!</h2>"

@app.route("/welcome/<user>")
def welcome_user(user):
    return f"<h2>Hi {user}, welcome to flask!</h2>"

@app.route("/square", methods=["GET"])
def squarenumber():
    if request.method == "GET":
        if request.args.get("num") is None:
            return render_template("square.html")
        elif (request.args.get("num") == ""):
            return "<html><body> <h1>Invalid input</h1></body></html>"
        else:
            number = request.args.get("num")
            square = float(number) ** 2
            return render_template("solution.html", squareofnum=square, num=number)


if __name__ == "__main__":
    app.run(debug=True)