py -m venv venv-build
call venv-build\Scripts\activate
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
setup.py sdist bdist_wheel
for /D %%i in (*.egg-info) do rd /S /Q "%%i"
rd /S /Q venv-build build
