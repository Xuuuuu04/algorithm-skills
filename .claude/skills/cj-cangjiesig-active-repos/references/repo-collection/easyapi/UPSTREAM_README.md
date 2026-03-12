# 轻量级Http服务框架

## API

### 类型

#### EasyHandler

处理器

```cj
public type EasyHandler = (EasyContext) -> Unit
```

#### ResponseHook

路由响应钩子

```cj
public type ResponseHook = (EasyContext) -> Unit
```

### 接口

####

```cj
public interface EasyFilter {
    /**
    * 触发过滤器
    * 
    * @param ctx 上下文
    *
    * @return 是否继续往下执行
    */
    public func filter(ctx: EasyContext): Bool // true则继续执行下一个filter，false则中断请求

    public func order(): Int64 {
        return 0
    }
}
```

### 类

#### EasyRoute

路由

```cj
public class EasyRoute {
    /**
    * 构造函数
    */
    public EasyRoute()

    /**
    * 日志工具
    */
    public mut prop logger: Logger 

    /**
    * 路由配置
    */
    public prop config: EasyConfig 

    /**
    * 添加GET方法处理器
    *
    * @param path 路由路径
    * @param handler 路由处理器
    */
    public func get(path: String, handler: EasyHandler): EasyRoute 

    /**
    * 添加POST方法处理器
    *
    * @param path 路由路径
    * @param handler 路由处理器
    */
    public func post(path: String, handler: EasyHandler): EasyRoute 

    /**
    * 添加PUT方法处理器
    *
    * @param path 路由路径
    * @param handler 路由处理器
    */
    public func put(path: String, handler: EasyHandler): EasyRoute 

    /**
    * 添加DELETE方法处理器
    *
    * @param path 路由路径
    * @param handler 路由处理器
    */
    public func delete(path: String, handler: EasyHandler): EasyRoute 

    /**
    * 添加HEAD方法处理器
    *
    * @param path 路由路径
    * @param handler 路由处理器
    */
    public func head(path: String, handler: EasyHandler): EasyRoute 

    /**
    * 添加OPTIONS方法处理器
    *
    * @param path 路由路径
    * @param handler 路由处理器
    */
    public func options(path: String, handler: EasyHandler): EasyRoute 

    /**
    * 添加PATCH方法处理器
    *
    * @param path 路由路径
    * @param handler 路由处理器
    */
    public func patch(path: String, handler: EasyHandler): EasyRoute 

    /**
    * 添加过滤器
    *
    * @param filter 过滤器实例
    */
    public func filter(filter: EasyFilter): EasyRoute 

    /**
    * 启动服务
    *
    * @param host Host
    * @param port 端口
    */
    public func listen(host: String, port: UInt16): Unit
}

```

#### EasyContext

上下文

```cj
public class EasyContext {

    /**
    * 构造函数
    *
    * @param ctx Http请求上下文
    * @param config 缓存配置
    */
    public EasyContext(ctx: HttpContext, config: EasyConfig) 

    /**
    * 请求实例
    */
    public prop req: EasyRequest 

    /**
    * 响应实例
    */
    public prop res: EasyResponse

    /**
    * 日志实例
    */
    public prop logger: Logger 

    /**
    * 用户自定义数据键集
    */
    public prop userDataKeys: HashSet<String> 

    /**
    * 设置用户自定义数据
    *
    * @param key 键
    * @param value 值
    */
    public func setUserValue(key: String, value: Any) 

    /**
    * 获取用户自定义数据
    *
    * @param key 键
    * 
    * @return 值
    */
    public func getUserValue(key: String): ?Any 

    /**
    * 订阅路由响应
    *
    * @param hook 路由响应钩子
    */
    public func subscribeResponse(hook: ResponseHook): Unit 
}

```


#### EasyConfig

路由配置

```cj
public class EasyConfig {
    /**
    * 自定义缓存目录
    */
    public var tempDir: String = "./easy_temp"

    /**
    * 路由前缀路径
    */
    public mut prop basePath: String
}

```

#### EasyRequest

请求实例

```cj
public class EasyRequest <: Resource {
    /**
    * 请求路径
    */
    public prop url: URL 

    /**
    * 请求方法
    */
    public prop method: String 

    /**
    * 请求远程地址
    */
    public prop remoteAddr: String 

    /**
    * 请求头
    */
    public prop headers: HttpHeaders 

    /**
    * 请求尾
    */
    public prop trailers: HttpHeaders 

    /**
    * 请求体大小
    */
    public prop bodySize: Int64 

    /**
    * 请求体是否为空
    */
    public prop isEOF: Bool 

    /**
    * 请求参数
    */
    public prop params: EasyParams 

    /**
    * multipart/form-data 数据实例
    */
    public prop multipartForm: MulitpartForm 

    /**
    * 是否为 multipart/form-data
    */
    public prop isFormData: Bool 

    /**
    * 是否为 application/x-www-form-urlencoded
    */
    public prop isURLEncoded: Bool 

    /**
    * 请求路径参数键集
    */
    public prop pathValueKeys: HashSet<String> 

    /**
    * 请求参数键集
    */
    public prop paramKeys: HashSet<String> 

    /**
    * 读取请求体
    *
    * @return 请求体字节数组
    */
    public func readBody(): Array<Byte> 

    /**
    * 获取请求路径参数值
    *
    * @param key 键
    *
    * @return 请求路径参数值
    */
    public func getPathValue(key: String): ?Any 
}
```

#### EasyParams

请求参数实例

