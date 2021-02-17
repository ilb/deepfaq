from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='deeppavlov_faq_bot',
    packages=['deeppavlov_faq_bot', 'deeppavlov_faq_bot.utils', 'deeppavlov_faq_bot.utils.files'],
    package_data={'deeppavlov_faq_bot.utils.files': ['*.*', 'deeppavlov_faq_bot/utils/files/']},
    version='0.0.1',
    description='This is deeppavlov_faq_bot',
    install_requires=required
    # add some information, like name, email, etc
)
