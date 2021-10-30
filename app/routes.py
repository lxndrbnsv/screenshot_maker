import time

from app import app
from flask import jsonify, request, send_file

from app.modules.screenshot import MakeScreenshot, CropScreenshot


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

    return send_file(f"../{filename}")

