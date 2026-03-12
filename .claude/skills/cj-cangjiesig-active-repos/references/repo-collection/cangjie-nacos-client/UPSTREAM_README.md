<div align="center">
<h1>Cangjie-nacos-client</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.0.1-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.3-brightgreen" style="display: inline-block;" />
<!-- <img alt="" src="https://img.shields.io/badge/cjcov-0.0%25-brightgreen" style="display: inline-block;" /> -->
<img alt="" src="https://img.shields.io/badge/state-孵化-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-Cloud-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/points- ？/100-brightgreen" style="display: inline-block;" />
</p>


## 介绍

本项目是使用Cangjie实现的一个轻量级的nacos客户端，目前支持以http请求的方式注册、注销服务，获取服务实例等。

### 项目特性

- 目前仅支持v2.x版本的nacos服务

- 支持使用http请求的方式注册服务实例、注销服务实例、获取全部/健康/单个服务实例

- 获取单个服务实例时可以选择轮询或带权重随机

### 项目计划

* 2025.11.8 完成使用http请求方式注册、注销服务等

* 2026.1.10前 完成配置管理、服务订阅

* 2026.2前 完成grpc的适配和v3.x版本的适配

## 项目架构

+ `doc`文档目录，用于存放接口文档

+ `src`源码目录

+ `src/test`测试文件目录

### 源码目录

```shell
.
├── doc                         # 文档目录，包括API接口文档
│   └── feature_api.md 
├── src 
│    ├── test                   # 测试代码目录
│    └── v2                     # 适配nacosv2.x版本的api
│         ├── balancer.cj   
│         ├── constance.cj
│         ├── error_code.cj
│         ├── nacos_client_properties.cj
│         ├── nacos_client_proxy_delegate.cj
│         ├── nacos_client_proxy.cj
│         ├── nacos_exception.cj
│         ├── nacos_grpc_client.cj
│         ├── nacos_http_client.cj
│         ├── naming_utils.cj
│         ├── result.cj
│         ├── service_info.cj
│         ├── service_instance.cj
│         └── utils.cj
├── CHANGELOG.md
├── cjpm.toml
├── LICENSE
└── README.md                   # 项目整体介绍
```

* 由于本项目依赖外部nacos服务，且服务启动顺序和端口占用带有随机性，故没有进行非常详尽的函数单元测试，但进行了充分的本地功能测试。

### 接口说明

主要类和函数接口说明，详见 [API](./doc/feature_api.md)

## 使用说明

### 依赖引入

1. 在系统环境变量中添加`CANGJIE_STDX_PATH`，指向`windows_x86_64_llvm`或`linux_x86_64_llvm`或`linux_aarch64_llvm`的上一级目录。

2. 在`cjpm.toml`中添加如下依赖

```shell
[dependencies]
    cangjie_nacos_client = { git = "https://gitcode.com/jjjyc/cangjie-nacos-client.git" }
```

### 编译构建


编译（win/linux）
```shell
cjpm update
cjpm build
```

### 功能示例
#### 服务注册/注销服务实例功能示例

* 服务注册

```cangjie

import cangjie_nacos_client.v2.*

main(): Int64 {

    let nacosServerPort: UInt16 = 8848
    let myServerPort: UInt16 = 8888

    let nacosClient = NacosClient(NacosClientProperties("public", "127.0.0.1", nacosServerPort))
    // 使用服务名、ip、端口号注册
    nacosClient.registerInstance("Cangjie-server", "127.0.0.1", myServerPort)

    // 使用服务名、服务实例注册
    let instance = ServiceInstance(serviceName: "Cangjie-server", ip: "127.0.0.1", port: 8887, weight: 5.0)
    nacosClient.registerInstance("Cangjie-server", instance)

    return 0
}
```

执行结果如下：

```shell
success
success
```

