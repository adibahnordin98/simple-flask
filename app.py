from flask import Flask, render_template


app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = 'any secret key'

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    # HOST = "0.0.0.0"
    # PORT = 5000

    # httpserver.serve(app, host=HOST, port=PORT)
    app.run(port=5000, debug=True)
