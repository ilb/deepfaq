from setuptools import setup, find_packages

app_dependencies = [
    "bottle==0.12.18",
    "gunicorn==20.0.4",
    "inject==4.0.0",
    "requests>=2.0.0",
    "bottle-swagger-2==2.0.8"
]

dev_dependencies = [
    "pytest",
    "wheel"
]

setup(
    name="webapp",
    version="0.0.1",
    description="This is web app based on bottle.",
    author="kvadro",
    author_email="mail@gmail.com",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=app_dependencies,
    extras_require={"dev": dev_dependencies, },
    entry_points={
         "console_scripts": [
             "webapp=webapp.__main__:main"
         ]
     }
)
