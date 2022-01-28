py -m venv venv-build
call venv-build\Scripts\activate
pip3 install setuptools wheel
pip3 install -r requirements.txt
setup.py sdist bdist_wheel
for /D %%i in (*.egg-info) do rd /S /Q "%%i"
rd /S /Q venv-build build
