# gateway-cj：仓颉语言实现的微服务网关

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/build-pass-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjcov-NA-red" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/project-open-brightgreen" style="display: inline-block;" />
</p>

## <img alt="" src="./docs/images/readme-icon-introduction.png" style="display: inline-block;" width=3%/> 1 介绍

仓颉原生微服务网关。已适配仓颉1.0.0 LTS版本 <br>

# 快速开始

解压介质包，结构如下

```text
gateway
├── bin
│   ├── gateway
│   └── startup.sh
└── resources
    └── applicationContext.yaml
```

根据需求编辑 applicationContext.yaml 配置

## 一个精简的示例配置如下：

```yaml
gateway:
  routes:
    - id: CangjieDemo
      uri: http://example.org/
      predicates:
        - Path=/demo/**
```

执行 ./bin/startup.sh 启动服务

# 断言

路由断言是用来决定一个请求是否匹配某个路由的规则。不同的断言可以根据请求的不同属性进行匹配。多个路由断言可以通过逻辑“与（and）”的方式组合，从而定义更加复杂的匹配条件。

## After路由断言

After路由断言接收一个日期时间参数，用于匹配那些发生在指定日期时间之后的请求。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - After=2025-09-01T00:00:00+08:00[Asia/Shanghai]
```

支持的时间格式：

- yyyy-MM-dd，例：2025-09-01 
- yyyy-MM-ddTHH:mm:ss，例：2025-09-01T00:00:00 
- yyyy-MM-ddTHH:mm:ss.S，例：2025-09-01T00:00:00.000 
- yyyy-MM-ddTHH:mm:ssOOOO，例：2025-09-01T00:00:00+08:00 
- yyyy-MM-ddTHH:mm:ss.SOOOO，例：2025-09-01T00:00:00.000+08:00 
- yyyy-MM-ddTHH:mm:ssOOOOz，例：2025-09-01T00:00:00+08:00[Asia/Shanghai] 
- yyyy-MM-ddTHH:mm:ss.SOOOOz，例：2025-09-01T00:00:00.000+08:00[Asia/Shanghai] 

## Before路由断言

Before路由断言接收一个日期时间参数，用于匹配那些发生在指定日期时间之前的请求。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - Before=2035-09-01T00:00:00+08:00[Asia/Shanghai]
```

## Between路由断言

Between路由断言接收两个日期时间参数参数：datetime1和datetime2。该断言会匹配发生在datetime1与datetime2之间的请求，因此要求参数datetime2必须在datetime1之后。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - Between=2017-01-20T17:00:47.789-07:00[America/Denver], 2027-01-21T17:42:47.789-07:00[America/Denver]
```

## Cookie路由断言

Cookie路由断言接收两个参数：Cookie名称和一个正则表达式（regexp），用于匹配具有指定名称且其值符合正则的Cookie。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - Cookie=suger:ch.p
```

## Header路由断言

Header路由断言接收两个参数：请求头的名称（header）和一个正则表达式（regexp），用于匹配具有指定名称并且其值符合给定正则表达式的请求头。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - Header=X-Request-Id:\id+
```

## Host路由断言

Host路由断言接收一个参数：主机名模式（host name patterns）的列表。采用以“.”为分隔符的Ant风格路径匹配格式，匹配与指定模式相符的Host请求头。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - Host=**.list.org, **.map.org
```

## Method路由断言

Method路由断言接收一个methods参数，这个参数是一个或多个HTTP方法名，用于匹配相应的请求方法。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - Method=GET
```

## Path路由断言

Path路由断言接收两个参数：一个Path模式列表，以及一个可选的标志位matchTrailingSlash（默认值为true）。Path路由断言用于匹配请求路径，如果将matchTrailingSlash设置为false，则将不再匹配以斜杠结尾的路径。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - Path=/green,/yellow/*
```

## Query路由断言

Query路由断言接收两个参数：一个必要的参数名（param）和一个可选的正则表达式（regexp），用于匹配包含查询参数并且其值符合正则的请求。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - Query=colors, blu.
```

## RemoteAddr路由断言

RemoteAddr路由断言接收一个来源地址列表（最小长度为 1），这些地址是以CIDR表示法（IPv4 或 IPv6）表示的字符串。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - RemoteAddr=192.168.2.0/24
```

## XForwarded RemoteAddr路由断言

XForwarded RemoteAddr路由断言接收一个请求来源列表（最小长度为1），列表中的元素采用CIDR表示法（IPv4 或 IPv6）的字符串形式。该路由断言允许根据名为X-Forwarded-For的HTTP请求头来过滤请求，可以与反向代理（如负载均衡器或 Web 应用防火墙）一起使用，以确保仅当请求来自这些反向代理所使用的受信任IP地址列表时才会被允许。

