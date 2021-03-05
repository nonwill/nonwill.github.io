---
title: "PostgreSQL  注册启动 及 停用卸载 批处理脚本"
date: 2015-01-12T23:12:27+08:00
draft: false
tags: [PostgreSQL]
categories: [db]
---
注册启动  pg_install.bat
```bat
@echo off
set PGSQL_DIR=%~dp0
 
if not "%PGSQL_HOME%"=="" (
    if not "%PGSQL_HOME%"=="%PGSQL_DIR%" (
        echo PGSQL_HOME=%PGSQL_HOME% != PGSQL_DIR=%PGSQL_DIR%
        goto pg_ends
    )
) else (
    set PGSQL_HOME=%PGSQL_DIR%
    echo PGSQL_HOME must be set as PGSQL_DIR=%PGSQL_DIR%
)
 
set PATH=%PGSQL_HOME%bin;%PGSQL_HOME%lib;%PATH%
 
pg_isready -h localhost 1>nul 2>nul
@if "%ERRORLEVEL%" == "0" (
    echo PostgreSQL is running.
    goto pg_ends
)
 
echo "PGSQL_HOME = %PGSQL_HOME%"
echo Install and start PostgreSQL server ...
 
 
@if not exist %PGSQL_HOME%data (
	mkdir %PGSQL_HOME%data
	%PGSQL_HOME%bin/initdb --username=root --pgdata=%PGSQL_HOME%data --encoding=UTF8 --locale=chinese
	rem @if not "%ERRORLEVEL%" == "0" (
	rem There ERRORLEVEL is 2, but successfully inited
	rem 	echo PostgreSQL initdb failed.
	rem 	goto pg_ends
	rem )
) 
 
pg_ctl register --pgdata=%PGSQL_HOME%data -N pgsql_srv -S demand
net start pgsql_srv
rem pg_ctl -w start
 
pg_isready -h localhost 1>nul 2>nul
@if "%ERRORLEVEL%" == "0" (
	echo PostgreSQL server started successfully
) else (
	echo Failed to start PostgreSQL server
)
 
:pg_ends
 
cmd /K
```
停用卸载 pg_stop.bat
```bat
@echo off
 
echo Stop and uninstall PostgreSQL server ...
 
pg_isready -h localhost 1>nul 2>nul
@if "%ERRORLEVEL%" == "0" (
    net stop pgsql_srv
)
 
pg_ctl unregister -N pgsql_srv
@if "%ERRORLEVEL%" == "0" echo Unregister PostgreSQL successfully
 
:my_ends
```
