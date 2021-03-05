---
title: "使用qt开发gsoap程序"
date: 2015-01-16T11:32:32+08:00
draft: false
tags: [gsoap,c++,c]
categories: [soap,Qt,c++,c]
---
## 1. 从http://gsoap2.sourceforge.net/下载最新的gsoap2源码包。  
>通过http://www.cppblog.com/qiujian5628/archive/2008/10/11/54019.html(EXP1)初步了解了gsoap2的使用方法（下属示例使用了该文章的例子）。  
## 2. qt项目目录结构
>其中add.cpp、add_client.cpp分别为服务端和客户端的例子程序， gsoap2应用项目需要放在learning目录下。
```bash
gsoap2                    # gsoap2 开发文档根目录
│  gsoap.pri              # 引入gsoap2开发用源码文件
│  gsoap28.pro            # 根项目文件
│ 
├─bin		        # gsoap2工具链(来自于sourceforge上下载的源码包)及编译后的二进制文件
│      soapcpp2.exe
│      wsdl2h.exe
│
├─gsoap                   # gsoap2开发用源码文件所在目录(来自于sourceforge上下载的源码包)
│      .dirstamp
│      dom.c
│      dom.cpp
│      stdsoap2.c
│      stdsoap2.cpp
│      stdsoap2.h
│      typemap.dat
│
└─leaning                # gsoap2应用程序所在根目录
    │  leaning.pri       # gsoap2应用用的源码及命令头文件
    │  leaning.pro       # 应用程序管理
    ├─nsmap              # 接口定义文件所在目录
    │      add.h         # 接口文件名字必须与gsoap2项目中GSOAP_NAME值一样
    │      calc.h
    ├─add                # 服务器应用目录
    │      add.pro       # 服务器项目
    │      main.cpp      # 项目源码(来自于(EXP1)所述文档)
    ├─add_client         # 客户端应用目录
    │      add_client.pro # 客户端项目
    │      main.cpp      # 客户端源码(来自于(EXP1)所述文档)
    ├─calc
    │      calc.pro
    │      main.cpp
    ├─calc_client
           calc_client.pro
           main.cpp
```
## 3. gsoap2应用程序项目
gsoap28.pro
```c
TEMPLATE = subdirs
SUBDIRS += leaning
```
gsoap.pri
```c
INCLUDEPATH += $${PWD}/gsoap
 
HEADERS += $${PWD}/gsoap/stdsoap2.h
 
contains(CONFIG,use_c_gsoap_api) {
    SOURCES += $${PWD}/gsoap/stdsoap2.c \
               $${PWD}/gsoap/dom.c
} else {
    SOURCES += $${PWD}/gsoap/stdsoap2.cpp \
               $${PWD}/gsoap/dom.cpp
}
 
LIBS += -lws2_32
```
leaning.pri
```c
DESTDIR = $${PWD}/../bin
 
include($${PWD}/../gsoap.pri)
INCLUDEPATH += $${PWD}/nsmap
 
#contains(CONFIG,soap_server) {
    !exists(./temp):system("mkdir  temp")
    SOAP_GEN_DIR= ./temp/$${GSOAP_NAME}
    !exists($${SOAP_GEN_DIR}):system("cd temp && mkdir $${GSOAP_NAME}")
    !exists($${SOAP_GEN_DIR}/$${GSOAP_NAME}.wsdl) {
        system("soapcpp2.exe -d./$${SOAP_GEN_DIR} ./nsmap/$${GSOAP_NAME}.h")
    }
#}
 
SOAP_GEN_DIR= $${PWD}/temp/$${GSOAP_NAME}
 
SOAP_M_HEADERS += $${SOAP_GEN_DIR}/soapH.h \
                  $${SOAP_GEN_DIR}/soapStub.h
SOAP_M_SOURCES += $${SOAP_GEN_DIR}/soapC.cpp \
                  $${SOAP_GEN_DIR}/soapServer.cpp
 
SOAP_C_HEADERS += $${SOAP_GEN_DIR}/soapH.h\
                  $${SOAP_GEN_DIR}/soapStub.h
SOAP_C_SOURCES += $${SOAP_GEN_DIR}/soapC.cpp \
                  $${SOAP_GEN_DIR}/soapClient.cpp
 
SOAP_L_SOURCES += $${SOAP_GEN_DIR}/soapC.cpp \
                  $${SOAP_GEN_DIR}/soapClientLib.cpp \
                  $${SOAP_GEN_DIR}/soapServerLib.cpp
 
SOAP_CP_OTHERS += $${SOAP_GEN_DIR}/$${GSOAP_NAME}.*.req.xml \
                  $${SOAP_GEN_DIR}/$${GSOAP_NAME}.*.res.xml \
                  $${SOAP_GEN_DIR}/ns.xsd \
                  $${SOAP_GEN_DIR}/$${GSOAP_NAME}.nsmap
 
INCLUDEPATH += $${SOAP_GEN_DIR}
contains(CONFIG,soap_server) {
    TARGET = $${GSOAP_NAME}
    HEADERS += $${SOAP_M_HEADERS}
    SOURCES += $${SOAP_M_SOURCES}
    QMAKE_CLEAN += $${SOAP_GEN_DIR}/$${GSOAP_NAME}.wsdl \
               $${SOAP_M_HEADERS} \
               $${SOAP_M_SOURCES} \
               $${SOAP_C_HEADERS} \
               $${SOAP_C_SOURCES} \
               $${SOAP_CP_OTHERS} \
               $${SOAP_L_SOURCES}
} else {
    TARGET = $${GSOAP_NAME}_client
    HEADERS += $${SOAP_C_HEADERS}
    SOURCES += $${SOAP_C_SOURCES}
}
 
HEADERS += $${PWD}/nsmap/$${GSOAP_NAME}.h
```
leaning.pro
```c
TEMPLATE = subdirs
CONFIG += ordered
SUBDIRS += add \
           add_client \
           calc \
           calc_client
```
add.pro
```c
GSOAP_NAME = add
TEMPLATE = app
CONFIG += console soap_server
 
include(../leaning.pri)
 
HEADERS +=
 
SOURCES += \
    main.cpp
```
add_client.pro
```c
GSOAP_NAME = add
TEMPLATE = app
CONFIG += console
 
include(../leaning.pri)
 
HEADERS +=
 
SOURCES += \
    main.cpp
 ```

