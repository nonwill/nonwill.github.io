---
title: "VMWare中Manjaro永久修改分辨率"
date: 2020-12-29T18:12:27+08:00
draft: false
tags: [linux]
categories: [VMWare,分辨率]
---
## 1. 打开或创建xorg.conf：
```bash
sudo nano /etc/X11/xorg.conf
```
## 2. 在文件中添加如下部分：
```c++
Section "Monitor"
Identifier "Configured Monitor"
Modeline "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
Option "PreferredMode" "1920x1080_60.00"
EndSection
Section "Screen"
Identifier "Default Screen"
Monitor "Configured Monitor"
Device "Configured Video Device"
EndSection
Section "Device"
Identifier "Configured Video Device"
EndSection
```
## 3. 保存文件并重启系统