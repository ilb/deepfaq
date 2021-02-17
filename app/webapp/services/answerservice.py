"""
get answer service
"""
from deeppavlov_faq_bot import faqbot


class AnswerService:

    def __init__(self, work_dir: str):
        self.work_dir = work_dir

    def get_answer(self, model, question: str):
        bot = faqbot.FaqBot(self.work_dir)
        answer, probability = bot.ask_model(model, question)
        ans = {"answer": answer[0], "probability": probability[0]}
        return ans
