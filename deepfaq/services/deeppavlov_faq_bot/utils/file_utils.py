"""
Library for creating / configuring models for FAQ bot
"""
from pathlib import Path
import shutil
import os
import json


class BotFilesUtil:
    """PATH_TO_WORK_DIR = "../FAQBot_work_dir/"
    MODELS_FOLDER_PATH = PATH_TO_WORK_DIR + "models/"
    MODEL_VECT_PATH = 'vectorizer/'
    MODEL_DICT_PATH = 'dict/'
    MODEL_LEARN_PATH = 'learn/'
    MODEL_LIST_FILE_PATH = MODELS_FOLDER_PATH + 'models_list.json'
    MODEL_LIST_JSON_NAME = 'model_list'
    CSV_FILE_NAME = 'data.csv'
    DEFAULT_CONFIG_PATH = MODELS_FOLDER_PATH + 'faq_skill_default_config.json'
    MODEL_CONFIG_FILE = 'config.json'
    VECTOR_DEFAULT_FILE_NAME = 'tfidf_vectorizer_ruwiki.pkl'
    DEFAULT_LEARN_FILE_NAME = 'tfidf_cos_sim_classifier.pkl'"""

    def __init__(self, work_dir: str):
        self.path_to_work_dir = os.path.abspath(work_dir) + "/"
        # path_to_work_dir = "../FAQBot_work_dir/"
        self.models_folder_path = self.path_to_work_dir + "models/"
        self.model_vect_path = 'vectorizer/'
        self.model_dict_path = 'dict/'
        self.model_learn_path = 'learn/'
        self.model_list_file_path = self.models_folder_path + 'models_list.json'
        self.model_list_json_name = 'model_list'
        self.csv_file_name = 'data.csv'
        self.default_config_path = self.models_folder_path + 'faq_skill_default_config.json'
        self.model_config_file = 'config.json'
        self.vector_default_file_name = 'tfidf_vectorizer_ruwiki.pkl'
        self.default_learn_file_name = 'tfidf_cos_sim_classifier.pkl'
        self.path = os.path.dirname(os.path.dirname(__file__))

    def get_model_list_path(self):
        return self.model_list_file_path

    def get_csv_file_path(self, model_name: str):
        return self.models_folder_path + model_name + '/' + self.csv_file_name

    def get_config_model_path(self, model_name: str):
        return self.models_folder_path + model_name + '/' + self.model_config_file

    def get_model_list_json_name(self):
        return self.model_list_json_name

    def create_work_dirs(self):
        try:
            Path(self.path_to_work_dir).mkdir(parents=True, exist_ok=True)
            Path(self.models_folder_path).mkdir(parents=True, exist_ok=True)
            if not os.path.isfile(self.models_folder_path + 'models_list.json'):
                shutil.copy(self.path + '/utils/files/models_list.json', self.model_list_file_path)
            if not os.path.isfile(self.default_config_path):
                shutil.copy(self.path + '/utils/files/faq_skill_default_config.json',
                            self.default_config_path)
            return True
        except Exception as e:
            print(e)
            return False

    def copy_plk_for_new_model(self, model_name: str):
        model_path = self.models_folder_path + model_name + "/"
        if not os.path.isfile(model_path + self.model_vect_path + self.vector_default_file_name):
            shutil.copy(self.path + '/utils/files/' + self.vector_default_file_name,
                        model_path + self.model_vect_path + self.vector_default_file_name)
        if not os.path.isfile(model_path + self.model_dict_path + self.default_learn_file_name):
            shutil.copy(self.path + '/utils/files/' + self.default_learn_file_name,
                        model_path + self.model_dict_path + self.default_learn_file_name)

    def add_model_to_list(self, model_name: str):
        with open(self.model_list_file_path, 'r', encoding='utf-8') as models_list_file_r:
            json_obj = json.load(models_list_file_r)
            models_list_file_r.close()
            with open(self.model_list_file_path, 'w', encoding='utf-8') as models_list_file_w:
                json_obj[self.model_list_json_name].append(model_name)
                json.dump(json_obj, models_list_file_w)
                models_list_file_w.close()

    def generate_model_config(self, model_name: str):
        with open(self.default_config_path, 'r', encoding='utf-8') as defaultConfig:
            def_config_json = json.load(defaultConfig)
            path_to_data_file = self.models_folder_path + model_name + "/" + self.csv_file_name
            def_config_json["dataset_reader"]["data_path"] = os.path.abspath(path_to_data_file)
            def_config_json["metadata"]["variables"]["MODELS_PATH"] = os.path.abspath(
                self.models_folder_path + model_name)
            path_to_model_config = self.models_folder_path + model_name + "/" + self.model_config_file
            with open(path_to_model_config, 'w', encoding='utf-8') as model_config:
                json.dump(def_config_json, model_config, sort_keys=True, indent=4)
                model_config.close()
        defaultConfig.close()

    def create_model(self, model_name: str):
        try:
            if self.create_model_workaround(model_name):
                self.generate_model_config(model_name)
                self.copy_plk_for_new_model(model_name)
                self.add_model_to_list(model_name)
                return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def create_dir(path: str):
        if not os.path.isdir(path):
            Path(path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def create_file(file_name: str):
        if not os.path.isfile(file_name):
            f = open(file_name, 'tw', encoding='utf-8')
            f.close()

    def create_model_workaround(self, model_name: str):
        try:
            model_root_path = self.models_folder_path + model_name + '/'
            self.create_dir(model_root_path)
            self.create_dir(model_root_path + self.model_vect_path)
            self.create_dir(model_root_path + self.model_dict_path)
            # self.create_dir(model_root_path + self.MODEL_LEARN_PATH)
            self.create_file(model_root_path + self.csv_file_name)
            return True
        except Exception as e:
            print(e)
            return False