* 服务注销
```cangjie
import cangjie_nacos_client.v2.*

main(): Int64 {

    let nacosServerPort: UInt16 = 8848
    let myServerPort: UInt16 = 8888

    let nacosClient = NacosClient(NacosClientProperties("public", "127.0.0.1", nacosServerPort))
    // 使用服务名、ip、端口号注销
    nacosClient.deregisterInstance("Cangjie-server", "127.0.0.1", myServerPort)

    // 使用服务名、服务实例注销
    let instance = ServiceInstance(serviceName: "Cangjie-server", ip: "127.0.0.1", port: 8887, weight: 5.0)
    nacosClient.deregisterInstance("Cangjie-server", instance)

    return 0
}
```

执行结果如下：

```shell
success
success
```

#### 获取全部服务实例功能示例
> nacos服务器中注册了三个"Cangjie-server"的服务实例，分别占用8888，8887，8886端口

```cangjie
import cangjie_nacos_client.v2.*

main(): Int64 {
    let nacosClient = NacosClient(NacosClientProperties("public", "127.0.0.1", 8848))
    let instances = nacosClient.getAllInstances("Cangjie-server")

    println(instances.size)
    instances |> forEach {p => println(p.port)}

    return 0
}
```

执行结果如下：

```shell
3
8888
8887
8886
```

#### 获取健康/非健康服务实例功能示例

* nacos服务器中有三个"Cangjie-server"的健康服务实例，分别占用8888，8887，8886端口

```cangjie
import cangjie_nacos_client.v2.*

main(): Int64 {
    let nacosClient = NacosClient(NacosClientProperties("public", "127.0.0.1", 8848))
    let instances = nacosClient.selectInstances("Cangjie-server", true)
    
    println(instances.size)
    instances |> forEach {p => println(p.port)}

    return 0
}
```

执行结果如下：

```shell
3
8887
8888
8886
```

* nacos服务器中有两个"Cangjie-server"的健康服务实例，分别占用8888，8887端口；一个不健康实例，占用8886端口

```cangjie
import cangjie_nacos_client.v2.*

main(): Int64 {
    let nacosClient = NacosClient(NacosClientProperties("public", "127.0.0.1", 8848))
    var instances = nacosClient.selectInstances("Cangjie-server", true)
    println("healthy: ${instances.size}")
    instances |> forEach {p => println(p.port)}

    instances = nacosClient.selectInstances("Cangjie-server", false)
    println("unhealthy: ${instances.size}")
    instances |> forEach {p => println(p.port)}

    return 0
}
```

执行结果如下：

```shell
healthy: 2
8887
8888
unhealthy: 1
8886
```

#### 获取单个健康实例功能示例
> nacos服务器中注册了三个"Cangjie-server"的服务实例，分别占用8888，8887，8886端口，同时8888和8887端口的实例为1.0权重，8886端口为5.0权重

* 按权重随机

```cangjie
import cangjie_nacos_client.v2.*

main(): Int64 {
    for(_ in 0..10){
        let instance = nacosClient.selectOneHealthyInstance("Cangjie-server")
        instance.port |> println
    }

    return 0
}
```

执行结果如下：

```shell
8887
8888                                                                                                               
8886                                                                                                                
8886                                                                                                                
8886                                                                                                                
8887    
8887     
8886   
8886 
```

* 轮询
```
import cangjie_nacos_client.v2.*

main(): Int64 {
    for(_ in 0..9){
        let instance = nacosClient.selectOneHealthyInstance("Cangjie-server", polled: true)
        instance.port |> println
    }

    return 0
}
```

执行结果如下：

```shell
8888         
8886       
8887     
8888    
8886    
8887    
8888    
8886          
8887 
```

## 约束与限制

在下述版本验证通过：

    Cangjie Version: 1.0.0, 1.0.3

## 开源协议

本项目基于 [Apache License 2.0](./LICENSE) ，请自由的享受和参与开源。


## 参与贡献

欢迎给我们提交PR，欢迎给我们提交Issue，欢迎参与任何形式的贡献。