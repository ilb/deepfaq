# deepfaq
Сервис ответов

FAQ bot web app based on Bottle
=========================================

Install deps:
----------
```shell script
pip install -e .[dev]
```


Build package:
----
```shell script
python setup.py sdist bdist_wheel
```

Install package:
----

```shell script
pip install dist/*.whl
```

Test:
-----
```shell script
pytest
```

Run package:
----

```shell script
(PYTHON_EXEC)/bin/webapp
/usr/bin/python3.7/bin/webapp
```

You can check it running on `http://localhost:5005/swagger/`