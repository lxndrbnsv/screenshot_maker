import os

from app import app
from flask import jsonify, request, send_file, after_this_request

from app.modules.screenshot import MakeScreenshot, CropScreenshot, RemoveScreenshot


@app.route("/")
@app.route("/index")
def index():
    return jsonify(status=None)


@app.route("/make_screenshot", methods=["GET"])
def make_screenshot():
    print(request, flush=True)
    url = request.args.get("url")
    print(url, flush=True)

    filename = MakeScreenshot(url=url).filename
    CropScreenshot(filename=filename)

    @after_this_request
    def remove(name=filename):
        os.remove(name)

    return send_file(f"../{filename}")

