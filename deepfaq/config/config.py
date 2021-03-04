from functools import lru_cache

import os
import inject
from inject import Binder
from pathlib import Path
from pycontext.context import AppContext
from pycontext.reader import ContextXmlReader, WebXmlReader

from deepfaq.services.deeppavlov_faq_bot.faqbot import FaqBot

context = AppContext.from_readers([
    ContextXmlReader("deepfaq"),
    WebXmlReader(Path(__file__).parent.joinpath("web.xml"))
])


def init() -> None:
    os.environ["DP_SKIP_NLTK_DOWNLOAD"] = "TRUE" # http://docs.deeppavlov.ai/en/master/integrations/settings.html
    inject.configure(build_container)


def build_container(binder: Binder) -> Binder:
    binder.bind(FaqBot, FaqBot(workdir()))
    return binder


@lru_cache(1)
def host() -> str:
    return context.get("ru.bystrobank.apps.deepfaq.host")


@lru_cache(1)
def port() -> int:
    return context.get("ru.bystrobank.apps.deepfaq.port")


@lru_cache(1)
def workdir() -> str:
    return context.get("ru.bystrobank.apps.deepfaq.workdir")
