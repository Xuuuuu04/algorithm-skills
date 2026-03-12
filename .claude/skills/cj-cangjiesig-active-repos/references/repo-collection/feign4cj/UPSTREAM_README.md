<div align="center">
<h1>feign4cj</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.0.1-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjcov-0.0%25-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/state-孵化-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-OHOS/Cloud-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/points- ？/100-brightgreen" style="display: inline-block;" />
</p>


## 介绍

**Feign4cj** 是一个基于宏的 **HTTP 客户端**，受 [feign](https://github.com/OpenFeign/feign) 启发，提供了通过仓颉语言的**接口**定义 **HTTP API** 的方式。

### 项目特性

- 用户只需**定义接口**，无需编写具体的 HTTP 请求相关代码

- 完全使用**宏**实现，与 [feign](https://github.com/OpenFeign/feign) 使用的动态代理相比拥有**较少的运行时性能开销**。

- 支持 `encoder`、`decoder`、`queryMapEncoder` 等自定义参数编解码器。

- 支持配置 `Target`、添加拦截器、指定 HTTP 客户端实现等多种自定义配置。

### 项目计划

<!-- 介绍开发和维护等关键里程碑 -->

TODO

## 项目架构

<!-- 架构图文说明，包括模块说明、架构层次等详细说明。 -->

### 源码目录

```shell
.
├── README.md             # 整体介绍
├── example               # 示例代码
└── src                   # 源码目录
    ├── core              # 运行时依赖的核心功能
    ├── param             # 宏参数解析工具
    ├── test              # 单元测试
    └── util              # 工具类
```

### 接口说明

TODO: 主要类和函数接口说明，详见 [API](./doc/feature_api.md)

#### 支持的宏

| 宏 | 修饰级别 | 用途 | 示例 |
| --- | --- | --- | --- |
| `@Feign` | 接口 | 声明 HTTP API | `@Feign public interface Api {}` |
| `@Headers` | 接口或函数 | 指定所有/单个函数请求时附带的请求头 | `@Feign @Headers["Foo: bar"] public interface Api {}` <br /> `@Headers["Foo: bar"] func getUser(@Param userId: Int)` |
| `@Body` | 函数 | 指定请求体 | `@Body["{{\"foo\": \"bar\"}}"]` <br /> `@Body["<foo>bar</foo>"]` |
| `@RequestLine` | 函数 | 同时指定 HTTP 方法和路径 | `@RequestLine["GET /api/v1/user/{userId}"]` |
| `@Get` | 函数 | 指定路径，并使用 GET 方法 | `@Get["/api/v1/user/{userId}"]` |
| `@Post` | 函数 | 指定路径，并使用 POST 方法 | `@Post["/api/v1/user/{userId}"]` |
| `@Put` | 函数 | 指定路径，并使用 PUT 方法 | `@Put["/api/v1/user/{userId}"]` |
| `@Delete` | 函数 | 指定路径，并使用 DELETE 方法 | `@Delete["/api/v1/user/{userId}"]` |
| `@Options` | 函数 | 指定路径，并使用 OPTIONS 方法 | `@Options["/api/v1/user/{userId}"]` |
| `@Head` | 函数 | 指定路径，并使用 HEAD 方法 | `@Head["/api/v1/user/{userId}"]` |
| `@Connect` | 函数 | 指定路径，并使用 CONNECT 方法 | `@Connect["/api/v1/user/{userId}"]` |
| `@Trace` | 函数 | 指定路径，并使用 TRACE 方法 | `@Trace["/api/v1/user/{userId}"]` |
| `@Patch` | 函数 | 指定路径，并使用 PATCH 方法 | `@Patch["/api/v1/user/{userId}"]` |
| `@Param` | 参数 | 指定表达式的参数 | `@Get["/user/{userId}"] func getUser(@Param userId: Int): String` <br /> `@Get["/user/{userId}"] func getUser(@Param["userId"] id: Int): String` <br /> `@Post["/user"] @Body["{{\"name\": \"{name}\"}}"] func createUser(@Param name: String): Unit` |
| `@QueryMap` | 参数 | 指定可以被展开为请求字符串的参数。需要该类型实现 `Serializable` 接口并且能够被展开为 `DataModelStruct`。 | `@Get["/users"] func getUsers(@QueryMap query: HashMap<String, String>): Array<User>` <br /> `@Get["/users"] func getUsers(@QueryMap query: CustomQuery): Array<User>` | 
| `@HeaderMap` | 参数 | 指定可以被展开为请求头的参数。需要该类型实现 `Serializable` 接口并且能够被展开为 `DataModelStruct`。 | `@Get["/users"] func getUsers(@HeaderMap headers: HashMap<String, String>): Array<User>` <br /> `@Get["/users"] func getUsers(@HeaderMap headers: CustomHeader): Array<User>` | 
| 不被宏修饰的参数 | 参数 | 指定请求体参数。需要该类型实现 `Serializable` 接口，并且在构建客户端时候需指定 `Encoder`。 | `@Post["/user"] func createUser(user: User): Unit` |
| 不被宏修饰的返回值 | 返回值 | 指定响应体被反序列化的类型。需要该类型实现 `Serializable` 接口，并且在构建客户端时候需指定 `Decoder`。 | `@Get["/users"] func getUsers(): Array<User>` |

#### 表达式

在 `@Get`、 `@Header` 等可以附带模板的宏中，允许以 `{key}` 的方式定义可被替换的占位符。当用户向被 `@Param` 修饰函数参数传递值时，将自动替换占位符的内容。例如下面这段代码：

```cangjie
@Get["/user/{userId}"]
func getUser(@Param[userId] id: Int): User
```

当通过 `getUser(1)` 的方式调用时，会自动将请求的路径部分替换为 `/user/1`。

被 `@Param[xxx]` 修饰的名称需要与模板 `{xxx}` 内的名称一致。当省略 `@Param` 宏的参数部分时，将使用变量名作为占位符名称，即需要将上文代码改为：

```cangjie
@Get["/user/{userId}"]
func getUser(@Param userId: Int): User
```

当需要表示 `{` 或 `}` 字符时，需要被分别转义为 `{{` 和 `}}`。

## 使用说明

### 引入依赖


在 `cjpm.toml` 中的 `[dependencies]` 内添加如下内容：

```toml
feign4cj = { git = "https://gitcode.com/PermissionDog/feign4cj" }
```

添加后 `cjpm.toml` 如下所示：

```toml
[dependencies]
  feign4cj = { git = "https://gitcode.com/PermissionDog/feign4cj" }

[package]
  cjc-version = "1.0.0"
  compile-option = ""
  description = "nothing here"
  link-option = ""
  name = "your_package_name_here"
  output-type = "executable"
  src-dir = ""
  target-dir = ""
  version = "1.0.0"
  package-configuration = {}
```
### 功能示例
#### 基本 API 定义功能示例

功能示例描述:

定义一个 `MockApi` 接口，用户可以通过对该接口的 `getComments(1)` 方法进行调用，以获取到 <http://jsonplaceholder.typicode.com/posts/1/comments> 的内容，响应体将以 `字符串` 的形式返回。具体代码见 [example/basic](example/basic/src/main.cj) 。


示例代码如下：

```cangjie
import feign4cj.*
import serialization.serialization.*

@Feign
public interface MockApi {
    @RequestLine["GET /posts/{postId}/comments"]
    func getComments(@Param postId: Int): String
}

main(): Int64 {
    let mockApi = MockApi.builder()
        .target("http://jsonplaceholder.typicode.com")
        .build()
    
    println(mockApi.getComments(1))

    return 0
}
```

执行结果如下：

```json
[
  {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
  },
  ...
]
```

#### 表达式功能示例

功能示例描述:

定义一个 `MockApi` 接口，用户可以在 `@RequestLine`、`@Headers`、`@Body`、`@Get`等宏的参数内通过 `{key}` 的形式定义请求参数模板。响应体将以 `字符串` 的形式返回。具体请求代码及服务端代码见 [example/expr](example/expr/src/main.cj) 。


示例代码如下：

```cangjie
import feign4cj.*
import serialization.serialization.*

@Feign
public interface MockApi {
    @Get["/info"]
    @Headers[[
        "Authorization: Bearer {token}",
        "User-Agent: {ua}"
    ]]
    func info(
        @Param token: String,
        @Param ua: String
    ): String

    @Post["/body"]
    @Headers["Content-Type: application/json"]
    @Body["{{\"greetings\": \"{greetings}\"}}"]
    func greetingJson(
        @Param greetings: String
    ): String

    @Post["/body"]
    @Headers["Content-Type: application/xml"]
    @Body["<greetings>{greetings}</greetings>"]
    func greetingXml(
        @Param greetings: String
    ): String
}

main(): Int64 {
    // 服务器代码见 example/expr/src/server.cj
    spawn { startServer() }

    let mockApi = MockApi.builder()
        .target("http://localhost:8080")
        .build()
    println(mockApi.info("ZmVpZ240Y2o=", "feign4cj"))
    println(mockApi.greetingJson("hello json"))
    println(mockApi.greetingXml("hello xml"))
    
    return 0
}
```

执行结果如下：

```
Authorization: Bearer ZmVpZ240Y2o=
User-Agent: feign4cj
Content-Type: application/json
body:
{"greetings": "hello json"}
Content-Type: application/xml
body:
<greetings>hello xml</greetings>
```

#### 拦截器功能示例

功能示例描述:

定义一个 `MockApi` 接口，用户可以在使用 `MockApi.builder()` 建造者后使用 `interceptor()` 指定函数形式的拦截器。此处添加了对请求 URL 和请求头进行打印的拦截器。响应体将以 `字符串` 的形式返回。具体请求代码见 [example/interceptor](example/interceptor/src/main.cj) 。


示例代码如下：

```cangjie
import feign4cj.*
import serialization.serialization.*

@Feign
public interface MockApi {
    @Post["/posts"]
    func createPost(body: PostModel): PostModel
}

public class PostModel <: Serializable<PostModel> & ToString {
  ...
}

main(): Int64 {

    let mockApi = MockApi.builder()
        .target("http://jsonplaceholder.typicode.com")
        .encoder(JsonEncoder())
        .decoder(JsonDecoder())
        .interceptor { ctx =>
            println("request url: ${ctx.request.url}")
            println("headers: ${ctx.request.headers}")
            ctx.next()
        }.build()
    
    println(mockApi.createPost(PostModel(1, "foo", "bar")))

    return 0
}
```

执行结果如下：

```
request url: http://jsonplaceholder.typicode.com/posts
headers: [(content-type, [application/json; charset=UTF-8])]
{
  "id": 101,
  "userId": 1,
  "title": "foo",
  "body": "bar"
}
```

#### Encoder & Decoder 功能示例

功能示例描述:

该示例分别定义了 `MockApi` 和 `RawMockApi` 两个接口，其中 `MockApi` 的请求体和响应体都将被分别序列化和反序列化为 JSON；`RawMockApi` 的响应体则是以字符串和字节数组的形式返回。具体请求代码见 [example/json](example/json/src/main.cj)。

对于需要进行 JSON 序列化或使用自定义序列化的情况，需要显式在建造者处指定 `encdoer()` 和 `decoder()`。

示例代码如下：

```cangjie
import feign4cj.*
import serialization.serialization.*

@Feign
public interface MockApi {
    @RequestLine["GET /posts/{postId}/comments"]
    func getComments(
        @Param["postId"] id: Int
    ): Array<CommentModel>

    @Post["/posts"]
    func createPost(body: PostModel): PostModel
}

@Feign
public interface RawMockApi {
    @RequestLine["GET /posts/{postId}/comments"]
    func getString(
        @Param["postId"] id: Int
    ): String

    @RequestLine["GET /posts/{postId}/comments"]
    func getBytes(
        @Param["postId"] id: Int
    ): Array<Byte>
}

public class PostModel <: Serializable<PostModel> {
  ...
}

public class CommentModel <: Serializable<CommentModel> {
  ...
}

main(): Int64 {

    let mockApi = MockApi.builder()
        .target("http://jsonplaceholder.typicode.com")
        .encoder(JsonEncoder())
        .decoder(JsonDecoder())
        .build()
    
    println(mockApi.getComments(1).size)
    println(mockApi.createPost(PostModel(1, "foo", "bar")))

    let rawMockApi = RawMockApi.builder()
        .target("http://jsonplaceholder.typicode.com")
        .build()

    println(rawMockApi.getString(1))
    println(rawMockApi.getBytes(1).size)

    return 0
}
```

执行结果如下：

```
5
{
  "id": 101,
  "userId": 1,
  "title": "foo",
  "body": "bar"
}
[
  {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
  },
  ...
]
1510
```



## 约束与限制
支持仓颉版本 `1.0.0`。

## 开源协议
[MIT License](LICENSE)

## 参与贡献

欢迎给我们提交PR，欢迎给我们提交Issue，欢迎参与任何形式的贡献。

本项目是 [SIGCANGJIE / 仓颉兴趣组](https://gitcode.com/SIGCANGJIE) 培育的社区项目。

<center><img src="https://raw.gitcode.com/SIGCANGJIE/homepage/attachment/uploads/eda83126-b3fc-4e77-b09e-cd213274004f/sigcangjie.png" /></center>