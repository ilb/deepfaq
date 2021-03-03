"""
get answer service
"""
from deepfaq.services.deeppavlov_faq_bot.faqbot import FaqBot
import inject


class GetAnswer:
    @inject.autoparams()
    def __init__(self, faq_bot: FaqBot):
        self.faq_bot = faq_bot

    def get_answer(self, model, question: str):
        # bot = faqbot.FaqBot(self.work_dir)
        bot = self.faq_bot
        answer, probability = bot.ask_model(model, question)
        ans = {"answer": answer[0], "probability": probability[0]}
        return ans
