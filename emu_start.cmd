@echo OFF
pushd "%~dp0"
%~dp0../hugo.exe server &
popd
