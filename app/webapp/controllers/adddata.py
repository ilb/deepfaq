import json
import inject
from bottle import request, Bottle, HTTPResponse
from webapp.services.errors import DataParseException

from webapp.services.addservice import AddDataService

add_d = Bottle()


@add_d.post("/")
@inject.autoparams()
def add_data(add_data_service: AddDataService) -> HTTPResponse:
    try:
        json_object = json.load(request.body)
        add_data_service.add_data(json_object)
        return HTTPResponse(status=200)
    except DataParseException as dpe:
        ans = {"error": repr(dpe)}
        return HTTPResponse(status=550, body=ans)
    except Exception as e:
        ans = {"error": repr(e)}
        return HTTPResponse(status=550, body=ans)
