Library for creating a FAQ-type bot using the library deeppavlov   
=========================

Uses miniconda distribution, makes environment for development process, builds python package. 

Install deps:
----------
```shell script
make bootstrap
```

Test:
-----
```shell script
make test 
```

Publish:
----
```shell script
make publish 
```
Result wheel and package will be on dist/
You can test it, following this:

```shell script
pip install dist/deeppavlov_faq_bot*.whl
python
```
```shell script
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from deeppavlov_faq_bot.deeppavlov_faq_bot import Library
>>> lib = Library()
>>> lib.call()
2.22.0
>>>
```
