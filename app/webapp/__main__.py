import os
import sys
import yaml
from bottle import Bottle
from webapp.config import config
from webapp.controllers.answer import answer
from webapp.controllers.adddata import add_d

from bottle_swagger import SwaggerPlugin

if __package__ == "__main__":
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

this_dir = os.path.dirname(os.path.abspath(__file__))
with open("{}/{}/openapi.yml".format(this_dir, "docs")) as f:
    swagger_def = yaml.load(f)

app = Bottle()


def main():
    config.init()
    app.mount("/webapp/answer/", answer)
    app.mount("/webapp/add/", add_d)
    app.install(
        SwaggerPlugin(swagger_def, validate_swagger_spec=False, serve_swagger_ui=True, swagger_ui_suburl="/swagger/"))
    sys.exit(
        app.run(
            server="gunicorn",
            host=config.host(),
            port=config.port(),
            debug=True,
        )
    )