```yaml
gateway:
  routes:
  - id: test_route
    uri: http://example.org/
    predicates:
      - XForwardedRemoteAddr=192.168.2.1/24
```

# 过滤器

路由过滤器可以在请求转发的过程中对请求或者响应进行修改

## AddRequestHeader过滤器

AddRequestHeader 过滤器接受一个名称和值参数。可以将配置键值添加到请求的头中。键和值之间使用冒号分隔，多个键值对之间使用逗号分隔。

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - AddRequestHeader=key:value
```

## AddRequestHeadersIfNotPresent过滤器

AddRequestHeadersIfNotPresent与AddRequestHeader过滤器功能相似。不同之处在于，只有在请求头不存在的情况下才会添加。如果客户端请求中已经包含该请求头，则会直接发送客户端原有的值。

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - AddRequestHeadersIfNotPresent=key:value
```

## AddRequestParameter过滤器

AddRequestParameter过滤器可以向请求url中添加查询参数。

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - AddRequestParameter=key:value
```

## AddResponseHeader过滤器

AddResponseHeader过滤器可以在http响应头中添加参数。

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - AddResponseHeader=key:value
```

## AllowMethod过滤器

AllowMethod过滤器将只允许指定方法的http请求通过。如果不匹配则直接返回405状态码。

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - AllowMethod=GET
```

## SetRequestHeader过滤器

SetRequestHeader过滤器用于替换指定的http请求头。

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - SetRequestHeader=key:value
```

## SetResponseHeader过滤器

SetRequestHeader过滤器用于替换指定的http响应头。

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - SetResponseHeader=key:value
```

## SetStatus过滤器

SetStatus过滤器会装响应码替换为配置的值。

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - SetStatus=200
```

## StripPrefix过滤器

StripPrefix过滤器可以在请求向下游转发时，剥离部分路径

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - StripPrefix=2
```

## RequestRateLimiter过滤器

RequestRateLimiter过滤器可以在请求向下游转发时，根据配置要求进行限流

配置示例

```
gateway:
  routes:
    - id: case  
      uri: http://example.org/
      predicates:
        - Path=/case
      filters:
        - RequestRateLimiter=rate:10,capacity:20
```

rate参数表示允许的请求处理速率，用于控制每秒允许处理的请求数；

capacity参数表示令牌桶的容量，控制允许处理的突发请求上限。

# nacos

您可以新增gateway.nacos配置项（非必填）来对接nacos服务

gateway.nacos.discovery （非必填）用于配置服务自动发现功能，它可以用来对接 lb://service 跳转，并已实现了轮询机制的负载局均衡

gateway.nacos.config （非必填）用于配置同步nacos上的配置，它会将nacos上的配置与本地配制进行合并，当配置项两边都有时，以本地配置优先。

## 配置示例如下

```yaml
gateway:
  nacos:
    #服务注册与发现
    discovery:
      application-name: nacos-server
      server-addr: http://127.0.0.1:8848
      group: DEFAULT_GROUP #默认分组
      instance-url-path: /nacos/v1/ns/instance/list
      service-url-path: /nacos/v1/ns/service/list
      username: nacos
      password: nacos
      namespace: public
    config:
      server-addr: http://127.0.0.1:8848
      service-name: Cangjie-service
      group: DEFAULT_GROUP #默认分组
      url-path: /nacos/v1/cs/configs
      username: nacos
      password: nacos
      namespace: public
```

# apollo

您可以新增gateway.apollo配置项（非必填）来对接apollo服务

它会将apollo上的配置与本地配制进行合并，当配置项两边都有时，以本地配置优先。

支持token和accesskey两种方式获取apollo上的配置，两种方式不可同时配置，请使用时注意区分：

利用token访问拉取配置时，server-addr的端口使用服务配置端口（一般是8070）；利用accesskey访问拉取配置时，server-addr的端口使用管理端端口（一般是8080）。

## 配置示例如下

```yaml
gateway:
  apollo:
    token: token
    server-addr: http://127.0.0.1:8070
    env: LOCAL
    appid: appid
    cluster: default
    namespace: config.yaml
```

或

```yaml
gateway:
  apollo:
    access-key-secret: accesskey
    server-addr: http://127.0.0.1:8080
    env: LOCAL
    appid: appid
    cluster: default
    namespace: config.yaml
