<div align="center">
<h1>whatlang4cj</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.1-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjcov-99.2%25-brightgreen" style="display: inline-block;" />
</p>

## 介绍
whatlang4cj 是一个基于Cangjie标准库实现的快速高效的自然语言检测工具。它能够自动检测一段文本的语言类型及文字体系。

项目参考自：https://github.com/abadojack/whatlanggo

### 项目特性

- **双层检测模型**
  - **多语言识别**：支持[81种语言](./SUPPORTED_LANGUAGES.md)的检测，覆盖全球主流语种。
  - **文字体系判定**：可自动识别文本使用的书写系统，包括拉丁文字、西里尔文字、汉字等多种文字体系。
- **可信度评估**：能够输出检测结果的置信度分数，帮助评估检测结果质量。
- **黑白名单控制**：可限定检测范围，提升特定场景识别准确率。
- **零配置开箱即用**：内置预训练语言模型，无需额外数据文件或网络请求。

### 项目计划

1. 2025年4月发布 1.0.0 版本

2. 对项目进行后续维护

## 项目架构

- `doc` 文档目录，用于存放接口文档
- `src` 源代码目录，用于存放源代码
- `src/test` 测试文件目录，用于存放测试用例


### 源码目录

```shell
.
├── doc                         # 文档目录
│   └── feature_api.md          # 特性接口文档
├── src                         # 源码目录
│   └── constants.cj            # 算法参数常量定义
│   └── detect.cj               # 语言检测核心逻辑
│   └── info.cj                 # 检测结果数据结构定义
│   └── lang.cj                 # 语言类型定义
│   └── options.cj              # 黑白名单配置
│   └── script.cj               # 文字体系检测逻辑
│   └── trigrams.cj             # 三元组操作实现
│   └── utils.cj                # 工具函数
│   └── test                    # 测试代码目录
│       └── detect_test.cj      # 语言检测相关功能测试
│       └── lang_test.cj        # 语言类型相关功能测试
│       └── script_test.cj      # 文字体系检测功能测试
│       └── trigrams_test.cj    # 三元组相关功能测试
│       └── utils_test.cj       # 工具函数相关功能测试
│   └── unicode                 # 字符库目录
│       └── graphic.cj          # 判断字符属性
│       └── letter.cj           # 字符范围表示
│       └── tables.cj           # 文字体系定义
├── cjpm.toml                   # 项目配置文件
├── CHANGLOG.md                 # 变更日志
├── README.md                   # 项目介绍
├── SUPPORTED_LANGUAGES.md      # 支持的检测语言列表
└── LICENSE                     # 许可证
```

### 接口说明

主要类和函数接口说明，详见 [API](./doc/feature_api.md)


## 使用说明

### 依赖引入

```shell
[dependencies]
  whatlang4cj = { git = "https://gitcode.com/pionneer/whatlang4cj.git" }
```

### 编译构建

```shell
cjpm update
cjpm build
```

### 功能示例

#### 语言检测

使用 whatlang4cj 库的核心函数 detect 可以对给定文本进行语言检测，该函数会返回检测到的语言类型、文字体系以及检测结果的置信度分数。

示例代码如下：
```cangjie
import whatlang4cj.*

main(): Int64 {
    let text1 = "Where there is a will,there is a way."
    let info1 = detect(text1)
    println("language:${info1.lang}, script:${Scripts[info1.script]}, confidence:${info1.confidence}")

    let text2 = "你好，世界！"
    let info2 = detect(text2)
    println("language:${info2.lang}, script:${Scripts[info2.script]}, confidence:${info2.confidence}")

    let text3 = "Русский язык имеет важное место в научном мире и культуре."
    let info3 = detect(text3)
    println("language:${info3.lang}, script:${Scripts[info3.script]}, confidence:${info3.confidence}")

    return 0
}
```

执行结果如下：

```shell
language:English, script:Latin, confidence:1.000000
language:Chinese, script:Han, confidence:1.000000
language:Russian, script:Cyrillic, confidence:1.000000
```

#### 黑白名单控制

使用黑白名单配置，可精准限定语言检测范围。其中，白名单用于指定仅检测的特定语言，缩小检测范围；黑名单则可排除某些语言，避免误检。

```cangjie
import std.collection.*
import whatlang4cj.*

main(): Int64 {

    // 白名单控制，限定检测语言
    let text1 = "Mi ne scias!"
    let options1 = Options(whiteList: HashMap<Lang, Bool>([(Epo, true), (Ukr, true)]))
    let info1 = detectWithOptions(text1, options1)

    println("language:${info1.lang}, script:${Scripts[info1.script]}, confidence:${info1.confidence}")

    // 黑名单控制，排除特定语言
    let text2 = "האקדמיה ללשון העברית"
    let options2 = Options(blackList: HashMap<Lang, Bool>([(Ydd, true)]))
    let info2 = detectWithOptions(text2, options2)

    println("language:${info2.lang}, script:${Scripts[info2.script]}, confidence:${info2.confidence}")

    return 0
}
```

执行结果如下：
```shell
language:Esperanto, script:Latin, confidence:1.000000
language:Hebrew, script:Hebrew, confidence:1.000000
```
## 约束与限制

- 在下述版本验证通过：
```shell
Cangjie Version: 0.53.18
```

- 本项目基于trigram模型，过短文本检测效果不佳。
## 开源协议

本项目基于 [Apache License 2.0](./LICENSE) ，请自由的享受和参与开源。

## 参与贡献

本项目由 [SIGCANGJIE / 仓颉兴趣组](https://gitcode.com/SIGCANGJIE) 实现并维护。技术支持和意见反馈请提Issue。

欢迎给我们提交PR，欢迎参与任何形式的贡献。

本项目committer：[@pionneer](https://gitcode.com/pionneer)

This project is supervised by [@zhangyin_gitcode](https://gitcode.com/zhangyin_gitcode) (HUAWEI Developer Advocate).

![](https://raw.gitcode.com/SIGCANGJIE/homepage/attachment/uploads/9b648c07-efc2-4eb3-b02f-eab18c77beea/devadvocate.png)