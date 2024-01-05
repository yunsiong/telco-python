# telco-python

Python bindings for [Telco](https://telco.re).

# Some tips during development

To build and test your own wheel, do something along the following lines:

```
set TELCO_VERSION=16.0.1-dev.7 # from C:\src\telco\build\tmp-windows\telco-version.h
set TELCO_EXTENSION=C:\src\telco\build\telco-windows\x64-Release\lib\python3.10\site-packages\_telco.pyd
cd C:\src\telco\telco-python\
pip wheel .
pip uninstall telco
pip install telco-16.0.1.dev7-cp34-abi3-win_amd64.whl
```
