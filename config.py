import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'amTestKey'
    CAMERA_FOLDER = basedir
    SERIAL_TIME = 3;
    REMOTE_FILE = 'Test'
