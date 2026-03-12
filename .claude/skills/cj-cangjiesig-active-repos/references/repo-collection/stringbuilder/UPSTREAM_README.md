<div align="center">
<h1>stringbuilder</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.2.1-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/build-pass-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/project-open-brightgreen" style="display: inline-block;" />
</p>

## <img alt="" src="./doc/assets/readme-icon-introduction.png" style="display: inline-block;" width=3%/>简介

更自由、更强大的StringBuilder工具类。

### 特性

- 🚀 支持写入、插入字符串数据

- 🚀 支持写入、插入原始字节数组数据

- 🚀 支持查找、分割、替换、克隆数据

- 💪 支持删除某个位置，某个区间的字符串数据

- 💪 支持并发包

## <img alt="" src="./doc/assets/readme-icon-framework.png" style="display: inline-block;" width=3%/> 架构

### 源码目录：

```shell
.
├── README.md
├── doc
│   ├── assets     
│   ├── cjcov
│   ├── design.md
│   ├── feature_api.md
├── src
│   ├── core
│   │   └── buffer.cj
│   │   └── types.cj
│   │   └── util.cj
│   ├── concurrent
│   │   └── concurrent_builder.cj
│   └── builder.cj
└── test   
    ├── HLT
    ├── LLT
    └── UT
```

- `doc` 存放库的设计文档、提案、库的使用文档、LLT 用例覆盖报告
- `src` 存放库源码的目录
- `test` 存放测试用例，包括 HLT 用例、LLT 用例和 UT 用例

### 类和接口说明：

详情见 [API](./doc/feature_api.md)

## <img alt="" src="./doc/assets/readme-icon-compile.png" style="display: inline-block;" width=3%/> 使用说明

### 编译

```shell
cpm build
```

### 功能示例

#### zlib 使用示例

```cangjie
import stringbuilder.*

main(): Int64 {
    let str = builder.StringBuilder()
    str.append(b"hello world").append([',', ' ']).append("hello 仓颉开发者!")
    println("1: ${str}") // 1: hello world, hello 仓颉开发者!

    str.remove(str.runeSize - 2)
    println("2: ${str}") // 2: hello world, hello 仓颉开发!

    str.remove(str.runeSize - 3, str.runeSize - 1)
    println("3: ${str}") // 3: hello world, hello 仓颉!

    str.insert(str.runeSize - 1, "开发").insert(str.runeSize - 1, '者')
    println("4: ${str}") // 4: hello world, hello 仓颉开发者!

    str.removeLast()
    println("5: ${str}") // 5: hello world, hello 仓颉开发者

    return 0
}
```

运行结果如下：

```cangjie
1: hello world, hello 仓颉开发者!
2: hello world, hello 仓颉开发!  
3: hello world, hello 仓颉!      
4: hello world, hello 仓颉开发者!
5: hello world, hello 仓颉开发者 
```


## <img alt="" src="./doc/assets/readme-icon-contribute.png" style="display: inline-block;" width=3%/> 参与贡献

[穗鸿仓](https://gitee.com/organizations/suihongcang)

欢迎给我们提交 PR，欢迎给我们提交 issue，欢迎参与任何形式的贡献。
