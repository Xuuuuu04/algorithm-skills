<div align="center">
<h1>tea</h1>
</div>
<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjcov-0.0%25-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/state-孵化-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-OHOS/Cloud-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/points- ？/100-brightgreen" style="display: inline-block;" />
</p>




## <img alt="" src="./doc/readme-image/readme-icon-introduction.png" style="display: inline-block;" width=3%/> 1 介绍

一个受Express、Gin、Fiber、Echo等Web框架启发的函数式Http Server项目

旨在高效、轻量、灵活、开放

欢迎大家的使用与建议！

您只需要在项目的cjpm.toml下的加入：

```cangjie
  tea = { git = "https://gitcode.com/yishengTH/tea", output-type = "static", branch = "main"}
```

继续在控制台输入`cjpm update`即可引入本项目



### 1.1 项目特性

🚀 Tea基于高性能、零拷贝、字节级操作实现的 [seedhttp](https://gitcode.com/yishengTH/SeedHTTP) http引擎

🚀 Tea拥有极其灵活的路由写法，支持函数式、仿函数式Handler，支持链式路由、分组路由等

🚀 Tea拥有灵活的路由参数，支持普通参数、可选参数、通配符、可选通配符、多个通配符等，并能处理一些复杂情况

🚀 Tea使用路由缓存来添加路由，原理上可以做到路由热更新；目前已支持热添加路由

🚀内置彩色日志库，轻松区分不同日志等级，且可扩展

🚀钩子函数机制，借助钩子函数可以完成相当多的中间件扩展功能

🚀提供了一些在Web场景下常用的常量



#### 简单的开始

下面是一个最简单的开始

```cangjie
import tea.*

main(): Int64 {
    let app = Tea.default()

    app.get("/") { c =>
        c.sendString("hello, Tea!")
    }

    app.run(8080)
    
    return 0
}
```

然后在浏览器中访问`http://localhost:8080`即可看到输出的结果`hello, Tea!`



#### 灵活路由参数

**路由参数**

```cangjie
// GET http://localhost:8080/hello%20world
app.get("/:value") { c =>
    c.sendString("value: ${c.param("value") ?? "None"}")
    // Response: "value: hello world"
    // 注: %20 不会自动解码成空格, 需要配置TeaConfig的unescapePath为true
}
```

**可选参数**

```cangjie
// GET http://localhost:8080/Tom
// GET http://localhost:8080/
app.get("/:name?") { c =>
    if (let Some(name) <- c.param("name")) {
        c.sendString("Hello ${name}")
        // Response: "Hello Tom" when GET http://localhost:8080/Tom
        return
    }
    c.sendString("Where is Tom?")
    // Response: "Where is Tom?" when GET http://localhost:8080/
}
```

**通配符**

```cangjie
// GET http://localhost:8080/api/user/Tom
app.get("/api/*") { c =>
    c.sendString("API path: ${c.param("*") ?? "None"}")
    // Response: "API path: user/Tom"
}
```

路由参数的功能不止演示的这些，详见`指引与说明`中`路由参数`



#### 链式路由

类express注册路由的方式，用链式调用的方式为同一个url注册多个方法的handler，更`restful`！！！

```cangjie
app.route("api").route("/user/:id?")
.get { c =>
    c.sendString("get")
}
.post { c =>
    c.sendString("post")
}
.put { c =>
    c.sendString("put")
}
.delete { c =>
    c.sendString("delete")
}
```



#### 路由重建

在运行时重建路由树，可以做到运行时添加路由

先请求/static，这个handler又注册了一个/dynamic的路由

```cangjie
app.get("/static") { c =>
    app.get("/dynamic") { c =>
        c.sendStatus(StatusOK)
    }

    app.rebuildTree()
}
```

但是注意，这个方法并不是线程安全的，必须要确保在不并发的情况下使用！！！



#### 函数元信息

内部的Handler全部使用仿函数处理，因此每个Handler都可以携带自己的描述信息

```cangjie
let h = Handler { c =>
	// ..
}
let map = h.metaData  // metaData类型是HashMap<String, Any>
// .. 对map进行一些操作, 从而添加对函数的描述信息
```

同时，也没有放弃外部以函数形式注册的支持

仍然可以使用尾随lambda的形式注册纯函数HandlerFunc，在Tea内部会统一转换成Handler类



### 1.2 项目计划
- [x] 路由机制.. 框架精髓部分。已完成路由部分并重组测试。
- [ ] 路由约束...计划中，架构已支持。未来实现
- [ ] 挂载...计划中，未来实现
- [x] 重建TeaContext的多个方法..已完成
- [x] 钩子函数机制...已完成，借助钩子函数可以完成相当多的中间件扩展功能
- [ ] 多格式Bind...等待中，已支持Json，其他格式将在语言或者其他三方库完成差不多再支持
- [ ] 配置管理机制...计划中
- [x] 彩色日志...已实现
- [ ] 代码优化...计划中，需要等框架大部分功能完备后进行
- [ ] 客户端...暂无计划，未来会支持
- [ ] 文件上传、下载、流式传输...计划中 等seedhttp支持才能支持..
- [ ] 完整的测试...计划中，需要等框架大部分功能完备后进行，测试将优先确保路由机制的稳固
- [ ] 完全零拷贝——需要仓颉官方的支持，目前kernel已基于字节数组实现，性能比官方实现高
- [ ] 更多的内置中间件，需要社区支持...包括适配官方的Http Server，预计将通过中间件的形式支持接口形式的适配
- [ ] 在支持String零拷贝后，做一套String零拷贝处理工具，等待仓颉官方支持中...



## 2.  API

这里仅介绍对外API

### 2.1 Tea

#### default & new

default方法返回一个以默认的TeaConfig作为配置的Tea实例

new方法需要传入自定义的config配置，意味着如果需要修改配置，就要使用new方法来构造Tea实例

```cangjie
// 按照默认配置构造Tea实例
let app = Tea.default()

// 使用自定义配置构造Tea实例
let config = TeaConfig()
// .. 可以对config进行一些设置
let app = Tea.new(config)
```



#### shutDown

shutDown方法调用后，将强制结束当前server

```cangjie
public func shutDown(): Unit
```



#### register

```cangjie
// 包括这些注册路由的方法：
// 使用仿函数注册路由
// 注: 仓颉使用Array表示可选参数, middleware参数可传可不传
func get(path: String, handler: Handler, middleware: Array<Handler>): IRouter
func head(path: String, handler: Handler, middleware: Array<Handler>): IRouter
func post(path: String, handler: Handler, middleware: Array<Handler>): IRouter
func put(path: String, handler: Handler, middleware: Array<Handler>): IRouter
func delete(path: String, handler: Handler, middleware: Array<Handler>): IRouter
func connect(path: String, handler: Handler, middleware: Array<Handler>): IRouter
func options(path: String, handler: Handler, middleware: Array<Handler>): IRouter
func trace(path: String, handler: Handler, middleware: Array<Handler>): IRouter
func patch(path: String, handler: Handler, middleware: Array<Handler>): IRouter
// 和use其实是一个作用 就是给全部的方法都注册这个handler
func all(path: String, handler: Handler, middleware: Array<Handler>): IRouter

// 使用纯函数注册路由
func get(path: String, handler: HandlerFunc): IRouter
func head(path: String, handler: HandlerFunc): IRouter
func post(path: String, handler: HandlerFunc): IRouter
func put(path: String, handler: HandlerFunc): IRouter
func delete(path: String, handler: HandlerFunc): IRouter
func connect(path: String, handler: HandlerFunc): IRouter
func options(path: String, handler: HandlerFunc): IRouter
func trace(path: String, handler: HandlerFunc): IRouter
func patch(path: String, handler: HandlerFunc): IRouter
func all(path: String, handler: HandlerFunc): IRouter

// 可以自选给某些特定的方法添加路由
func add(methods: Array<String>, path: String, handler: Handler, middleware: Array<Handler>): IRouter
func add(methods: Array<String>, path: String, handler: HandlerFunc, middleware: Array<HandlerFunc>): IRouter
```

eg. 使用HandlerFunc + 尾随lambda的形式注册路由

```cangjie
app.get("/api/get") { c =>
    c.sendString("Get Handler")
}

app.post("/api/post") { c =>
    c.sendString("Post Handler")
}
```

eg. 使用Handler + 尾随lambda的形式注册路由

```cangjie
app.get("/api/get", Handler { c =>
    c.sendString("Get Handler")
}) 
```

注意： 如果不使用仿函数Handler可以携带一个元信息（HashMap）的特性，建议使用纯函数HandlerFunc的形式来注册路由，语法上会简便许多



#### use

注册中间件，中间件是为了对请求或响应进行修改而设计的函数，可以链式使用多个中间件、可以用于特定路径前缀

常见用途有：限制重复请求访问公共API、基本认证、负载管理等等...

```cangjie
// 为当前app或者分组下的全部路由注册中间件
public func use(middleware: Array<Handler>): IRouter
public func use(middleware: Array<HandlerFunc>): IRouter

// 为前缀为path的路由注册中间件
public func use(path: String, middleware: Array<Handler>): IRouter
public func use(path: String, middleware: Array<HandlerFunc>): IRouter
```

eg. 使用use注册中间件

```cangjie
// 为app下全部路由注册此中间件
// 现在请求app下任意路由都会经过本次中间件的处理
app.use { c =>
    println("this is middleware")
    c.next() // 调用c.next() 才会使中间件向下进行，否则本次执行链将在此次中间件中断
}
```





#### group

创建路由组，路由组是一种组织和管理多个路由的方式

可以给某个特定的路由组使用特定的中间件

```cangjie
// 创建路由组
func group(prefix: String, handlers: Array<Handler>): IRouter
```

eg. 使用路由组

```cangjie
app = Tea.default()

api = app.group("/api", handler)  // /api

v1 = api.group("/v1", handler)    // /api/v1
v1.get("/list", handler)          // /api/v1/list
v1.get("/user", handler)          // /api/v1/user

v2 = api.group("/v2", handler)    // /api/v2
v2.get("/list", handler)          // /api/v2/list
v2.get("/user", handler)          // /api/v2/user
```



#### route

```cangjie
// 先创建一个路由前缀, 然后继续可以链式调用去注册方法
func route(path: String): IRegister
```

eg. 更restful的方式创建路由

```cangjie
app.route("api").route("/user/:id?")
.get { c =>
    c.sendString("get")
}
.post { c =>
    c.sendString("post")
}
.put { c =>
    c.sendString("put")
}
.delete { c =>
    c.sendString("delete")
}
```



#### rebuildTree

重建路由树，在运行时重建路由树，可以做到运行时添加路由

```cangjie
public func rebuildTree(): Unit
```

eg. 使用重建路由树的一个场景

先请求/static，这个handler又注册了一个/dynamic的路由

```cangjie
app.get("/static") { c =>
    app.get("/dynamic") { c =>
        c.sendStatus(StatusOK)
    }

    app.rebuildTree()
}
```

但是注意，这个方法并不是线程安全的，必须要确保在不并发的情况下使用！！！

本方法可以配合以后热更新路由来使用~~~



#### name

```cangjie
public func name(name: String): IRouter
```

给最后一次创建的路由取名



#### getRoute

```cangjie
public func getRoute(name: String): ?Route
```

根据路由的名称从已注册的路由中寻找



### 2.2 TeaContext

TeaContext是用户在Handler中使用最多的类



#### send

```cangjie
public func send(body: Array<Byte>): Unit
```

以Array<Byte>的形式发送响应体，适合高性能场景下发送响应体

注意：send开头的发送响应体的方法都会重设响应体，而不是续写，如果需要续写响应体，使用write开头的发送方法



#### sendStatus

```cangjie
public func sendStatus(status: Int64): Unit
```

根据状态码发送响应体，status与响应体的对照关系参见seedhttp项目的status中

如果找不到状态码对应的响应体，会发送`Unknown Status Code`



#### sendString

```cangjie
public func sendString(body: String): Unit
```

以String的形式发送响应体



#### sendJson

```cangjie
public func sendJson<T>(body: Serializable<T>): Unit
```

以Json的形式发送响应体，T需要实现Serializable方法



#### string

```cangjie
public func string(code: Int, data: String): Unit
```

以String的形式发送响应体，并且重设状态码为code，如果code为200一般使用sendString方法代替



#### json

```cangjie
public func json<T>(code: Int, data: Serializable<T>): Unit
```

以Json的形式发送响应体，并且重设状态码为code，如果code为200一般使用sendJson方法代替



#### param

```cangjie
public func param(_key: String): ?String
```

获取路由中的param

eg. 获取路由中的param

```cangjie
// GET http://example.com/user/fenny
app.get("/user/:name") {
  c.param("name") // "fenny"

  // ...
}

// GET http://example.com/user/fenny/123
app.get("/user/*") {
  c.param("*")  // "fenny/123"
  c.param("*1") // "fenny/123"
  // ...
}
```

eg. 对于通配符 `+` 或者 `*`来说，可以使用数字来获取他们出现的先后位置

```cangjie
// ROUTE: /v1/*/shop/*
// GET:   /v1/brand/4/shop/blue/xs
c.param("*1")  // "brand/4"
c.param("*2")  // "blue/xs"
```

eg. 如果说出现了多个通配符，但是没有指定获取哪个位置，那么默认获取第一个

```cangjie
app.get("/v1/*/shop/*") {
  c.param("*") // 默认就是*1
})
```



#### query

```cangjie
public func query(key: String): ?String
```

eg. 获取路由中的query参数

```cangjie
// GET http://localhost:8080/?name=lzj&brand=nike
app.get("/") {
  c.query("name")          // "lzj"
  c.query("brand")         // "nike"

  // ...
}
```



#### getRequestHeader

```cangjie
public func getRequestHeader(key: String): ?String
```

根据key获取请求头，注意：暂时没有对key进行特殊处理，如果需要获取到对应key的value，这个传入的key必须和请求头中的key一模一样才能正常获取到



#### getRawData

```cangjie
public func getRawData(): String
```

获取请求体的数据，如果没有请求体将返回 `""`



#### bindJson

```cangjie
public func bindJson<T>(): T where T <: Serializable<T>
```

以Json的形式把请求体的数据绑定到一个对象中，非常常用

eg. 使用bindJson

```cangjie
public class User <: Serializable<User>{
    public User(
        public let id: UInt32,
        public let username: String,
        public let password: String
    ) {}

    public func serialize(): DataModel {
        return DataModelStruct()
            .add(field<UInt32>("id", this.id))
            .add(field<String>("username", this.username))
            .add(field<String>("password", this.password))
    }

    public static func deserialize(dm: DataModel): User {
        var dms = match (dm) {
            case st: DataModelStruct => st
            case _ => throw Exception("this data is not DataModelStruct")
        }
        return User(
            UInt32.deserialize(dms.get("id")),
            String.deserialize(dms.get("username")),
            String.deserialize(dms.get("password"))
        )
    }
}

// POST http://localhost:8080/user
/*
  携带请求体
  {
    "id": 1,
    "username": "lzj",
    "password": "123456"
  }
*/
app.post("/user") { c =>
	let user = c.bindJson<User>()
	// 获得到请求数据填充过后的user对象
	
	// ..
}
```



#### setResponseHeader

```cangjie
public func setResponseHeader(key: String, value: String): Unit
```

设置响应头，可以结合Constants给的一些常量使用



#### delResponseHeader

```cangjie
public func delResponseHeader(key: String): Unit
```

删除对应的请求头



#### setStatusCode

```cangjie
public func setStatusCode(code: Int64): TeaContext
```

设置状态码，注意这个函数返回TeaContext，意味着可以链式调用

eg. 链式调用

```cangjie
app.get("/") { c =>
	c.setStatusCode(200).sendString("hello!")
}
```



#### setContentType

```cangjie
public func setContentType(contentType: String): TeaContext
```

设置响应头的ContentType



#### next

```cangjie
public func next(): Unit
```

调用下一个中间件处理，这是中间件的核心方法

进入下个中间件有且只有通过next方法，如果不在本次中间件调用next，那么中间件执行链将会在本次中断



#### set

```cangjie
public func set(key: String, value: String): Unit
```

设置共享参数

在中间件执行链中，这些handler共享一个TeaContext，如果希望本次的数据给后续的中间件使用，那么可以使用set方法来给TeaContext设置一些数据，在后续中间件中get来使用。

eg. 使用set和get来设置与获取共享参数

```cangjie
// GET http://localhost:8080/test
let app = Tea.default()

app.use { c =>
    c.set("book", "Harry Potter")
    c.next()
}

app.get("/test") { c =>
    if (let Some(book) <- c.get("book")) {
        let bookStr = book as String
        c.sendString("get value: ${bookStr.getOrThrow()}") // Response => "get value: Harry Potter"
        return
    }
    c.sendString("nothing")
}

app.run(8080)
```



#### get

```cangjie
public func get(key: String): ?Any
```

获取共享参数



### 2.3 TeaConfig

Tea的配置信息，使用自定义配置需要使用Tea.new( ) 方法

```cangjie
// 使用自定义配置构造Tea实例
let config = TeaConfig()
// .. 可以对config进行一些设置
let app = Tea.new(config)
```

既可以在创建时以命名参数的形式传入需要修改的配置信息，又可以在创建后修改

```cangjie
// 使用命名参数
let config = TeaConfig(caseSensitive: true)

// 在创建后修改参数
let config = TeaConfig()
config.caseSensitive = true
```



#### requestMethods

```cangjie
public var requestMethods!:Array<String> = defaultMethods
```

支持的请求方法，默认是HTTP的九个方法：

```cangjie
let defaultMethods: Array<String> = [
    MethodGet,
	MethodHead,
	MethodPost,
	MethodPut,
	MethodDelete,
	MethodConnect,
	MethodOptions,
	MethodTrace,
	MethodPatch
] // 具体的值可以见Constants
```

可以替换成自定义的HTTP方法



#### caseSensitive

```cangjie
public var caseSensitive!: Bool = false
```

路由是否区分大小写，开启后 /a 和 /A 认为是不同的路由，默认不开启，**即默认认为 /a 和 /A 是一样的**



#### strictRouting

```cangjie
public var strictRouting!: Bool = false
```

是否为严格路由模式，开启后 /a 和 /a/ 认为是不同的路由，默认不开启，**即默认会处理路由最后的/**



#### errorHandler

```cangjie
public var errorHandler!: ?ErrorHandler = None
```

异常处理器，如果是None会Tea的实例会使用默认的异常处理器

```cangjie
public type ErrorHandler = (TeaContext, Exception) -> Bool
```

注：成功处理Exception之后需要返回true，如果返回flase，那么本次执行链将直接抛出异常，再由seedhttp的异常处理机制兜底，所以不建议轻易改动默认的异常处理器。默认的异常处理器已经可以兜底所有异常。



#### disableStartupMessage

```cangjie
public var disableStartupMessage!: Bool = false
```

禁止输出启动信息，设置为true则不输出，默认输出启动的logo和port、pid等



#### unescapePath

```cangjie
public var unescapePath!: Bool = false
```

是否解码请求来的URL，设置为true表示进行解码

eg. 设置为true

```cangjie
    let config = TeaConfig(unescapePath: true)
    let app = Tea.new(config)
    app.get("/仓颉") { c =>
        c.sendString("你好") // GET: localhost:8080/%E4%BB%93%E9%A2%89
    }
    app.run(8080)
```

如果不设置，将会提示找不到路径`/%E4%BB%93%E9%A2%89`



### 2.4 Bind

bind计划专门实现一整套完整的逻辑，来bind不同的格式比如json、xml、html等等，支持用户自定义格式的bind等等

**但是受制于目前生态状况，暂时难以支持更多格式的bind**

所以仅实现最最常用的bindJson即：TeaContext.bindJson() 



### 2.5 Hook

钩子函数，在tea运作的各个阶段调用，目前有**6类**钩子函数

```cangjie
public type OnRouteHandler      = (Route) -> Unit  // 作用于添加Route之后
public type OnNameHandler       = (Route) -> Unit  // 作用于命名Route之后
public type OnGroupHandler      = (Group) -> Unit  // 作用于添加Group之后
public type OnGroupNameHandler  = (Group) -> Unit  // 作用于命名Group之后
public type OnListenHandler     = () -> Unit       // 作用于启动项目之前, 初始化完成后，输出启动信息前
public type OnShutdownHandler   = () -> Unit       // 作用于调用app.shutDown()执行的开始，结束server之前
```

使用tea的实例来注册这些函数

```cangjie
// Hooks类的方法:
public func registerOnRoute(handler: Array<OnRouteHandler>): Unit
public func registerOnName(handler: Array<OnNameHandler>): Unit
public func registerOnGroup(handler: Array<OnGroupHandler>): Unit
public func registerOnGroupName(handler: Array<OnGroupNameHandler>): Unit
public func registerOnListen(handler: Array<OnListenHandler>): Unit
public func registerOnShutdown(handler: Array<OnShutdownHandler>): Unit
```

eg. 注册钩子函数

```cangjie
let app = Tea.default()
app.hooks.registerOnGroup(...) // 省略
```



### 2.6 Log

一个简单内置的带缓冲彩色日志，实现类为`ColorLogger`

使用全局变量logger，为了保证灵活性，使用**官方接口**，可以在项目任意地方使用，也可以随时替换成其他日志实现

并且日志的输出目标可以替换为其他文件，会自动检测，不在文件中输出颜色符号

```cangjie
public var logger: Logger = ColorLogger(Console.stdOut)
```

注意：

1. 在tea项目中，没有使用仅可以使用一次的`setGlobalLogger`方法，意味着可以给引入者最小的干扰，可以随时替换为其他日志实现
2. 使用前要引入官方日志库

eg. 在项目中使用下面的例子查看输出效果

```cangjie
logger.level = LogLevel.ALL  // 设置level
logger.debug("女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变",("k1", [[1, 4], [2, 5], [3]]), ("password", "v22222"))
logger.error("女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变",("k1", [[1, 4], [2, 5], [3]]), ("password", "v22222"))
logger.fatal("女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变",("k1", [[1, 4], [2, 5], [3]]), ("password", "v22222"))
logger.info("女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变",("k1", [[1, 4], [2, 5], [3]]), ("password", "v22222"))
logger.trace("女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变",("k1", [[1, 4], [2, 5], [3]]), ("password", "v22222"))
logger.warn("女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变女大十一变",("k1", [[1, 4], [2, 5], [3]]), ("password", "v22222"))
```



### **2.7 Constants**

#### HTTP Method

```cangjie
public const	MethodGet     = "GET"     // RFC 7231, 4.3.1
public const	MethodHead    = "HEAD"    // RFC 7231, 4.3.2
public const	MethodPost    = "POST"    // RFC 7231, 4.3.3
public const	MethodPut     = "PUT"     // RFC 7231, 4.3.4
public const	MethodPatch   = "PATCH"   // RFC 5789
public const	MethodDelete  = "DELETE"  // RFC 7231, 4.3.5
public const	MethodConnect = "CONNECT" // RFC 7231, 4.3.6
public const	MethodOptions = "OPTIONS" // RFC 7231, 4.3.7
public const	MethodTrace   = "TRACE"   // RFC 7231, 4.3.8
```



#### ContentType

```cangjie
public const	MIMETextXML         = "text/xml"
public const	MIMETextHTML        = "text/html"
public const	MIMETextPlain       = "text/plain"
public const	MIMETextJavaScript  = "text/javascript"
public const	MIMETextCSS         = "text/css"
public const	MIMEApplicationXML  = "application/xml"
public const	MIMEApplicationJSON = "application/json"
public const	MIMEApplicationCBOR = "application/cbor"
public const	MIMEApplicationForm       = "application/x-www-form-urlencoded"
public const	MIMEOctetStream           = "application/octet-stream"
public const	MIMEMultipartForm         = "multipart/form-data"
public const	MIMETextXMLCharsetUTF8         = "text/xml; charset=utf-8"
public const	MIMETextHTMLCharsetUTF8        = "text/html; charset=utf-8"
public const	MIMETextPlainCharsetUTF8       = "text/plain; charset=utf-8"
public const	MIMETextJavaScriptCharsetUTF8  = "text/javascript; charset=utf-8"
public const	MIMETextCSSCharsetUTF8         = "text/css; charset=utf-8"
public const	MIMEApplicationXMLCharsetUTF8  = "application/xml; charset=utf-8"
public const	MIMEApplicationJSONCharsetUTF8 = "application/json; charset=utf-8"
```



#### Header

```cangjie
public const	HeaderAuthorization                      = "Authorization"
public const	HeaderProxyAuthenticate                  = "Proxy-Authenticate"
public const	HeaderProxyAuthorization                 = "Proxy-Authorization"
public const	HeaderWWWAuthenticate                    = "WWW-Authenticate"
public const	HeaderAge                                = "Age"
public const	HeaderCacheControl                       = "Cache-Control"
public const	HeaderClearSiteData                      = "Clear-Site-Data"
public const	HeaderExpires                            = "Expires"
public const	HeaderPragma                             = "Pragma"
public const	HeaderWarning                            = "Warning"
public const	HeaderAcceptCH                           = "Accept-CH"
public const	HeaderAcceptCHLifetime                   = "Accept-CH-Lifetime"
public const	HeaderContentDPR                         = "Content-DPR"
public const	HeaderDPR                                = "DPR"
public const	HeaderEarlyData                          = "Early-Data"
public const	HeaderSaveData                           = "Save-Data"
public const	HeaderViewportWidth                      = "Viewport-Width"
public const	HeaderWidth                              = "Width"
public const	HeaderETag                               = "ETag"
public const	HeaderIfMatch                            = "If-Match"
public const	HeaderIfModifiedSince                    = "If-Modified-Since"
public const	HeaderIfNoneMatch                        = "If-None-Match"
public const	HeaderIfUnmodifiedSince                  = "If-Unmodified-Since"
public const	HeaderLastModified                       = "Last-Modified"
public const	HeaderVary                               = "Vary"
public const	HeaderConnection                         = "Connection"
public const	HeaderKeepAlive                          = "Keep-Alive"
public const	HeaderAccept                             = "Accept"
public const	HeaderAcceptCharset                      = "Accept-Charset"
public const	HeaderAcceptEncoding                     = "Accept-Encoding"
public const	HeaderAcceptLanguage                     = "Accept-Language"
public const	HeaderCookie                             = "Cookie"
public const	HeaderExpect                             = "Expect"
public const	HeaderMaxForwards                        = "Max-Forwards"
public const	HeaderSetCookie                          = "Set-Cookie"
public const	HeaderAccessControlAllowCredentials      = "Access-Control-Allow-Credentials"
public const	HeaderAccessControlAllowHeaders          = "Access-Control-Allow-Headers"
public const	HeaderAccessControlAllowMethods          = "Access-Control-Allow-Methods"
public const	HeaderAccessControlAllowOrigin           = "Access-Control-Allow-Origin"
public const	HeaderAccessControlExposeHeaders         = "Access-Control-Expose-Headers"
public const	HeaderAccessControlMaxAge                = "Access-Control-Max-Age"
public const	HeaderAccessControlRequestHeaders        = "Access-Control-Request-Headers"
public const	HeaderAccessControlRequestMethod         = "Access-Control-Request-Method"
public const	HeaderOrigin                             = "Origin"
public const	HeaderTimingAllowOrigin                  = "Timing-Allow-Origin"
public const	HeaderXPermittedCrossDomainPolicies      = "X-Permitted-Cross-Domain-Policies"
public const	HeaderDNT                                = "DNT"
public const	HeaderTk                                 = "Tk"
public const	HeaderContentDisposition                 = "Content-Disposition"
public const	HeaderContentEncoding                    = "Content-Encoding"
public const	HeaderContentLanguage                    = "Content-Language"
public const	HeaderContentLength                      = "Content-Length"
public const	HeaderContentLocation                    = "Content-Location"
public const	HeaderContentType                        = "Content-Type"
public const	HeaderForwarded                          = "Forwarded"
public const	HeaderVia                                = "Via"
public const	HeaderXForwardedFor                      = "X-Forwarded-For"
public const	HeaderXForwardedHost                     = "X-Forwarded-Host"
public const	HeaderXForwardedProto                    = "X-Forwarded-Proto"
public const	HeaderXForwardedProtocol                 = "X-Forwarded-Protocol"
public const	HeaderXForwardedSsl                      = "X-Forwarded-Ssl"
public const	HeaderXUrlScheme                         = "X-Url-Scheme"
public const	HeaderLocation                           = "Location"
public const	HeaderFrom                               = "From"
public const	HeaderHost                               = "Host"
public const	HeaderReferer                            = "Referer"
public const	HeaderReferrerPolicy                     = "Referrer-Policy"
public const	HeaderUserAgent                          = "User-Agent"
public const	HeaderAllow                              = "Allow"
public const	HeaderServer                             = "Server"
public const	HeaderAcceptRanges                       = "Accept-Ranges"
public const	HeaderContentRange                       = "Content-Range"
public const	HeaderIfRange                            = "If-Range"
public const	HeaderRange                              = "Range"
public const	HeaderContentSecurityPolicy              = "Content-Security-Policy"
public const	HeaderContentSecurityPolicyReportOnly    = "Content-Security-Policy-Report-Only"
public const	HeaderCrossOriginResourcePolicy          = "Cross-Origin-Resource-Policy"
public const	HeaderExpectCT                           = "Expect-CT"
public const	HeaderPermissionsPolicy                  = "Permissions-Policy"
public const	HeaderPublicKeyPins                      = "Public-Key-Pins"
public const	HeaderPublicKeyPinsReportOnly            = "Public-Key-Pins-Report-Only"
public const	HeaderStrictTransportSecurity            = "Strict-Transport-Security"
public const	HeaderUpgradeInsecureRequests            = "Upgrade-Insecure-Requests"
public const	HeaderXContentTypeOptions                = "X-Content-Type-Options"
public const	HeaderXDownloadOptions                   = "X-Download-Options"
public const	HeaderXFrameOptions                      = "X-Frame-Options"
public const	HeaderXPoweredBy                         = "X-Powered-By"
public const	HeaderXXSSProtection                     = "X-XSS-Protection"
public const	HeaderLastEventID                        = "Last-Event-ID"
public const	HeaderNEL                                = "NEL"
public const	HeaderPingFrom                           = "Ping-From"
public const	HeaderPingTo                             = "Ping-To"
public const	HeaderReportTo                           = "Report-To"
public const	HeaderTE                                 = "TE"
public const	HeaderTrailer                            = "Trailer"
public const	HeaderTransferEncoding                   = "Transfer-Encoding"
public const	HeaderSecWebSocketAccept                 = "Sec-WebSocket-Accept"
public const	HeaderSecWebSocketExtensions             = "Sec-WebSocket-Extensions"
public const	HeaderSecWebSocketKey                    = "Sec-WebSocket-Key"
public const	HeaderSecWebSocketProtocol               = "Sec-WebSocket-Protocol"
public const	HeaderSecWebSocketVersion                = "Sec-WebSocket-Version"
public const	HeaderAcceptPatch                        = "Accept-Patch"
public const	HeaderAcceptPushPolicy                   = "Accept-Push-Policy"
public const	HeaderAcceptSignature                    = "Accept-Signature"
public const	HeaderAltSvc                             = "Alt-Svc"
public const	HeaderDate                               = "Date"
public const	HeaderIndex                              = "Index"
public const	HeaderLargeAllocation                    = "Large-Allocation"
public const	HeaderLink                               = "Link"
public const	HeaderPushPolicy                         = "Push-Policy"
public const	HeaderRetryAfter                         = "Retry-After"
public const	HeaderServerTiming                       = "Server-Timing"
public const	HeaderSignature                          = "Signature"
public const	HeaderSignedHeaders                      = "Signed-Headers"
public const	HeaderSourceMap                          = "SourceMap"
public const	HeaderUpgrade                            = "Upgrade"
public const	HeaderXDNSPrefetchControl                = "X-DNS-Prefetch-Control"
public const	HeaderXPingback                          = "X-Pingback"
public const	HeaderXRequestID                         = "X-Request-ID"
public const	HeaderXRequestedWith                     = "X-Requested-With"
public const	HeaderXRobotsTag                         = "X-Robots-Tag"
public const	HeaderXUACompatible                      = "X-UA-Compatible"
public const	HeaderAccessControlAllowPrivateNetwork   = "Access-Control-Allow-Private-Network"
public const	HeaderAccessControlRequestPrivateNetwork = "Access-Control-Request-Private-Network"
```



### 2.8 Middleware

预计先制作 CORS 中间件

其他的中间件需要社区支持...



## 3.指引与说明

### 3.1 路由机制

#### **路由参数**

路由参数是路由中的动态元素，用于捕获在URL中指定位置的值，可以使用TeaContext.param函数来检索获得的值。

Tea的路由参数十分灵活，提供了多种选择。

eg. 使用路由参数

```cangjie
// GET  /user/lzj/books/hello
app.get("/user/:name/books/:title") { c =>
	println(c.param("name"))  // 输出 `lzj`
	println(c.param("title")) // 输出 `hello`
}

// GET  /user/lzj -> 输出 `lzj`
// GET  /user/    -> 输出 None 不会响应404
// 路由参数后加上? 表示这是一个可选参数
app.get("/user/:name?") { c =>
	println(c.param("name"))
}

// GET  /user/books/hello -> 输出 `books/hello`
// + 代表贪心匹配 将匹配/user/后面的所有url
// + 代表强制匹配 也就是必须匹配到东西 此时请求url: /user/ 会响应404
app.get("/user/+") { c =>
	println(c.param("+"))
}

// GET  /user/books/hello -> 输出 `books/hello`
// * 代表贪心匹配 将匹配/user/后面的所有url
// * 代表非强制匹配 此时请求url: /user/ 仍然可以正常执行handler
app.get("/user/*") { c =>
	println(c.param("*"))
}

// GET /v1/some/resource/name:customVerb"
app.get("/v1/some/resource/name\:customVerb") {
    c.sendString("Hello, Tea!")
})

```



在路由中搭配`.` 或 `-` 有一些非常实用的价值：

```cangjie
// GET /plantae/prunus.persica
app.get("/plantae/:genus.:species") {
	c.param("genus")   // => "prunus"
	c.param("species") // => "persica"
})

// GET /flights/LAX-SFO
app.get("/flights/:from-:to") {
	c.param("from")  // => "LAX"
	c.param("to")    // => "SFO"
})
```



tea的路由非常灵活，可以处理下面这些情况：

```cangjie
// GET /shop/product/color:blue/size:xs
app.get("/shop/product/color::color/size::size") {
	c.param("color") // => "blue"
	c.param("size")  // => "xs"
}

// GET /@v1
// "sign" -> "@", "param" -> "v1"
app.get("/:sign:param", handler)

// GET /api-v1
// "name" -> "v1" 
app.get("/api-:name", handler)

// GET /customer/v1/cart/proxy
// "*1" -> "customer/", "*2" -> "/cart"
app.get("/*v1*/proxy", handler)

// GET /v1/brand/4/shop/blue/xs
// "*1" -> "brand/4", "*2" -> "blue/xs"
app.get("/v1/*/shop/*", handler)
```

注意：不建议在实际开发中使用复杂的路由匹配，会降低性能




## <img alt="" src="./doc/readme-image/readme-icon-contribute.png" style="display: inline-block;" width=3%/> 4 参与贡献

本项目由 [SIGCANGJIE / 仓颉兴趣组](https://gitcode.com/SIGCANGJIE) 实现并维护。技术支持和意见反馈请提Issue。

本项目基于 [MIT License](LICENSE)，欢迎给我们提交PR，欢迎参与任何形式的贡献。

本项目committer：[@yishengTH](https://gitcode.com/yishengTH)

This project is supervised by [@zhangyin-gitcode](https://gitcode.com/zhangyin_gitcode).