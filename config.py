import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or ""
    MAX_CONTENT_LENGTH = 2048 * 2048
