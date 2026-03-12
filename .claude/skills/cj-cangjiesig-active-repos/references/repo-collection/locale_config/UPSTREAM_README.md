# locale_config
一个强大的本地化配置管理系统，支持 RFC4647 和 RFC5646 标准的语言范围处理。
## 功能
- 处理 RFC4647 和 RFC5646 标准的语言范围
- 封装平台本地化api，提供统一接口获取
- 管理复杂多类别本地化配置
## 项目结构
```tree
├── CHANGELOG.md    // changelog
├── cjpm.toml
├── docs            // 文档主题
│   ├── header.html
│   └── theme
├── Doxyfile        // 文档生成配置
├── LICENSE         // 许可证
├── README.md
└── src
    ├── cfg.toml
    ├── darwin.cj   // darwin平台代码
    ├── windows.cj  // windows平台代码
    ├── lib.cj      // 主要代码
    ├── lib_test.cj
    └── unix.cj     // Unix-like平台相关代码
```

## 版本
你可以在 Gitcode 的发行版页面获取对应版本的 cjpm.toml 配置。

## 文档
本项目所有公开API均提供Doxygen风味文档注释，请自行阅读源码或查看
[在线文档（已过时）](https://docs.open-cj.org/locale_config/)。~~亦可通过`cjdoc`自行生成文档。~~
### ~~使用 cjdoc 生成文档~~
> [!WARNING]
> cjdoc 已被弃用。

下载本项目后：
```
git submodule update --init docs/theme
cjdoc ./Doxyfile
```
文档将生成在`docs/html`下。
## 使用
本项目大部分API在任意平台均可用。特别的，暂时仅支持在*Unix-like*平台上获取系统本地化设置。
### 手动设置平台特征
默认情况下，本项目会自动识别平台特征。但可能在特定情况下失效，或者与实际特征不符。你可以通过设置如下*feature*进行手动配置：
```
locale_platform = "unix" // 可用值：unix windows darwin
```
## 参与本项目
本项目使用MIT许可证。

committer: yms_hi