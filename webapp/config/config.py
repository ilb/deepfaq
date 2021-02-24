import inject
from inject import Binder
from webapp.services.deeppavlov_faq_bot.faqbot import FaqBot


def init() -> None:
    inject.configure(build_container)


def build_container(binder: Binder) -> Binder:
    binder.bind(FaqBot, FaqBot(work_dir()))
    return binder


def host() -> str:
    return "127.0.0.1"


def port() -> int:
    return 5005


def work_dir() -> str:
    return "../FAQBot_work_dir/"