```

# 其它配置

## 配置项说明

- server.host 服务监听ip
- server.port 服务监听port
- server.output-console 是否将日志输出到控制台
- server.interval-ms 定时更新nacos、apollo配置项，单位毫秒
- server.tls 配置tls, 用于支持https功能
- server.tls.key-filepath 配置tls的key文件路径
- server.tls.crt-filepath 配置tls的crt文件路径
- global.response-timeout 转发http的响应超时时长，单位毫秒
- global.connect-timeout 转发http的请求超时时长，单位毫秒
- routes.tls 支持转发https请求
- routes.tls.trust-all 信任所有证书，这个为true时不需要配routes.tls.crt-filepath
- routes.tls.crt-filepath 配置信任证书文件位置

## 配置示例如下

```yaml
gateway:
  server:
    host: "0.0.0.0"
    port: 8080
    output-console: true
    interval-ms: 300000
    tls:
      key-filepath: ./tls/server.key
      crt-filepath: ./tls/server.crt
  globals:
    response-timeout: 60000
    connect-timeout: 60000
  routes:
    - id: TestHttps
      uri: https://127.0.0.1:443
      tls:
        trust-all: true
        crt-filepath: ./tls/server.crt
      predicates:
        - Path=/hello
      filters:
        - AllowMethod=GET, POST
```

# 完整的配置示例

```yaml
gateway:
  server:
    host: "0.0.0.0"
    port: 8080
    output-console: true
    interval-ms: 300000
    #tls:
    #  key-filepath: ./tls/server.key
    #  crt-filepath: ./tls/server.crt
  nacos:
    #服务注册与发现
    discovery:
      application-name: app
      server-addr: http://127.0.0.1:8848
      group: DEFAULT_GROUP #默认分组
      instance-url-path: /nacos/v1/ns/instance/list
      service-url-path: /nacos/v1/ns/service/list
      username: nacos
      password: nacos
      namespace: public
    config:
      server-addr: http://127.0.0.1:8848 # Nacos服务端地址
      service-name: Cangjie-service
      group: DEFAULT_GROUP #默认分组
      url-path: /nacos/v1/cs/configs
      username: nacos
      password: nacos
      namespace: public
  apollo:
    #方式1：通过token拉取
    # token: token
    # server-addr: http://127.0.0.1:8070
    #方式2：通过accesskey
    access-key-secret: "1cf998c4e2ad4704b45a98a509d15719" 
    server-addr: http://127.0.0.1:8080
    env: LOCAL
    appid: app
    cluster: default
    namespace: config.yaml
  globals:
    response-timeout: 60000
    connect-timeout: 60000
    filters:
      - AllowMethod=GET, POST
  routes:
    - id: RouteLineConf
      uri: http://example.org/
      predicates:
        - After=2025-09-01
        - Before=2025-11-01T08:00:00
        - Between=2025-01-20T17:42:47.789-07:00[America/Denver], 2026-01-21T17:42:47.789-07:00[America/Denver]
        - Cookie=chocolate, ch.p
        - Header=X-Request-Id:\id+
        - Host=**.list.org, **.map.org
        - Method=GET,POST
        - Path=/green,/yellow/*,false
        - Query=colors, blu.
        - RemoteAddr=192.168.1.0/24, 10.0.0.1/32, 2001:db8::/32, ::1/128
        - XForwardedRemoteAddr=192.168.1.1/24, 192.168.0.1/16
      filters:
        - AddRequestHeader=key:value
        - AddRequestHeadersIfNotPresent=key:value
        - AddRequestParameter=key:value
        - AddResponseHeader=key:value
        - AllowMethod=GET
        - SetRequestHeader=key:value
        - SetResponseHeader=key:value
        - SetStatus=200
        - StripPrefix=2
        - RequestRateLimiter=rate:10,capacity:20
    - id: RouteObjConf
      uri: http://example.org/
      predicates:
        - name: After
          args:
            datetime: 2025-10-01T08:00:00+08:00[Asia/Shanghai]
        - name: Before
          args:
            datetime: 2025-12-11T16:00:00+08:00[Asia/Shanghai]
        - name: Before
          args:
            datetime1: 2025-11-01T08:00:00+08:00[Asia/Shanghai]
            datetime2: 2025-12-11T16:00:00+08:00[Asia/Shanghai]
        - name: Cookie
          args:
            name: session
            regexp: a-zA-Z0-9 
        - name: Header
          args:
            header: X-Request-Id
            regexp: \d+
        - name: Host
          args:
            pattern: 
              - "**.map.org"
              - "**.list.org"
        - name: Method
          args:
            methods: GET 
        - name: Path
          args:
            patterns: /api/v1/**
            matchTrailingSlash: false  
        - name: Query
          args:
            param: colors
            regexp: red
        - name: RemoteAddr
          args:
            sources: 2001:db8::/32  
        - name: XForwardedRemoteAddr
          args:
            sources: 192.168.1.1/24 
    - id: RouteHttps
      uri: https://example.org/
      tls:
        trust-all: true
        crt-filepath: ./tls/server.crt
      predicates:
        - Path=/blue
    - id: RouteLB
      uri: lb://servername
      predicates:
        - Path=/red
```