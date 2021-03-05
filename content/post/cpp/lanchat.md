---
title: "句聊 Lanchat 1.5.0"
date: 2019-01-10T23:20:53+08:00
draft: false
tags: [lanchat]
categories: [Qt]
---
## Greetings to [lanmessenger](https://lanmessenger.github.io)
### 下载:
>[lanchat-1.5.0-win64](https://github.com/nonwill/nwDeployed) 

### 在Lan Messenger的基础上：
1. 重构了其连接管理、消息处理和分发部分的实现。
2. TCP监听端口可改(UDP端口相同的用户相互可见)。
3. 改用QJson组织消息。
4. 内存管理做了增强，减少了程序运行时占用的内存。
5. 复用其UI并做了改进及问题修复。

### 下一步：
1. 可用性及稳定性改进，UI重构与改进

### 远期：
1. 支持离线用户管理
2. 增加插件支持扩展