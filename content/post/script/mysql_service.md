---
title: "MYSQL 注册启动 及 停用卸载 批处理脚本"
date: 2015-01-12T19:12:27+08:00
draft: false
tags: [MYSQL]
categories: [db]
---
注册启动  my_install.bat
```bat
@echo off
set MYSQL_DIR=%~dp0
rem set MYSQL_DIR=%cd%
 
if not "%MYSQL_HOME%"=="" (
    if not "%MYSQL_HOME%"=="%MYSQL_DIR%" (
        echo MYSQL_HOME=%MYSQL_HOME% != MYSQL_DIR=%MYSQL_DIR%
        goto my_ends
    )
) else (
    set MYSQL_HOME=%MYSQL_DIR%
    echo MYSQL_HOME must be set as MYSQL_DIR=%MYSQL_DIR%
)
 
set PATH=%MYSQL_HOME%bin;%MYSQL_HOME%lib;%PATH%
 
mysqladmin -uroot  ping 1>nul 2>nul
@if "%ERRORLEVEL%" == "0" (
    echo Mysql is running.
    goto my_ends
)
 
echo "MYSQL_HOME = %MYSQL_HOME%"
echo Install and start mysql server ...
 
mysqld --install mysql_srv
sc config mysql_srv start= DEMAND
rem sc query mysql_srv
net start mysql_srv
rem sc query mysql_srv
 
mysqladmin -uroot  ping 1>nul 2>nul
@if "%ERRORLEVEL%" == "0" echo "Mysql started successfully"
 
:my_ends
 
cmd /K
```
停用卸载 my_uninstall.bat
```bat
@echo off
set MYSQL_DIR=%~dp0
rem set MYSQL_DIR=%cd%
 
if not "%MYSQL_HOME%"=="" (
    if not "%MYSQL_HOME%"=="%MYSQL_DIR%" (
        echo MYSQL_HOME=%MYSQL_HOME% != MYSQL_DIR=%MYSQL_DIR%
        goto my_ends
    )
) else set MYSQL_HOME=%MYSQL_DIR%
 
set PATH=%MYSQL_HOME%\bin;%MYSQL_HOME%\lib;%PATH%
echo "MYSQL_HOME = %MYSQL_HOME%"
echo Stop and uninstall mysql server ...
 
mysqladmin -uroot  ping  1>nul 2>nul
@if "%ERRORLEVEL%" == "0" (
    net stop mysql_srv
    rem sc query mysql_srv
)
 
mysqld --remove mysql_srv
 
:my_ends
 
pause
```
