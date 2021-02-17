import os
import sys
from bottle import Bottle

if __package__ == "__main__":
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from webapp.config import config
from webapp.controllers.answer import answer
from webapp.controllers.adddata import add_d

app = Bottle()


def main():
    config.init()
    app.mount("/webapp/answer/", answer)
    app.mount("/webapp/add/", add_d)

    sys.exit(
        app.run(
            server="gunicorn",
            host=config.host(),
            port=config.port(),
            debug=True,
        )
    )
