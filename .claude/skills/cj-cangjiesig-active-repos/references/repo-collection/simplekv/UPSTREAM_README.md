<div align="center">
<h1>simplekv</h1>
</div>
<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v1.1.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-HOS/Cloud-brightgreen" style="display: inline-block;" />
</p>



## 介绍

simplekv 是一个基于 cangjie 标准库和自定义模块（ random_access_file_cj）实现的高性能、简洁的键值存储库。它支持高效的查找、插入和删除操作，同时可以对数据进行排序，支持范围扫描和按前缀查询等操作，尤其适合中小规模的存储场景。

### 项目特性

- **高性能**：查找、插入和删除性能媲美哈希表。 
- **多功能**：支持按键值排序，范围扫描，前缀查询等操作。
- **轻量级**：短小精悍的代码库，易于理解和维护。
- **并发安全**：可在多协程环境中安全使用。
- 本项目参考了[recoilme/pudge](https://github.com/recoilme/pudge)部分思路


## 项目架构

架构图文说明，包括模块说明、架构层次等详细说明。

### 源码目录

```shell
.
├── README.md             #整体介绍
├── doc                   #文档目录，包括设计文档，API接口文档等
│   ├── design.md         #设计文档
│   └── feature_api.md    #特性接口文档
├── src                   #源码目录
│   ├── simple_kv_cmd.cj		#命令类，代表一个键值对的存储信息 
│   ├── simple_kv_config.md		#配置类，用于配置数据库参数
│   ├── simple_kv_db.md			#数据库类，代表一个数据库实例
│   ├── simple_kv_manager.md	#管理类，用于管理数据库
│   └── simple_kv_util.md		#工具类
└── test                  #测试代码目录（这一部分单独成一个项目：simplekv_test）
    ├── HLT
    └── LLT
```

测试代码地址：[simple_kv_test](https://gitcode.com/leaveWhite9088/simplekv_test)

### 接口说明

主要类和函数接口说明如下，详见 [API](./doc/feature_api.md)

#### SimpleKVManager类

```cangjie
/** 打开或创建一个数据库连接。
     *
     * @param f   数据库文件名或路径，用于标识数据库。
     * @param cfg 数据库连接配置，若为 None 则使用默认配置。
     * @return 数据库连接实例，返回的对象是一个 SimpleKVDb 类型。
     * @throws Exception 如果数据库连接创建失败，则抛出异常。
     */
    public func open(f: String, cfg: ?SimpleKVConfig): SimpleKVDb
```

```cangjie
/** 关闭数据库连接并释放相关资源。
     *
     * @param f   数据库文件名或路径，用于标识数据库。
     */
    public func close(f: String): Unit
```

```cangjie
/** 关闭并删除指定的数据库文件。
     *
     * @param file 数据库文件名
     * @throws Exception 如果以 file 为名的数据库不存在，则抛出异常。
     */
    public func deleteFile(f: String): Unit
```

```cangjie
/** 获取数据库中键的数量。
     *
     * @param f 数据库名称
     * @return 键的数量
     */
    public func count(f: String): Int64
```

```cangjie
/** 获取所有键，支持分页和排序。
     *
     * 注意：由于数据库中可能存在各种类型的 key，所以这里的返回值以 Byte 数组的方式直接呈现，不进行转化
     *
     * @param f 数据库名称
     * @param from 键的起始值，可以是字节数组或字符串，支持通配符
     * @param limit 每次查询的最大键数量
     * @param offset 偏移量，表示从哪个位置开始查询
     * @param asc 排序方式，`true` 表示升序，`false` 表示降序
     * @return 返回符合条件的键的二维字节数组
     */
    public func keys<T>(f: String, from: ?T, limit: Int64, offset: Int64, asc: Bool): Array<String> where T <: Serializable<T>
```

#### SimpleKVDb类

```cangjie
/** 向数据库中插入一条记录。
     *
     * @param key 要插入的记录的键
     * @param value 要插入的记录的值
	 */
	public func set<keyType, valueType>(key: keyType, value: valueType): Unit where keyType <: Serializable<keyType>
```

```cangjie
/** 以 Int64 的数据类型从数据库读取数据。
     *
     * @param key 要读取数据的键
     * @return 读取到的数据
     */
    public func getInt64<keyType>(key: keyType): Int64 where keyType <: Serializable<keyType>
```

```cangjie
/** 以 Float64 的数据类型从数据库读取数据。
     *
     * @param key 要读取数据的键
     * @return 读取到的数据
     */
    public func getFloat64<keyType>(key: keyType): Float64 where keyType <: Serializable<keyType>
```

```cangjie
/** 以 Bool 的数据类型从数据库读取数据。
     *
     * @param key 要读取数据的键
     * @return 读取到的数据
     */
    public func getBool<keyType>(key: keyType): Bool where keyType <: Serializable<keyType>
```

```cangjie
/** 以 String 的数据类型从数据库读取数据。
     *
     * @param key 要读取数据的键
     * @return 读取到的数据
     */
    public func getString<keyType>(key: keyType): String where keyType <: Serializable<keyType>
```

```cangjie
/** 从数据库读取非基础类型数据。
     *
     * 这个方法用于读取Json、Array等形式的数据
     *
     * @param key 要读取数据的键
     * @return 读取到的数据
     */
    public func getOther<keyType>(key: keyType): String where keyType <: Serializable<keyType>
```

```cangjie
/** 以 Array<Byte> 的数据类型从数据库读取数据。
     *
     * @param key 要读取数据的键
     * @return 读取到的数据
     */
    public func getByteArray<keyType>(key: keyType): Array<Byte> where keyType <: Serializable<keyType>
```

```cangjie
/** 以自定义类型的数据类型从数据库读取数据。
     *
     * @param key 要读取数据的键
     * @return 读取到的数据
     */
    public func getSerializable<keyType, valueType>(key: keyType): valueType where keyType <: Serializable<keyType>
```

```cangjie
/** 以自定义类型的数据类型从数据库读取数据。
     * 
     * 这个方法是为了简化常用类型的使用，避免反复书写泛型
     *
     * @param key 要读取数据的键
     * @return 读取到的数据
     */
    public func getSerializable<valueType>(key: Any): valueType where valueType <: Serializable<valueType>
```

## 使用说明

### 编译构建

描述具体的编译过程：

```shell
cjpm update
cjpm build
```

### 功能示例
#### 配置和打开数据库功能示例

功能示例描述: 这个示例展示了如何配置数据库并打开它。演示了如何处理错误以及如何删除数据库文件。

示例代码如下：

```cangjie
main() {
	// 配置
	let config = SimpleKVConfig()
 	config.fileMode = "0777"
    config.dirMode = "0777"
	
	// 打开数据库
	let F: String = "./testDir/testDb.db"
	let db = SimpleKVManager.default.open(F, config)
	
	// 删除数据库文件
	db.deleteFile()
}
```

#### 设置和获取键值功能示例

功能示例描述: 此示例展示了如何在数据库中设置键值对，并通过键获取存储的值。

示例代码如下：

```cangjie
main() {
	// 打开数据库
	let F: String = "./testDir/testDb.db"
	let db = SimpleKVManager.default.open(F, config)
	
	// 设置键值对
	db.set(1, true)
	
	// 获取键值对
	let v = db.getBool(1)
	
	// 删除数据库文件
	SimpleKVManager.default.deleteFile(F)
	
	// 打印结果
	println(v)
}
```

执行结果如下：

```shell
true
```

#### 并发操作 - 异步写入和读取功能示例

功能示例描述: 这个示例演示了如何进行并发的数据库写入和读取操作。我们使用 spawn来执行异步写入和读取，并使用 `.get()` 来确保所有操作完成。

示例代码如下：

```cangjie
main() {
	// 打开数据库
	let file = "./testDir/async.db"
	SimpleKVManager.default.deleteFile(file)
	
	// 写入任务
    for(i in 1..=len){
        spawn { =>
            let index = i
            let k = "Key:" + index.toString()
            let v = "Val:" + index.toString()
            db.set<String, String>(k, v)
        }
    }
    
    // 这里模拟写入已完成
    sleep(Duration.second*2)
    
    // 读取任务
    for(i in 1..=len){
        // 模拟生产者消费者
        let fut = spawn { =>
            let index = i
            let k = "Key:" + index.toString()
            let v = "Val:" + index.toString()
            let b = db.getString(k)
        }
        fut.get()
    }
    
    // 这里模拟读取已完成
    sleep(Duration.second*2)
    
    // 删除数据库文件
	SimpleKVManager.default.deleteFile(F)
}
```

#### 获取数据库键功能示例

功能示例描述: 该示例展示了如何获取数据库中的键，并根据不同排序条件（升序、降序等）进行筛选。

示例代码如下：

```cangjie
main() {
	// 打开数据库
	let fKeys = "./testDir/keys.db"
	let db = SimpleKVManager.default.open(fKeys, None)
	
	// 插入键值对
    for(i in 22..0: -1){
    	let k: String = i.format("02")
        let v: String = "Val:" + i.toString()
        db.set<String, String>(k, v)
	}
	
	// 升序检索
    let res = db.keys<String>(None, 0, 0, true)
    var s = ""
    for(r in res){
    	s += r.toString()
    }
    println(s)

	// 升序偏移和限制
    let reslimit  = db.keys<String>(None, 2, 2, true)
    s = ""
    for(r in reslimit){
    	s += r.toString()
    }
    println(s)

    // 从特定字节开始的降序检索
    let resfromdesc = db.keys<String>("10", 2, 2, false)
    s = ""
    for(r in resfromdesc){
        s += r.toString()
    }
    println(s)

    // 按前缀查询
    let respref = db.keys<String>("2*", 4, 0, false)
    s = ""
    for(r in respref){
        s += r.toString()
    }
    println(s)

    // 按前缀升序查询所有
    let resprefasc2 = db.keys<String>("1*", 0, 0, true)
    s = ""
    for(r in resprefasc2){
        s += r.toString()
    }
    println(s)
    
    // 删除数据库文件
    db.deleteFile()
}
```

执行结果如下：

```shell
01020304050607080910111213141516171819202122	// 升序检索
0304	// 升序偏移和限制
0706	// 从特定字节开始的降序检索
10111213141516171819	// 按前缀升序查询所有
```

#### 数据库计数器功能示例

功能示例描述: 展示了如何使用计数器来递增某个键的值。通过 `Counter` 方法，可以方便地进行自动递增操作。

示例代码如下：

```cangjie
main() {
	// 打开数据库
	let fTestCnt = "./testDir/TestCnt.db"
	let db = SimpleKVManager.default.open(fTestCnt, None)
	
	// 计数器
	let key = "postcounter"
    var counter = 0
    for(_ in 0..10){
        counter = db.counter<String>(key, 1)
    }
    println(counter)
    
    // 删除数据库文件
    db.deleteFile()
}
```

执行结果如下：

```shell
10
```

#### Lazy设置和获取键值功能示例

功能示例描述: 此示例展示了如何用Lazy的方式在数据库中设置键值对，并通过键获取存储的值。

示例代码如下：

```cangjie
main() {
	// 设置键值
	let F: String = "./testDir/testDb.db"
    SimpleKVManager.default.set<Int64, Int64>(F, 2, 42)
	
	// 关闭数据库
    SimpleKVManager.default.closeAll()
	
	// 取出键值
    let val = SimpleKVManager.default.getInt64(F, 2)
    println(val)
	
	// 删除数据库文件
    SimpleKVManager.default.deleteFile(F)
}
```

执行结果如下：

```shell
42
```

## 开源协议
本项目基于 MIT License

## 参与贡献

欢迎给我们提交PR，欢迎给我们提交Issue，欢迎参与任何形式的贡献。

本项目committer：[@leaveWhite9088](https://gitcode.com/leaveWhite9088)

This project is supervised by [@zhangyin_gitcode](https://gitcode.com/zhangyin_gitcode) (HUAWEI Developer Advocate).

![img](https://raw.gitcode.com/SIGCANGJIE/homepage/attachment/uploads/9b648c07-efc2-4eb3-b02f-eab18c77beea/devadvocate.png)