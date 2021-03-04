from setuptools import setup, find_packages

app_dependencies = [
    "bottle==0.12.18",
    "gunicorn==20.0.4",
    "uvloop==0.14.0", # pin uvloop version which supports Python >=3.5 (required by deeppavlov -> uvicorn)
    "inject==4.0.0",
    "requests>=2.0.0",
    "bottle-swagger-2==2.0.8",
    "deeppavlov~=0.14.0",
    "ilb-pycontext==2.1.0"
]

dev_dependencies = [
    "pytest",
    "wheel"
]

setup(
    name="ilb-deepfaq",
    version="0.0.4",
    description="FAQ bot based on deep learning",
    url="https://git.ilb.ru/ilb.ru/deepfaq",
    author="kvadro1",
    author_email="kvadro1@gmail.com",
    maintainer="Maxim Kuznetsov",
    maintainer_email="kuznetsov_me@bystrobank.ru",
    python_requires=">=3.6",
    packages=find_packages(exclude=["test.*", "test"]),
    package_data={'': ['*.json', '*.pkl', "*.yml", "*.xml"]},
    install_requires=app_dependencies,
    extras_require={"dev": dev_dependencies},
    entry_points={
         "console_scripts": [
             "deepfaq=deepfaq.__main__:main"
         ]
     }
)
