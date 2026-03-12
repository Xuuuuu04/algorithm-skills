# 扩展库速查 (stdx-map)

> **用途**: 仅当题目明确需要 JSON/URL/加密/HTTP/序列化等功能时才引入 stdx。
> **竞赛场景**: 算法题极少需要 stdx，但部分应用类题目可能涉及。

---

## 一、stdx.encoding.json

**import**: `import stdx.encoding.json.*`

### 核心类层次
```
JsonValue (abstract base)
├── JsonObject   — { "key": value }
├── JsonArray    — [ v1, v2, ... ]
├── JsonString   — "text"
├── JsonInt      — 整数
├── JsonFloat    — 浮点数
├── JsonBool     — true/false
└── JsonNull     — null
```

### 高频 API

| 操作 | 代码 |
|------|------|
| 解析 JSON 字符串 | `let jv = JsonValue.fromStr(jsonStr)` |
| 转回字符串 | `jv.toStr()` 或 `jv.toString()` |
| 创建对象 | `JsonObject().put("key", JsonInt(42))` |
| 创建数组 | `JsonArray().add(JsonInt(1)).add(JsonInt(2))` |
| 获取字段 | `jobj.get("key")` → `Option<JsonValue>` |
| 获取数组元素 | `jarr.get(0)` → `Option<JsonValue>` |
| 获取所有项 | `jarr.getItems()` → `ArrayList<JsonValue>` |
| 类型判断 | `jv.kind()` → `JsonKind` 枚举 |
| 转 Int64 | `(jv as JsonInt).getValue()` |
| 转 String | `(jv as JsonString).getValue()` |
| 转 Float64 | `(jv as JsonFloat).getValue()` |
| 转 Bool | `(jv as JsonBool).getValue()` |

### 接口 ToJson
```cangjie
interface ToJson {
    func toJson(): JsonValue
    static func fromJson(jv: JsonValue): Self
}
```

### 快速示例
```cangjie
import stdx.encoding.json.*

let s = """{"name":"Alice","age":30}"""
let jv = JsonValue.fromStr(s)
let obj = jv as JsonObject
let name = (obj.get("name").getOrThrow() as JsonString).getValue()
println(name)  // Alice
```

---

## 二、stdx.encoding.url

**import**: `import stdx.encoding.url.*`

### 核心类

| 类 | 功能 |
|----|------|
| `URL` | URL 解析与组装 |
| `Form` | 表单 query 参数 key-value 管理 |

### URL 操作

| 操作 | 代码 |
|------|------|
| 解析 URL | `URL("https://example.com/path?q=1")` |
| 获取组件 | `.scheme`, `.host`, `.port`, `.path`, `.query`, `.fragment` |
| URL 编码 | `URL.encodeComponent(s)` |
| URL 解码 | `URL.decodeComponent(s)` |

### Form 操作

| 操作 | 代码 |
|------|------|
| 创建 | `Form()` 或 `Form("a=1&b=2")` |
| 添加 | `form.add("key", "value")` |
| 获取 | `form.get("key")` → `Option<String>` |
| 获取所有 | `form.getAll("key")` → `ArrayList<String>` |
| 克隆 | `form.clone()` |

---

## 三、stdx.encoding.base64

**import**: `import stdx.encoding.base64.*`

| 函数 | 签名 | 用途 |
|------|------|------|
| 编码 | `toBase64String(data: Array<Byte>): String` | Byte数组 → Base64字符串 |
| 解码 | `fromBase64String(data: String): Option<Array<Byte>>` | Base64字符串 → Byte数组 |

```cangjie
import stdx.encoding.base64.*
let encoded = toBase64String("Hello".toArray())
let decoded = fromBase64String(encoded)  // Option<Array<Byte>>
```

---

## 四、stdx.encoding.hex

**import**: `import stdx.encoding.hex.*`

| 函数 | 签名 | 用途 |
|------|------|------|
| 编码 | `toHexString(data: Array<Byte>): String` | Byte数组 → Hex字符串 |
| 解码 | `fromHexString(data: String): Option<Array<Byte>>` | Hex字符串 → Byte数组 |

---

## 五、stdx.crypto

### 5.1 stdx.crypto.crypto — 安全随机数 & SM4

**import**: `import stdx.crypto.crypto.*`  
**外部依赖**: OpenSSL 3

| 类 | 功能 |
|----|------|
| `SecureRandom` | 加密安全伪随机数生成器 |
| `SM4` | 国密 SM4 对称加解密 |

**SecureRandom API**:

