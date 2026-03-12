<div align="center">
<h1>InterCeptor</h1>
</div>
<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.1.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/state-孵化-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-HOS/Cloud-brightgreen" style="display: inline-block;" />
</p>

## 1 介绍

本项目基于跨平台的底层库 uiohook 进行封装，为开发者提供了一个简单、安全且高性能的事件拦截接口。

### 项目特性


### 1.1 项目特性

* ⚙️ **全局输入事件捕获**：支持系统级键盘、鼠标事件监听。
* ⌨️ **键盘事件系统**：支持 `keyPressed`、`keyReleased`、`keyTyped` 三种事件，区分物理键与字符输入。
* 🖱️ **鼠标事件系统**：支持按键点击、滚轮滚动、指针移动等事件类型。
* 🧠 **原生扫描码与虚拟键码映射**：提供多层键盘映射机制，支持自定义布局和输入法兼容。
* 🔄 **事件回调模型**：采用注册式回调函数设计，方便嵌入自定义处理逻辑。
* 🔒 **线程安全与异步事件分发**：内部事件队列异步分发，支持在多线程程序中安全使用。
* 🧰 **修饰键状态追踪**：支持 Ctrl、Shift、Alt、Meta 等组合键状态管理。
* 🪶 **轻量级依赖**：适合嵌入其他项目或封装为动态库。
* 🧭 **高精度时间戳**：所有事件均带有时间戳，可用于事件序列回放或延迟测量。


### 1.2 项目计划

1. [x] 全局键盘事件捕获：实现 `keyPressed`、`keyReleased`、`keyTyped` 的事件回调与封装
2. [ ] 全局鼠标事件捕获：支持移动、点击、滚轮滚动等事件监听
3. [ ] 事件调度与分发模块（EventDispatcher）：实现统一的事件路由与线程安全队列
4. [x] 修饰键状态管理：支持 Ctrl、Alt、Shift、Meta 等组合状态检测
5. [ ] 键码与字符映射表完善：实现虚拟键码与系统扫描码映射逻辑


## 2 源码目录

```shell
├── clib      # c语言底层模块
│   ├── example.c
│   ├── interceptor.c
│   ├── interceptor.h
│   ├── Makefile
│   └── uiohook.h
└─── src
    ├── event       #事件及其映射文件
    │   ├── ascii_control_keys.cj
    │   ├── kevent.cj
    │   ├── key_event.cj
    │   ├── key_names.cj
    │   ├── key.cj
    │   ├── keycode_asc.cj
    │   ├── keycode.cj
    │   └── maskcode.cj
    ├── msg         #消息模型目录
    │   ├── cmd_msg_handler.cj
    │   ├── event_msg.cj
    │   ├── model_msg_handler.cj
    │   ├── msg_channel.cj
    │   ├── msg_dispatcher.cj
    │   ├── msg_handler.cj
    │   └── msg.cj
    └── test    #测试目录
       └── msg_sys_test.cj
      
```

## 3 使用说明

### 3.1 编译构建（Win/Linux/Mac）
在工程根目录下运行： 
```shell
cd clib 
make
cd ..
cjpm build
```

## 4 参与贡献
本项目由 Gloomysunny 实现并维护。技术支持和意见反馈请提Issue。