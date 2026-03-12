<div align="center">
<h1>Ginger</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.3-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjcov-100.0%25-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/state-孵化-brightgreen" style="display: inline-block;" />
</p>

## 介绍

Ginger是一个轻量级的http客户端，支持多种请求配置，及使用函数方式注册拦截器链。

### 项目特性

- 支持get, post, put, delete, options类型的请求

- 支持手动添加请求配置，添加拦截器

- 支持使用`next()`函数自定义处理拦截器链中下一个拦截器的执行位置

## 项目架构

+ `doc` 文档目录，用于存放接口文档和覆盖率报告

+ `src` 源码目录

+ `src/default` 提供了一些方便用户调用的函数

+ `src/test` 测试文件目录

### 源码目录

```shell
.
├── doc                         # 文档目录，包括API接口文档
│   └── feature_api.md 
├── src 
│    ├── test                   # 测试代码目录
│    ├── default                
│    │    └── import.cj    
│    ├── ginger.cj             
│    ├── ginger_config.cj 
│    ├── ginger_response.cj
│    ├── ginger_context.cj
│    ├── request_body.cj
│    ├── readable_response.cj
│    ├── message.cj
│    └── util.cj
├── CHANGELOG.md
├── cjpm.toml
├── LICENSE
└── README.md                   # 项目整体介绍
```
* 本项目单元测试测试覆盖率100%，点击[查看测试覆盖率](./doc/coverage.md)

* 或执行`cjcov -o output -e "./src/test" --html-detail`查看

### 接口说明

主要类和函数接口说明，详见 [API](./doc/feature_api.md)

## 使用说明
### 依赖引入

1. 在系统环境变量中添加`CANGJIE_STDX_PATH`，指向`windows_x86_64_llvm`或`linux_x86_64_llvm`或`linux_aarch64_llvm`的上一级目录。

2. 在`cjpm.toml`中添加如下依赖

```shell
[dependencies]
  ginger = { git = "https://gitcode.com/Cangjie-SIG/ginger.git" }
```

### 编译构建


编译（win/linux）
```shell
cjpm update
cjpm build
```

### 功能示例
#### 基本发送请求功能示例

+ get请求 (服务器返回 "Server: Get Hello Cangjie!" )


```cangjie
import ginger.*

main(): Int64 {
    let ginger = Ginger()
    let response = ginger.get("http://localhost:8080/cangjie/get") 
    ginger.close()
    response.readString() |> println
    return 0
}
```

执行结果如下：

```shell
Server: Get Hello Cangjie!
```

+ post请求 (服务器返回请求体中的User的String)


```cangjie
import ginger.*

main(): Int64 {
    let ginger = Ginger()
    let user = User("zhangsan", 18) // User实现了Serializable接口
    let response = ginger.post("http://localhost:8080/cangjie/post", body:RequestBody.of(user)) 
    let newUser = response.readAs<User>()
    ginger.close()
    println(newUser.id)
    println(newUser.name)
}
```

执行结果如下：

```shell
18
zhangsan
```

+ 在创建Ginger时添加配置 (服务器返回 "Server: Get Hello Cangjie!" )


```cangjie
import ginger.*

main(): Int64 {
    let ginger = Ginger(config: RequestConfig(baseUrl: "http://localhost:8080"))
    let response = ginger.get("/cangjie/get")
    ginger.close()
    response.readString() |> println
    return 0
}
```

执行结果如下：

```shell
Server: Get Hello Cangjie!
```

#### 快捷发送请求功能示例

+ get请求 (服务器返回 "Server: Get Hello Cangjie!" )



```cangjie
import ginger.*
import ginger.default.*

main(): Int64 {
    let response = get("http://localhost:8080/cangjie/get") 
    response.readString() |> println
    return 0
}
```

执行结果如下：

```shell
Server: Get Hello Cangjie!
```
+ post请求 (服务器返回请求体中的User的String)


```cangjie
import ginger.*

main(): Int64 {
    let user = User("zhangsan", 18) // User实现了Serializable接口
    let response = post("http://localhost:8080/cangjie/post", body:RequestBody.of(user)) 
    let newUser = response.readAs<User>()
    println(newUser.id)
    println(newUser.name)
    return 0
}
```

执行结果如下：

```shell
18
zhangsan
```

#### 拦截器功能示例

+ 添加请求拦截器 (服务器返回全部请求头信息)



```cangjie
import ginger.*

main(): Int64 {
    let ginger = Ginger()
    ginger.addInterceptors{
        c => 
        c.config = c.config.setHeader("customHeader", ["customValue"])
        c.next()
    }

    let response = ginger.get("http://localhost:8080/cangjie/getHeader")
    ginger.close()
    response.readString() |> println
    return 0
}
```

执行结果如下：

```shell
host: localhost:8080
customheader: customValue
accept: application/json,text/plain,*/*
user-agent: CANGJIEUSERAGENT_1_1
connection: keep-alive
content-length: 0
```

+ 添加响应拦截器 (如果响应码是404则做处理)


```cangjie
import ginger.*
import stdx.net.http.*

main(): Int64 {
    let ginger = Ginger()
    ginger.addInterceptors{
        c =>
        c.next()
        if(c.response.status == 404){
            c.response = HttpResponseBuilder().body("Path Error, please check it!").build()
        }
    }

    let response = ginger.get("http://localhost:8080/cangjie/none")
    ginger.close()
    response.readString() |> println
    return 0
}
```

执行结果如下：

```shell
Path Error, please check it!
```

+ 中断请求，返回自定义响应


```cangjie
import ginger.*
import stdx.net.http.*

main(): Int64 {
    let ginger = Ginger()
    ginger.addInterceptors{
        c => c.response = HttpResponseBuilder().status(250).body("Custom response").build()
    }

    let response = ginger.get("http://localhost:8080/cangjie/mock")
    ginger.close()
    println(response)
    println(response.readString())
    return 0
}
```

执行结果如下：

```shell
HTTP/1.1 250 

body size: 15

Custom response
```


## 约束与限制

在下述版本验证通过：

    Cangjie Version: 1.0.0

## 开源协议

本项目基于 [Apache License 2.0](./LICENSE) ，请自由的享受和参与开源。

## 参与贡献

本项目由 [SIGCANGJIE / 仓颉兴趣组](https://gitcode.com/SIGCANGJIE) 实现并维护。技术支持和意见反馈请提Issue。

欢迎给我们提交PR，欢迎参与任何形式的贡献。

本项目committer：[@Chemxy](https://gitcode.com/Chemxy)

This project is supervised by [@zhangyin_gitcode](https://gitcode.com/zhangyin_gitcode) (HUAWEI Developer Advocate).

![](https://raw.gitcode.com/SIGCANGJIE/homepage/attachment/uploads/9b648c07-efc2-4eb3-b02f-eab18c77beea/devadvocate.png)