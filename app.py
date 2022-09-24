import logging
from flask import Flask, send_from_directory

from main.views import view_blueprint
from loader.load import load_blueprint


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(view_blueprint)
app.register_blueprint(load_blueprint)

logging.basicConfig(filename="basic.log", level=logging.INFO)



@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
