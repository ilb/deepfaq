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
```
