@echo off

pushd "%~dp0\.."

SET PYTHONPATH=%~dp0\..
python myt/main.py

popd