## 4. 编译后的项目目录结构
>nsmap下的接口文件为手动编辑所得（c的接口定义，通过它生成gsoap项目所需的源码文件）。  
temp目录为编译中间产物，由编译时自动产生。
```bash
gsoap2
│  gsoap.pri
│  gsoap28.pro
│  gsoap28.pro.user
│  mmsys.env
│
├─bin
│      add.exe
│      add_client.exe
│      calc.exe
│      calc_client.exe
│      soapcpp2.exe
│      wsdl2h.exe
│
├─gsoap
│      .dirstamp
│      dom.c
│      dom.cpp
│      stdsoap2.c
│      stdsoap2.cpp
│      stdsoap2.h
│      typemap.dat
│
└─leaning
    │  leaning.pri
    │  leaning.pro
    │
    ├─add
    │      add.pro
    │      main.cpp
    │
    ├─add_client
    │      add_client.pro
    │      main.cpp
    │
    ├─calc
    │      calc.pro
    │      main.cpp
    │
    ├─calc_client
    │      calc_client.pro
    │      main.cpp
    │
    ├─nsmap
    │      add.h
    │      calc.h
    │
    └─temp
        ├─add
        │      add.add.req.xml
        │      add.add.res.xml
        │      add.nsmap
        │      add.wsdl
        │      ns.xsd
        │      soapC.cpp
        │      soapClient.cpp
        │      soapClientLib.cpp
        │      soapH.h
        │      soapServer.cpp
        │      soapServerLib.cpp
        │      soapStub.h
        │
        └─calc
                calc.add.req.xml
                calc.add.res.xml
                calc.div.req.xml
                calc.div.res.xml
                calc.mul.req.xml
                calc.mul.res.xml
                calc.nsmap
                calc.pow.req.xml
                calc.pow.res.xml
                calc.sub.req.xml
                calc.sub.res.xml
                calc.wsdl
                ns.xsd
                soapC.cpp
                soapClient.cpp
                soapClientLib.cpp
                soapH.h
                soapServer.cpp
                soapServerLib.cpp
                soapStub.h9
```