| 方法 | 返回值 |
|------|--------|
| `nextBool()` | `Bool` |
| `nextBytes(length: Int32)` | `Array<Byte>` |
| `nextBytes(bytes: Array<Byte>)` | 原地填充 |
| `nextBits(bits: UInt64)` | `UInt64` |
| `nextFloat64()` | `Float64` [0,1) |
| `nextInt64()` | `Int64` |

### 5.2 stdx.crypto.digest — 摘要算法

**import**: `import stdx.crypto.digest.*`

| 类 | 功能 |
|----|------|
| `MD5` | MD5 摘要 |
| `SHA1` | SHA-1 摘要 |
| `SHA256` | SHA-256 摘要 |
| `SHA512` | SHA-512 摘要 |
| `SM3` | 国密 SM3 摘要 |
| `HMAC` | HMAC 消息认证码 |

**通用 Digest 用法**:
```cangjie
import stdx.crypto.digest.*
let h = MD5()
h.write("hello".toArray())
let result: Array<Byte> = h.finish()
```

### 5.3 stdx.crypto.keys — 密钥管理

| 类 | 功能 |
|----|------|
| `ECPrivateKey` / `ECPublicKey` | 椭圆曲线密钥对 |
| `RSAPrivateKey` / `RSAPublicKey` | RSA密钥对 |
| `SM2PrivateKey` / `SM2PublicKey` | SM2密钥对 |

### 5.4 stdx.crypto.x509 — X.509 证书

| 类 | 功能 |
|----|------|
| `X509Certificate` | X.509证书解析 |
| `X509CertificateRequest` | 证书请求 |

---

## 六、stdx.net.http

**import**: `import stdx.net.http.*`  
**外部依赖**: OpenSSL 3

### Client 端

```cangjie
import stdx.net.http.*

let client = ClientBuilder().build()
let req = HttpRequestBuilder()
    .method("GET")
    .url("https://example.com/api")
    .build()
let resp = client.send(req)
println(resp.status)
println(resp.body.readToEnd())
```

**核心类**:

| 类 | 功能 |
|----|------|
| `ClientBuilder` | 构建 HTTP Client |
| `Client` | 发送请求 |
| `HttpRequestBuilder` | 构建请求 |
| `HttpRequest` | 请求对象 |
| `HttpResponse` | 响应对象 |
| `HttpHeaders` | 请求/响应头 |

**Client 配置**: `httpProxy`, `httpsProxy`, `autoRedirect`, `cookieJar`, `readTimeout`, `writeTimeout`

### Server 端

```cangjie
import stdx.net.http.*

let server = ServerBuilder()
    .addr("0.0.0.0")
    .port(8080)
    .distributor(handler)
    .build()
server.serve()
```

---

## 七、stdx.net.tls

**import**: `import stdx.net.tls.*`  
**外部依赖**: OpenSSL 3

| 类 | 功能 |
|----|------|
| `TlsClientConfig` | TLS 客户端配置 |
| `TlsServerConfig` | TLS 服务端配置 |
| `TlsSocket` | TLS Socket 连接 |
| `TlsSessionContext` | TLS 会话上下文 |

---

## 八、stdx.serialization

**import**: `import stdx.serialization.*`

用于自定义类型的序列化/反序列化。核心为 `DataModel` 类层次：

```
DataModel (abstract)
├── DataModelBool
├── DataModelInt
├── DataModelFloat
├── DataModelString
├── DataModelNull
├── DataModelSeq    — 序列 (数组)
└── DataModelStruct — 结构体 (字段映射)
```

**接口**:
- `Serializable<T>`: 实现 `serialize()` 和 `deserialize()`

---

## 九、stdx.compress.zlib

**import**: `import stdx.compress.zlib.*`

提供 zlib 压缩/解压。

---

## 十、stdx.log / stdx.logger

**import**: `import stdx.log.*` 或 `import stdx.logger.*`

提供日志功能。竞赛中基本不用。

---

## 竞赛使用建议

| 场景 | 是否使用 stdx | 说明 |
|------|:---:|------|
| 纯算法题 | ❌ | 只需 std |
| 需要 JSON 解析 | ✅ | `stdx.encoding.json` |
| 需要 URL 编解码 | ✅ | `stdx.encoding.url` |
| 需要 Base64/Hex 编解码 | ✅ | `stdx.encoding.base64/hex` |
| 需要加密/哈希 | ✅ | `stdx.crypto.*` (需 OpenSSL) |
| 需要 HTTP 请求 | ✅ | `stdx.net.http` (需 OpenSSL) |
| 纯算法中的随机数 | ❌ | 用 `std.random.Random` 即可 |

> ⚠️ **警告**: stdx 中 crypto/http/tls 均依赖 OpenSSL 3 外部库。竞赛环境如果没有预装 OpenSSL，这些功能无法使用。请优先确认竞赛环境。
