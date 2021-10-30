import os
from multiprocessing import Process


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

    file_handle = open(filename, "rb")

    def stream_and_remove_file():
        yield from file_handle
        file_handle.close()
        os.remove(filename)

    return app.response_class(stream_and_remove_file())
