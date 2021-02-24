import shutil
import time
import requests
from bottle import run
from bottle import Bottle
from threading import Thread
from webapp.config import config
from webapp.controllers.answer import answer
from webapp.controllers.adddata import add_d
from start_stop_server import MyServer

model_name = "faq"
jsonQuestion = {
    "model": model_name,
    "q": "второй отдел"
}
jsonData = {
    "model": model_name,
    "faq": [
        {
            "q": ["Декан"],
            "a": "Шашкин Александр Иванович"
        },
        {
            "q": ["Телефон деканата"],
            "a": "84732208266"
        },
        {
            "q": ["Шашкин Александр Иванович"],
            "a": "доктор физико-математических наук, профессор, заведующий кафедрой математического и прикладного "
                 "анализа, член президиума УМО классических университетов "
        },
        {
            "q": ["Заместитель декана по научной работе"],
            "a": "Задорожний Владимир Григорьевич"
        },
        {
            "q": ["Какие существуют направления обучения на ПММ, пмм Факультет прикладной математики, информатики и "
                  "механики"],
            "a": "Направления обучения: Направления бакалавриата:Прикладная математика и информатика, Математическое "
                 "обеспечение и администрирование информационных систем,Механика и математическое моделирование,"
                 "Фундаментальные информатика и информационные технологии,Бизнес-информатика,Прикладная информатика. "
                 "Направления магистратуры: Математическое обеспечение и администрирование информационных систем,"
                 "Бизнес-информатика,Прикладная математика и информатика,Механика и математическое моделирование,"
                 "Фундаментальные информатика и информационные технологии "
        },
        {
            "q": ["Как будет проходить распределение по кафедрам на ПМИ?"],
            "a": "Распределение по кафедрам проходит после второго курса по результатам первых трёх экзаменационных "
                 "сессий. Конкурс похож на конкурс при поступлении: рассчитывается сумма баллов за экзамены, "
                 "выставляются приоритеты. Студенты, которые учатся по договору, зачисляются на желаемую кафедру вне "
                 "конкурса. "
        },
        {
            "q": ["Зачем нужен второй отдел?"],
            "a": "Во втором отделе нужно взять справку для военкомата, чтобы тебе дали отсрочку и не забрали служить "
                 "Родине."
        }
    ]
}


def test_add_date_and_ask():
    app = Bottle()
    config.init()
    app.mount("/webapp/answer/", answer)
    app.mount("/webapp/add/", add_d)

    def begin():
        run(app=app, server=server)

    url = "http://{}:{}".format(config.host(), config.port())
    server = MyServer(host=config.host(), port=config.port())
    Thread(target=begin).start()
    time.sleep(1)
    try:

        r = requests.post(url + '/webapp/answer/')
        assert r.status_code == 450  # parse error

        r = requests.post(url + '/webapp/answer/', json=jsonQuestion)
        assert r.status_code == 550  # no models yet

        r = requests.post(url + '/webapp/add/')
        assert r.status_code == 550  # wrong data add

        r = requests.post(url + '/webapp/add/', json=jsonData)
        assert r.status_code == 200  # add data OK

        r = requests.post(url + '/webapp/answer/', json=jsonQuestion)
        assert r.status_code == 200
        json_answer = r.json()
        assert json_answer['answer'] == "Во втором отделе нужно взять справку для военкомата, чтобы тебе дали " \
                                        "отсрочку и не забрали служить Родине."  # valid answer
    finally:
        server.shutdown()
        time.sleep(1)
        shutil.rmtree(config.work_dir())