```cj
public class EasyParams <: Resource {
    /**
    * 请求参数数量
    */
    public prop size: Int64 

    /**
    * 请求参数所有键集
    */
    public prop keysets: HashSet<String>

    /**
    * 获取请求参数
    * 
    * @param key 键
    * 
    * @return 值
    */
    public func get(key: String): ?EasyParamsValues
}
```

#### EasyParamsValue

```cj
public class EasyParamsValue {
    /**
    * 值
    */
    public let value: String

    /**
    * 是否没有值，即为None/null
    */
    public let noValue: Bool
}
```

#### EasyParamsValue

```cj
public class EasyParamsValues <: Resource {
    /**
    * 值数组
    */
    public prop values: Array<EasyParamsValue>

    /**
    * 获取第一个值
    * 
    * @return 值
    */
    public func getFirst(): ?String

    /**
    * 获取最后一个值
    * 
    * @return 值
    */
    public func getLast(): ?String 
}
```

#### EasyUserData

```cj
public class EasyUserData <: Resource {
    /**
    * 用户自定义数据数组
    */
    public prop datas: HashMap<String, Any>

    /**
    * 数据键集
    */
    public prop keysets: HashSet<String> 

    /**
    * 设置自定义数据
    *
    * @param key 键
    * @param value 值
    */
    public func set(key: String, value: Any): Unit

    /**
    * 获取自定义数据
    *
    * @param key 键
    * 
    * @return 值
    */
    public func get(key: String): ?Any 
}
```

#### EasyResponse

```cj
public class EasyResponse <: Resource {
    /**
    * 响应码
    */
    public mut prop statusCode: UInt16 

    /**
    * 响应头信息
    */
    public prop headers: Map<String, String> 

    /**
    * 将文本写入响应体
    *
    * @param str 文本
    */
    public func writeBody(str: String): EasyResponse 

    /**
    * 将字节数组写入响应体
    *
    * @param buf 字节数组
    */
    public func writeBody(buf: Array<Byte>): EasyResponse 

    /**
    * 覆盖响应体
    *
    * @param str 文本
    */
    public func overwriteBody(str: String): EasyResponse 

    /**
    * 覆盖响应体
    *
    * @param buf 字节数组
    */
    public func overwriteBody(buf: Array<Byte>): EasyResponse 

    /**
    * 以JSON方式写入响应体
    *
    * @param str 文本
    */
    public func writeJSON(str: String): EasyResponse 

    /**
    * 以JSON方式写入响应体
    *
    * @param buf 字节数组
    */
    public func writeJSON(buf: Array<Byte>): EasyResponse 

    /**
    * 以流方式写入响应体
    *
    * @param input 输入流
    */
    public func writeStream(input: InputStream): EasyResponse 

    /**
    * 添加响应头
    *
    * @param key 键
    * @param value 值
    */
    public func addHeader(key: String, val: String): EasyResponse 
    
    /**
    * 设置响应体
    *
    * @param key 键
    * @param value 值
    */
    public func setHeader(key: String, val: String): EasyResponse 

    /**
    * 删除响应头
    *
    * @param key 键
    */
    public func delHeader(key: String): EasyResponse 

    /**
    * 获取响应体
    *
    * @return 响应体字节数组
    */
    public func readBody(): Array<Byte>
}
```

## 案例

### 项目实践

- [开源仓颉组织官网后端](https://gitcode.com/OpenCangjieCommunity/official-backend)

- [网络应用开发框架](https://gitcode.com/changeden/easyframework)

### API
```cj
package demo

import easyapi.route.*
import easyapi.filter.*
import easyapi.macros.*
import log.*

@EasyApiMain
main(): Int64 {
    let router = getRouter()
    router.config.basePath = "/api"
    router.logger.level = LogLevel.DEBUG
    router.config.tempDir = './temp'

    @FilterMapping(OtherFilter())

    router.listen("0.0.0.0", 8080)

    return 0
}

@FilterMapping
class OtherFilter <: EasyFilter {
    public func filter(ctx: EasyContext): Bool {
        @Debug("OtherFilter")

        ctx.subscribeResponse({
            ctx => @Debug("OtherFilter::onResponse ${String.fromUtf8(ctx.res.readBody())}")
        })
        true
    }

    public func order(): Int64 {
        1
    }
}

@RouterGroup["/test"](
    @GetMapping["/"]
    func index(ctx: EasyContext): Unit {
        let v = ctx.req.params.get("check")
        if (let Some(p) <- v) {
            @Debug("${p.getFirst()}")
        } else {
            @Debug("index")
        }
        ctx.res.writeBody("index")
    }
    
    @RouterGroup["/hello/"](
        @PostMapping["/"+":name"]
        func hello(ctx: EasyContext): Unit {
            let name = ctx.req.getPathValue("name")

            let params = ctx.req.params

            if (let Some(n) <- name) {
                @Debug("${n}")
                let date = params.get("date")
                ctx.res.writeBody("hello world, ${n}, since ${date?.getFirst()}")
            } else {
                @Debug("hello")
                ctx.res.writeBody("hello world")
            }
        }
    )

    @PostMapping["/file/upload/image"]
    func uploadImage(ctx: EasyContext): Unit {
        @Debug("uploadImage ${ctx.req.bodySize}")

        let form = ctx.req.multipartForm
        for ((key, values) in form.values) {
            @Debug("${key} = ${values}")
        }
        let fileReadBuffer = Array<Byte>(30, repeat: 0)
        for ((key, files) in form.files) {
            for (file in files) {
                try (f = file.open()) {
                    let count = f.read(fileReadBuffer)
                    @Debug("${key} read_count: ${count} bytes: ${fileReadBuffer[..count]}")
                }
            }
        }
        ctx.res.writeBody("uploadImage")
    }
)

```
