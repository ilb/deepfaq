import json
import inject
from bottle import request, Bottle, HTTPResponse

from webapp.services.getanswerservice import GetAnswer

answer = Bottle()


@answer.post("/")
@inject.autoparams()
def get_answer(answer_service: GetAnswer) -> HTTPResponse:
    try:
        json_object = json.load(request.body)
        model = (json_object['model'])
        question = (json_object['q'])
    except Exception as ex:
        ans = {"error": repr(ex)}
        return HTTPResponse(status=450, body=ans)

    try:
        result = answer_service.get_answer(model, question)
        ans = json.dumps(result, ensure_ascii=False)
        if not ans:
            ans = {"error": "model {} not found".format(model)}
            return HTTPResponse(status=550, body=ans)
    except Exception as e:
        ans = {"error": repr(e)}
        return HTTPResponse(status=550, body=ans)

    return HTTPResponse(status=200, body=ans)
