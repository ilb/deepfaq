FAQ bot web app based on Bottle
=========================================

Install deps:
----------
before command install lib deep_pavlov_faq_bot (see library/readme.md) 
```shell script
python setup.py develop
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
/usr/bin/python3.8.5/bin/webapp
```

You can check it running on `http://localhost:5005/`
