<div align="center">
<h1>Cangjie CEF</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.0.1-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.3-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjcov-0.0%25-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/state-孵化/毕业-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-HOS/Cloud-brightgreen" style="display: inline-block;" />
</p>

- 示例
![运行界面](./doc/img/test.gif)
![运行界面](./doc/img/math_life.gif)    
    

- [1. 项目历程](#1-项目历程)
- [2. 介绍](#2-介绍)
  - [2.1 项目特性](#21-项目特性)
  - [2.2 项目扩展说明](#22-项目扩展说明)
  - [2.3 项目计划](#23-项目计划)
- [3. 项目架构](#3-项目架构)
  - [3.1 源码目录](#31-源码目录)
  - [3.2 接口说明](#32-接口说明)
- [4. 使用说明](#4-使用说明)
  - [4.1 编译构建](#41-编译构建)
    - [4.1.1 编译运行](#411-编译运行)
    - [4.1.2 libcef.dll下载](#412-libcefdll下载)
    - [4.1.3 编译运行说明](#413-编译运行说明)
  - [4.2 示例代码](#42-示例代码)
  - [4.3 进程间通信说明](#43-进程间通信说明)
    - [4.3.1 js 调用仓颉](#431-js-调用仓颉)
    - [4.3.1 仓颉调用js](#431-仓颉调用js)
  - [4.4 无边框支持](#44-无边框支持)
  - [4.5 文件流传(数据流）传输](#45-文件流传数据流传输)
- [约束与限制](#约束与限制)
- [开源协议](#开源协议)
- [参与贡献](#参与贡献)



## 1. 项目历程
- 2025/7/5  切换仓颉版本为1.0.0， 更新进程间通信功能
- 2025/7/10 补充窗口管理函数， 修复gpu报错堆异常应用闪退问题
- 2025/7/13 切换cef版本为 cef_binary_138.0.21+g54811fe+chromium-138.0.7204.101_windows64， 补充完善部分窗口及浏览器视图管理功能
- 2025/7/14 添加无边框窗口和自定义标题栏支持
- 2025/7/16 添加ipc数据流传输，修改ipc接口参数默认值， 回调接口数据Option包装（参考：test/src/main.js）
- 2025/7/17 添加gpu支持，新增启动脚本
- 2025/7/18 优化执行脚本，一键编译打包执行
- 2025/7/19 优化项目配置，自定义实现mt.exe
- 2025/7/21 添加cjpm 构建脚本， 实现cjpm run 一键启动， 优化构建流程
- 2025/7/29 优化进程间通信，支持多参数传递，支持宏简化操作
- 2025/11/9 仓颉切换1.0.3， cef切换到141，解决闪退问题



## 2. 介绍

Cangjie CEF 是 CEF(Chromium Embedded Framework) C API 在仓颉端的封装和拓展，可作为仓颉跨平台桌面端开发框架

### 2.1 项目特性

- 补充仓颉的桌面混合开发框架
- 实现仓颉嵌入和调用浏览器的能力
- CEF端使用原生C API 实现，可和仓颉直接对接调用，性能更高效
- 基于web和仓颉的桌面混合开发框架
- 仓颉跨平台桌面开发框架
- 基于仓颉Lambda 和 宏等特性，开发更简单


### 2.2 项目扩展说明
- 在c端封装部分功能做默认配置，减少仓颉端封装的复杂度，提高执行效率。此接口是在CEF C API的基础上进行的c接口封装，见libcef_c_wrapper.dll 
- 保留CEF C API和仓颉的映射接口， 相关接口映射基本已经封装完全，详见src/ffi 目录下, 实现CEF大部分原有接口和结构，可直接在仓颉端扩展和实现CEF相关功能

### 2.3 项目计划
- 阶段一：基础框架封装实现（完善补充中）
  - 已经实现功能：
    - 窗口管理(窗口创建、窗口大小、窗口位置、标题、图标设置、子视图插入、弹窗管理等)
    - 窗口最大、最小、关闭、全屏、隐藏、显示控制接口
    - 本地HTML、js、css等加载渲染
    - URL加载渲染
- 阶段二： js进程间通信 （补充完善中）
   - js和调用仓颉并返回 (已实现)
   - 仓颉调用js并返回 (已实现)
   - 文件传输 (已实现)
 - 阶段三： 无边框窗口支持 （已实现）
 - 阶段四： GPU支持
    - 已支持
- 阶段五： 跨平台支持
    - Windows (已实现)
    - Linux   (开发中)
    - MacOS   (开发中)
## 3. 项目架构
目前架构分两层：仓颉端封装和cef端动态库

### 3.1 源码目录

```shell
.
├── README.md             #整体介绍
├── cef_cangjie_c_wrapper #cef capi的封装源码，用于仓颉调用, 使用时可删除   
├── cjbind_tmp            #c结构翻译工具，来自cjbind 库  
├── doc                   #文档目录，包括设计文档，API接口文档等
│   ├── design.md         #设计文档
│   └── feature_api.md    #特性接口文档
├── lib                   #依赖库，包括cef动态库，cjc动态库等
|   ├── cef               #cef动态库目录
├── src                   #源码目录
|   ├── core              #功能封装
|   ├── ffi               #cjc和cef的映射接口
|   ├── config            #相关配置
|   ├── ipc               #进程间通信相关
|   ├── define            # 宏定义
│   └── cef.cj            #包说明
├── resources             #测试资源文件目录，包括图标、图片、静态文件等等， 测试时可将其下的 html和icon复制到编译后可执行程序同级目录，测试html加载和icon设置
|—— pack_run.bar          # 打包执行脚本文件
└── test                  #测试代码目录
    ├── src
    |    ├── main.cj       # 使用示例
    └── 
```

### 3.2 接口说明

主要类和函数接口说明，详见 [API](./doc/feature_api.md)


## 4. 使用说明
### 4.1 编译构建
- <span style="color: red; font-weight: bold;">注： 项目依赖仓颉 stdx库， 请先安装。
    - 安装参考：[https://gitcode.com/Cangjie/cangjie_stdx](https://gitcode.com/Cangjie/cangjie_stdx) 
    - 下载地址：[https://gitcode.com/Cangjie/cangjie_stdx/releases/v1.0.3.1](https://gitcode.com/Cangjie/cangjie_stdx/releases/v1.0.3.1)
    </span>

安装完成后修改test/cjpm.toml 中stdx 配置路径
- ![运行界面](./doc/img/stdx.png) 
  
#### 4.1.1 编译运行
```shell
    cd test
    cjpm run
```

- 描述具体的编译过程：
    - 下载libcef.dll, 放入lib/cef目录下， 下载参考 4.1.2 方式
    - 将所需的资源文件（img, css, js, html等），放在resources目录下，按对应路径（js, html，css中引入的相对路径）
    - 修改构建脚本， 以test/build.cj为例， 检查几个所需变量是否符合，要是项目结构没有变化修改就无需改
       - ![运行界面](./doc/img/build2.png) 
    - 然后执行cjpm run 运行即可

#### 4.1.2 libcef.dll下载
- libcef.dll 存放到新建的发行版目录下，此版本为方便于libcef.dll 下载， 代码非最新。
- 注意： 仓库最新代码基于cef141， 请下载141版本
- 链接： 
[https://gitcode.com/Cangjie-SIG/cj-cef/releases/0.1](https://gitcode.com/Cangjie-SIG/cj-cef/releases/0.1)
![](./doc/img/libcefdll.png)

#### 4.1.3 编译运行说明
    在test中使用了cjpm build构建脚本，见test/build.cj, 会自动拷贝lib/cef和resources下的内容到编译后可执行程序目录。并且会为可执行程序注册windows清单文件，保证gpu调用的正确性。

### 4.2 示例代码

```cangjie
package cef_test

import stdx.log.*
import stdx.logger.*
import std.env.*
import std.console.Console
import std.sync.*
import std.collection.*
import std.time.MonoTime
import cef.core.*
import cef.core.App
import cef.config.*
import cef.ipc.*
import cef.define.*

let logger = getGlobalLogger(("name", "main"))
let tl = SimpleLogger(Console.stdOut)

main(args: Array<String>): Int32 {
    tl.level = LogLevel.TRACE
    setGlobalLogger(tl)

    let hash = App.hashApi()
    if (hash) {
        logger.error("App hash: false");
        return -1;
    }

    let config = AppConfig()
        .browserConfig {
            config =>
            // config.setURL("http://www.baidu.com")
            config.setHTML("html/index.html")
        }
        .windowConfig {
            config => config
                .setWidth(800)
                .setHeight(600)
                .setIcon("icon/icon1.png")
                .setTitle("CangjieCEF")
                .setPopupWindowHeight(600)
                .setPopupWindowWidth(800)
                .setPopupWindowIcon("icon/icon1.png")
                .setPopupWindowTitle("CangjieCEFPoupWindow")
        }

    App.initialize(config)

    let browser_view = BrowserView(config)
    let window = Window(config, browser_view)

    // 注册js调用函数
    @IpcMainOn
    let example_event = {
        param: String =>
        println("example_event: ${param}")

        // 调用js
        @IpcMainSend[browser_view, 100: Int32, "test12345": String, false: Bool]
        let call_js4 = {
            parm1: Bool, parm2: Int32, parm3: String =>
            println("call_js4 param1: ${parm1}")
            println("call_js4 param2: ${parm2}")
            println("call_js4 param3: ${parm3}")
        }

        return "hello world cangjie"
    }

    // 注册js调用函数
    @IpcMainOn
    let send_test_list = {
        param1: Bool, param2: Int32, param3: Float64, param4: String =>
        println("send_test_list param1: ${param1}")
        println("send_test_list param2: ${param2}")
        println("send_test_list param3: ${param3}")
        println("send_test_list param4: ${param4}")
        return "hello world cangjie"
    }

    App.launch()

    return 0
}

```

执行结果如下：
- 本地html加载
![运行界面](./doc/img/html1.png)

- 网络URL加载
![运行界面](./doc/img/url1.png)

### 4.3 进程间通信说明
  通过进程间通信，实现js和仓颉的通信，数据通过特定结构封装，暂时支持单参数， 参数类型支持Bool, Float64, Int32, String
  #### 4.3.1 js 调用仓颉
    js 通过封装的v8 全局函数来调用仓颉端注册的函数，调用和注册的函数名称一致
    ```javascript
        ipcRenderer.send('send_test_list', [true, 100, 99.99, 'tests'], (response) => {
            console.log("rsponse: ")
            console.log(response)
        })
    ```
    仓颉端需要注册调用函数
    ```Cangjie
    // 注册js调用函数
    @IpcMainOn
    let send_test_list = {
        param1: Bool, param2: Int32, param3: Float64, param4: String =>
        println("send_test_list param1: ${param1}")
        println("send_test_list param2: ${param2}")
        println("send_test_list param3: ${param3}")
        println("send_test_list param4: ${param4}")
        return "hello world cangjie"
    }
    ```

#### 4.3.1 仓颉调用js
    - js 注册函数
    ```js
        ipcRenderer.on('call_js4', (arg1, arg2, arg3) => {
            console.log("cangjie call ......param:")
            console.log("arg1:", arg1)
            console.log("arg2:", arg2)
            console.log("arg2:", arg3)
            return [true, 100, 'test_list']
        })
    ```

    - 仓颉调用函数
    ```Cangjie
        // 调用js
        @IpcMainSend[browser_view, 100: Int32, "test12345": String, false: Bool]
        let call_js4 = {
            parm1: Bool, parm2: Int32, parm3: String =>
            println("call_js4 param1: ${parm1}")
            println("call_js4 param2: ${parm2}")
            println("call_js4 param3: ${parm3}")
        }
    ```

更多进程间通信示例请参考： [进程间通信](./doc/进程间通信.md)

### 4.4 无边框支持

![运行界面](./doc/img/noboder.png)
- 无边框支持开启：
    - .set_is_frameless(true)
- 拖拽支持：
  - css 添加属性： -webkit-app-region: drag; 
- 示例参考： test/src/main_drag.cj
  
### 4.5 文件流传(数据流）传输
- 示例参考： test/src/main_file_stream.cj


注： 测试和使用示例参考test

## 约束与限制
- 开发环境：windows11
- CEF版本： cef_binary_141.0.11+g7e73ac4+chromium-141.0.7390.123_windows64
- 仓颉版本：widows native版，1.0.3

## 开源协议
License

## 参与贡献

欢迎给我们提交PR，欢迎给我们提交Issue，欢迎参与任何形式的贡献。