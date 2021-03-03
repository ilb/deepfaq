#!/usr/bin/env python
"""
A library for creating a bot of the FAQ type with many models (FAQ thematics) based on the library deeppavlov.
When creating a bot, it is necessary to provide a working directory
(where it is possible to create and delete files and directories).
Each model (theme) is stored in its own catalog. When FAQ data is try added to a non-existent model,
that model is created.
You need to train the model after new data is added to it (train_model(model name)).
"""
from deeppavlov import train_model, build_model
import json

from deepfaq.services.deeppavlov_faq_bot.utils.file_utils import BotFilesUtil


class CreateBotException(Exception):
    pass


class ModelNotFoundException(Exception):
    pass


class FaqBot:

    def __init__(self, work_dir: str):
        try:
            if not work_dir:
                raise CreateBotException('work_dir param is empty')
            self.file_util = BotFilesUtil(work_dir)
            self.file_util.create_work_dirs()
            self.model_list = self.__get_model_list()
        except Exception as ex:
            raise CreateBotException(ex)

    def train_model(self, model_name: str):
        if self.__model_is_exist(model_name):
            train_model(self.file_util.get_config_model_path(model_name))
        else:
            raise ModelNotFoundException("model {} not found".format(model_name))

    def ask_model(self, model_name, question: str):
        if self.__model_is_exist(model_name):
            model = build_model(self.file_util.get_config_model_path(model_name))
            result = model([question])
            return result
        else:
            raise ModelNotFoundException("model {} not found".format(model_name))

    def __get_model_list(self):
        path = self.file_util.get_model_list_path()
        with open(path, 'r', encoding='utf-8') as f:
            json_obj = json.load(f)
            result = json_obj[self.file_util.get_model_list_json_name()]
            f.close()
            return result

    def add_data_to_model(self, model_name, question, answer: str):
        if not self.__model_is_exist(model_name):
            self.file_util.create_model(model_name)
        header = 'Question,Answer' + '\n'
        write_string = '\"' + question + '\"' + ',' + '\"' + answer + '\"' + '\n'
        # check string count in file
        with open(self.file_util.get_csv_file_path(model_name), 'r', encoding='utf-8') as f_r:
            size = sum(1 for _ in f_r)
            f_r.close()
        # add question an answer
        with open(self.file_util.get_csv_file_path(model_name), 'a', encoding='utf-8') as f:
            if size == 0:
                f.write(header)
            f.write(write_string)
            f.close()
        # self.train_model(model_name)

    def __model_is_exist(self, model_name: str):
        self.model_list = self.__get_model_list()
        if model_name:
            if model_name in self.model_list:
                return True
            else:
                return False
        else:
            return False
