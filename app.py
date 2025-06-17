from flask import Flask, render_template
from routes import register_routes

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)