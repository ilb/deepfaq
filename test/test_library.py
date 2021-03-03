import unittest
import shutil

from deepfaq.services.deeppavlov_faq_bot.faqbot import FaqBot, ModelNotFoundException, CreateBotException


class MyTestCase(unittest.TestCase):

    def test_create_bot_without_work_dir_path(self):
        with self.assertRaises(CreateBotException):
            bot = FaqBot("")

    def test_empty_model_list(self):
        path = "../FAQBot_work_dir_1/"
        bot = FaqBot(path)

        with self.assertRaises(ModelNotFoundException):
            bot.ask_model("faq1", "контакты")
        with self.assertRaises(ModelNotFoundException):
            bot.train_model("faq1")

        with self.assertRaises(ModelNotFoundException):
            bot.train_model("")
        with self.assertRaises(ModelNotFoundException):
            bot.ask_model("", "")

        shutil.rmtree(path)

    def test_model_create(self):
        path = "../FAQBot_work_dir_2/"
        model_name = "faq"
        bot = FaqBot(path)
        bot.add_data_to_model(model_name, "Декан", "Шашкин Александр Иванович")
        bot.add_data_to_model(model_name, "Телефон деканата", "84732208266")
        bot.add_data_to_model(model_name, "Шашкин Александр Иванович",
                              "доктор физико-математических наук, профессор, заведующий кафедрой математического и "
                              "прикладного анализа, член президиума УМО классических университетов, "
                              "академик International Academy of Refrigeration. Зам. председателя специализированного "
                              "совета по защите кандидатских диссертаций (специальность – 01.02.04), член докторского "
                              "совета (специальность – 01.02.04). Руководитель грантов РФФИ.")
        bot.add_data_to_model(model_name, "Заместитель декана по научной работе", "Задорожний Владимир Григорьевич")
        bot.add_data_to_model(model_name, "Задорожний Владимир Григорьевич",
                              "доктор физико-математических наук, профессор, Соросовский профессор, "
                              "член Американского математического общества, заведующий кафедрой нелинейных колебаний")
        bot.add_data_to_model(model_name, "Заместитель декана по учебной работе (дневное отделение)",
                              "Лазарев Константин Петрович")
        bot.add_data_to_model(model_name, "Лазарев Константин Петрович",
                              "кандидат физико-математических наук, доцент кафедры вычислительной математики и "
                              "прикладных информационных технологий")
        bot.add_data_to_model(model_name, "Заместитель декана по довузовской подготовке", "Каширина Ирина Леонидовна")
        bot.add_data_to_model(model_name,
                              "Какие существуют направления обучения на ПММ, пмм Факультет прикладной математики, "
                              "информатики и механики",
                              "Направления обучения: Направления бакалавриата:Прикладная математика и информатика, "
                              "Математическое обеспечение и администрирование информационных систем,Механика и "
                              "математическое моделирование,Фундаментальные информатика и информационные технологии,"
                              "Бизнес-информатика,Прикладная информатика. Направления магистратуры: Математическое "
                              "обеспечение и администрирование информационных систем,Бизнес-информатика,Прикладная "
                              "математика и информатика,Механика и математическое моделирование,Фундаментальные "
                              "информатика и информационные технологии")
        bot.add_data_to_model(model_name, "Есть ли на Вашем факультете заочная форма обучения?",
                              "Добрый день! Есть в магистратуре по направлению Бизнес-информатика")
        bot.add_data_to_model(model_name,
                              "В следующем году готовлюсь  поступать на ""бизнес-информатику"". Планируется ли "
                              "создание бюджетных мест?И хотелось бы узнать проходные баллы на коммерческое отделение "
                              "и  стоимость обучения за год.",
                              "Создание бюджетных мест пока не планируется, на это направление они не выделены. "
                              "Проходных баллов как таковых нет, минимальное требование - перейти порог по требуемым "
                              "ЕГЭ. Стоимость: 52000")
        bot.train_model(model_name)
        answer, probability = bot.ask_model(model_name, "направления обучения на ПММ")
        self.assertEqual(answer[0], "Направления обучения: Направления бакалавриата:Прикладная математика и "
                                    "информатика, Математическое обеспечение и администрирование информационных "
                                    "систем,Механика и математическое моделирование,Фундаментальные информатика и "
                                    "информационные технологии,Бизнес-информатика,Прикладная информатика. Направления "
                                    "магистратуры: Математическое обеспечение и администрирование информационных "
                                    "систем,Бизнес-информатика,Прикладная математика и информатика,Механика и "
                                    "математическое моделирование,Фундаментальные информатика и информационные "
                                    "технологии")
        shutil.rmtree(path)


if __name__ == '__main__':
    unittest.main()
