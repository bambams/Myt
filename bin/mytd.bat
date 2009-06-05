@echo off

pushd "%~dp0\.."

SET PYTHONPATH=%~dp0\..
python mytd/main.py %*

popd
