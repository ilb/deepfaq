from setuptools import setup, find_packages

app_dependencies = [
    "bottle==0.12.18",
    "gunicorn==20.0.4",
    "inject==4.0.0",
    "requests>=2.0.0",
    "bottle-swagger-2==2.0.8",
    "deeppavlov~=0.14.0",
    "ilb-pycontext==2.0.3"
]

dev_dependencies = [
    "pytest",
    "wheel"
]

setup(
    name="deepfaq",
    version="0.0.1",
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
