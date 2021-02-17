"""
add answers service

{
    "model": "frontoffice",
    "faq": [
        {
            "q": ["Что такое X?", "Где я могу приобрести X?"],
            "a": "X - это наше самое выгодное предложение, вы можете приобрести его наших магазинах."
        }
    ]
}
"""
from deeppavlov_faq_bot import faqbot

from webapp.services.errors import DataParseException


class AddDataService:

    def __init__(self, work_dir: str):
        self.work_dir = work_dir

    def add_data(self, json_data):
        try:
            bot = faqbot.FaqBot(self.work_dir)
            model_name = json_data["model"]
            input_arr = list()
            for faq in json_data["faq"]:
                answer = faq["a"]
                for question in faq["q"]:
                    input_arr.append({"q": question, "a": answer})
        except Exception as ex:
            raise DataParseException(ex)

        if not input_arr or len(input_arr) <= 0:
            raise DataParseException("Input date is empty")

        try:
            for rec in input_arr:
                bot.add_data_to_model(model_name, rec['q'], rec['a'])
            bot.train_model(model_name)
        except Exception as exp:
            raise Exception(exp)
