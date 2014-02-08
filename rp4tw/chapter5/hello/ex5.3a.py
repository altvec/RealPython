from flask import Flask

app = Flask(__name__)

# decorations to link the function to a url
@app.route("/")
@app.route("/hello")
@app.route("/hw")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, world!"

# start the dev server using run()
if __name__ == "__main__":
    app.run()

