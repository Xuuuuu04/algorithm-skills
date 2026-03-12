# multipart

`multipart/form-data`请求体解析工具。

## API

### MulitpartReader

Multipart解析器

```cj
public class MulitpartReader <: Resource {
    /**
    * 创建Multipart解析器
    * 
    * @param input 输入流，需实现 InputStream
    * @param boundary Form-Data分割线，需自行解析请求头中的 Content-Type
    */
    public init(input: InputStream, boundary: Array<Byte>) {}

    /**
    * 创建Multipart解析器
    * 
    * @param input 输入流，需实现 InputStream
    * @param boundary Form-Data分割线，需自行解析请求头中的 Content-Type
    * @param maxMemory 最大内存缓存，超出则将文件写入至临时目录
    */
    public init(input: InputStream, boundary: Array<Byte>, maxMemory: Int64) {}

    /**
    * 获取解析后的Form-Data实例
    */
    public prop form: MulitpartForm
}
```

### MulitpartForm

Form-Data实例

```jc
public class MulitpartForm <: Resource {
    /**
    * 获取Form-Data中Text部分
    */
    public prop values: Map<String, Array<String>>

    /**
    * 获取Form-Data中File部分
    */
    public prop files: Map<String, Array<MultipartFile>>
}
```

### MultipartFile

文件实例

```jc
public class MultipartFile <: Resource {
    /**
    * 获取文件名
    */
    public let filename: String

    /**
    * 获取MIME信息
    */
    public let header: MIMEHeader

    /**
    * 获取文件大小
    */
    public prop size: Int64

    /**
    * 开启文件读取流
    */
    public func open(): MultipartFileStream {}
}
```

###

文件读取流

```cj
public class MultipartFileStream <: InputStream & Seekable & Resource {
    /**
    * 返回当前流中的总数据量
    */
    public prop length: Int64 

    /**
    * 返回当前光标位置
    */
    public prop position: Int64 

    /**
    * 返回当前流中未读的数据量
    */
    public prop remainLength: Int64 

    /**
    * 移动光标到指定的位置
    */
    public func seek(sp: SeekPosition): Int64 {}

    /**
    * 从输入流中读取数据放到 buffer 中
    */
    public func read(buffer: Array<Byte>): Int64 {}
}
```

## 使用方式

```cj
package test

import multipart.*

main(): Int64 {
    let boundaryString = "--------------------------761903867315179375835300"
    try (f = File("./testdata/formData", OpenMode.Read)) {
        try (reader = MulitpartReader(f, boundaryString.toArray(), 100)) {
            let form = reader.form
            for ((k, v) in form.values) {
                println("${k}=${v}")
            }
            for ((k, v) in form.files) {
                for (f in v) {
                    println("${k}=${f.filename} ${f.size}")
                    try (r = f.open()) {
                        let buf = Array<Byte>(10, {_ => 0})
                        let l = r.read(buf)
                        println("readCount=${l} buf=${buf}")
                    }
                }
            }
        }
    }
    return 0
}
```