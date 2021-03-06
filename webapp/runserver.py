"""
This script runs the webapp application using a development server.
"""

from os import environ
from webapp import app
from config import DEBUG

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT, debug=DEBUG)
