---
title: "回收VMWare虚拟机占用的磁盘空间"
date: 2012-11-05T18:12:27+08:00
draft: false
tags: [linux]
categories: [VMWare]
---
## 1. 开虚拟机，root，每个分区下：
```bash
cat /dev/zero > zero.fill;sync;sleep 1;sync;rm -f zero.fill
```
## 2. 宿主机执行命令：
```bash
vmware-vdiskmanager.exe -k *.vmdk
```
## 3. 以下这些情况是无法使用shrink功能的:
>★使用默认方式新建的GSX Server虚拟机。  
★使用了快照功能的虚拟机。  
★使用了物理磁盘为虚拟机磁盘。  
★虚拟磁盘保存在CD-ROM或DVD-ROM上。  
★你不能收缩预分配的磁盘。  
在进行收缩之前，需要删除创建的快照，之后，直接登录虚拟，打开VmwareTools就可能收缩磁盘了。

## /dev/null and /dev/zero:
>/dev/null，外号叫无底洞，你可以向它输出任何数据，它通吃，并且不会撑着！  
/dev/zero，是一个输入设备，你可你用它来初始化文件。