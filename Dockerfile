FROM python:3.7
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install -e .[dev] \
&& python setup.py sdist bdist_wheel \
&& pip install dist/*.whl

CMD ["deepfaq"]