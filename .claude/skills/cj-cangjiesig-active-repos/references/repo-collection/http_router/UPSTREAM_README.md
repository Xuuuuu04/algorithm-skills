# Restful路径解析工具

参考[https://github.com/julienschmidt/httprouter](https://github.com/julienschmidt/httprouter)解耦出`Restful路径解析部分代码`。

提供标准化的`路由注册`、`路由匹配`能力。

## API

### Node<T>

- 路由节点
- 泛型`T`为路由处理器类型

```cj
public class Node<T> {
    /**
    * 注册路由处理器
    * 
    * @param path 路由路径
    * @param handler 路由处理器
    */
    public func addHandler(path: String, handler: T): Unit

    /**
    * 获取路由处理器
    * 
    * @param path 路由路径
    * @param valueSetter 路由路径值设置函数
    * 
    * @return (路由处理器, 是否以'/'结尾)
    */
    public func getHandler(path: String, valueSetter: ?RouterValueSetter): (?T, Bool)
}
```

### RouterValueSetter

- 路由路径值设置函数

```cj
/**
* @param key 键
* @param value 值
*/
public type RouterValueSetter = (key: String, value: String) -> Unit
```

### 工具

```cj
/**
* 打印路由节点信息
* 
* @param node 路由节点
*/
public func dump<T>(node: Node<T>): Unit

/**
* 打印路由节点信息
* 
* @param node 路由节点
* @param level 起始层级
*/
public func dump<T>(node: Node<T>, level: Int64): Unit
```

## 示例

### 单节点

```
package demo

import http_router.*

main(): Int64 {
    let root = Node<DefaultHandler>()

    root.addHandler("/", index)
    root.addHandler("/hello/:name", hello)
    root.addHandler("/file/upload/image", upload)

    dump(root)

    let (indexHandler, _) = root.getHandler("/", getDefaultValueSetter("index"))
    indexHandler?()
    let (helloHandler, _) = root.getHandler("/hello/changeden", getDefaultValueSetter("hello"))
    helloHandler?()
    let (uploadHandler, _) = root.getHandler("/file/upload/image", getDefaultValueSetter("upload"))
    uploadHandler?()

    return 0
}

func getDefaultValueSetter(route: String): RouterValueSetter {
    {
        key, value => println("[${route}] key: ${key} , value: ${value}")
    }
}

type DefaultHandler = () -> Unit

func index() {
    println("index")
}

func hello() {
    println("hello")
}

func upload() {
    println("upload")
}
```

### 多节点(多种请求方法)

```
package demo

import std.collection.*

main(): Int64 {
    let rootMap = HashMap<HttpMethod, Node<DefaultHandler>>()

    registerHandler(rootMap, HttpMethod.GET, "/", index)
    registerHandler(rootMap, HttpMethod.GET, "/readme", readme)
    registerHandler(rootMap, HttpMethod.POST, "/hello/:name", hello)
    registerHandler(rootMap, HttpMethod.POST, "/file/upload/image", upload)

    for ((m, r) in rootMap) {
        println("=== ${m} ===")
        dump(r)
    }

    getHandler(rootMap, HttpMethod.GET, "/")?()
    getHandler(rootMap, HttpMethod.GET, "/readme")?()
    getHandler(rootMap, HttpMethod.POST, "/hello/changeden")?()
    getHandler(rootMap, HttpMethod.POST, "/file/upload/image")?()

    return 0
}

enum HttpMethod <: Hashable & Equatable<HttpMethod> & ToString {
    | GET
    | POST
    | PUT

    public func hashCode(): Int64 {
        match (this) {
            case GET => 1
            case POST => 2
            case PUT => 3
        }
    }

    public func toString(): String {
        match (this) {
            case GET => "GET"
            case POST => "POST"
            case PUT => "PUT"
        }
    }

    public operator func ==(that: HttpMethod): Bool {
        match ((this, that)) {
            case (GET, GET) => true
            case (POST, POST) => true
            case (PUT, PUT) => true
            case _ => false
        }
    }

    public operator func !=(that: HttpMethod): Bool {
        return !(this == that)
    }
}

func registerHandler(rootMap: HashMap<HttpMethod, Node<DefaultHandler>>, method: HttpMethod, path: String,
    h: DefaultHandler): Unit {
    if (!rootMap.contains(method)) {
        rootMap[method] = Node<DefaultHandler>()
    }
    rootMap[method].addHandler(path, h)
}

func getHandler(rootMap: HashMap<HttpMethod, Node<DefaultHandler>>, method: HttpMethod, path: String): ?DefaultHandler {
    if (rootMap.contains(method)) {
        let (handler, _) = rootMap[method].getHandler(path, getDefaultValueSetter("default"))
        return handler
    }
    None
}

func getDefaultValueSetter(route: String): RouterValueSetter {
    {
        key, value => println("[${route}] key: ${key} , value: ${value}")
    }
}

type DefaultHandler = () -> Unit

func index() {
    println("index")
}

func readme() {
    println("readme")
}

func hello() {
    println("hello")
}

func upload() {
    println("upload")
}
```