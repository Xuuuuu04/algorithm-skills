# CJFltk
基于 fltk 的跨平台轻量图形化框架。

[使用指南](https://gitcode.com/Cangjie-SIG/cjfltk/discussions/1)

## 功能
- 事件循环
- GL 支持（预期）
- 轻量图形化

## 示例
见 `src/example/` 。

[温度单位转换](https://gitcode.com/Cangjie-SIG/locale_config/discussions/1)
## 使用说明
> [!NOTE]
> 仓颉运行时默认配置会导致栈溢出，可通过设置环境变量 `cjStackSize=1GB` 解决。
> 
> 参见： https://docs.cangjie-lang.cn/docs/1.0.4/user_manual/source_zh_cn/Appendix/runtime_env.html#cjstacksize

> [!NOTE]
> 仓颉运行时自带的 `libpcre-2` 可能较老，导致无法编译/运行。

## 文档
正在开发阶段，暂不专门提供文档，建议参考代码内文档注释、示例及 [Fltk Document](https://www.fltk.org/doc-1.4/index.html) 。

## 项目结构
```
├── cfltk
├── cjpm.toml
├── LICENSE
├── README.md
└── src
    ├── c        // cfltk 绑定
    ├── app
    ├── dsl     
    ├── e        // 枚举
    ├── example  // 示例
    ├── lib.cj   // 所有预期供外部使用的类均在此重导出
    ├── macros   // 开发所需要的宏
    ├── prelude  // 若干接口，以模拟 c++ 侧类
    ├── utils
    └── widget
```

## 版权
本项目使用 MIT 开源许可证分发。特别地，你需要考虑本项目依赖（`cfltk` ， `fltk` ）的分发要求。