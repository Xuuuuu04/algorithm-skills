<div align="center">
<h1>CJoy</h1>
<p>A fast, extensible, lightweight and joyful Cangjie application framework.</p>
<p>一个高性能、可扩展、轻量、省心的仓颉应用开发框架。</p>
<br/>
<img alt="CJoy Logo" src="doc/imgs/logo.png" height="118" width="200" />
</div>

<p align="center">
  <img alt="Release" src="https://img.shields.io/badge/release-v0.90.0-brightgreen" />
  <img alt="Cangjie Version" src="https://img.shields.io/badge/cjc-v1.0.4-brightgreen" />
  <img alt="Code Coverage" src="https://img.shields.io/badge/cjcov-70%25+-brightgreen" />
  <img alt="State" src="https://img.shields.io/badge/state-孵化-brightgreen" />
  <img alt="Domain" src="https://img.shields.io/badge/domain-cloud-brightgreen" />
  <img alt="License" src="https://img.shields.io/badge/License-MulanPSL2-orange.svg?style=flat-square&logo=opensourceinitiative" />
  <img alt="Stars" src="https://atomgit.com/Cangjie-SIG/cjoy/star/badge.svg?style=flat-square" />
  <img alt="Top 2025" src="https://atomgit.com/Cangjie-SIG/cjoy/star/2025top.svg" />
</p>

---

## 概览

CJoy 借鉴了多种语言 Web 开源框架的设计优点，基于仓颉语言打造的高性能、高扩展性、高易用性的应用开发框架。

### 特性

在仓颉 SDK 提供的 HTTP 框架基础上进一步封装，简化后端应用开发：

| 特性 | 描述 |
|------|------|
| 🌲 **高效路由** | 基于压缩前缀树的路由管理，支持多种 Path 的高效注册与路由、路由分组 |
| 🎭 **中间件扩展** | 基于拦截器的中间件扩展能力，支持 Session 等多种能力扩展 |
| 📦 **上下文管理** | 基于 Context 的上下文管理，支持快速获取请求参数与构建 Json/Text 响应 |
| 🔧 **IoC 容器** | 基于编译宏的轻量级 IoC 框架，轻松实现依赖倒置与模块间松耦合 |
| 📝 **JSON 处理** | 基于编译宏的 JSON 序列化与反序列化，支持请求与响应消息的 JSON 直接绑定映射 |
| ✨ **自动注册** | 基于编译宏支持自动注册与参数注入请求处理函数与中间件函数、请求参数校验 |
| 🤖 **MCP 服务** | 基于编译宏支持 MCP 服务暴露工具等能力给 LLM |
| 📡 **内置能力** | 内置文件下载与上传、WebSocket、SSE 等能力 |
| 🔐 **认证支持** | 内置多种中间件，支持 Basic、Token、JWT、OAuth2 等认证 |

### 应用场景

- ♠️ **API 服务**：快速开发 API 服务并配置路由规则与管理各种资源
- ♥️ **Web 服务**：压缩前缀树高性能路由查找与文件服务，提升性能优势
- ♣️ **微服务**：路由组与内置 JSON 编译宏，轻松实现微服务各类接口分组管理与接口调用
- ♦️ **MCP 服务**：提供 AI MCP 服务组件编译宏，快速暴露 MCP 的工具等能力给 LLM

### 技术特点

| 特点 | 描述 |
|------|------|
| 🚀 **高性能** | 零反射，基于编译宏生成代码，前缀树高效路由，运行时高性能 |
| 🧩 **轻量化** | 零第三方库依赖，内置 Web 应用开发常见能力，模块化按需使用，灵活组装 |
| 🔌 **可扩展** | 提供中间件与服务扩展机制，支持对请求拦截与服务调用，丰富应用能力 |
| 😊 **易上手** | 内置多种能力，提供编译宏，简化 Web、MCP 应用开发，聚焦应用逻辑 |
| 🛠️ **多协议** | 支持 HTTP/1.1、HTTP/2、WebSocket、SSE、MCP 等协议 |

### 应用架构

<img alt="Architecture" src="doc/imgs/arch.png" />

- CJoy 提供 Server 框架、中间件、Service、通用能力
- 开箱即用，应用只需实现业务逻辑的 Handler

---

## 快速开始

> ⚠️ **注意**
>
> CJoy 支持 Windows、Linux 与 MacOS，推荐在 Linux（或 WSL）、MacOS 中运行仓颉，获得更好更快的体验。

### 环境要求

仓颉版本：`v1.0.4`

本项目依赖仓颉 stdx 包，请先下载对应版本的 stdx 包，使用说明参见 [仓颉编程语言 stdx](https://gitcode.com/Cangjie/Cangjie-STDX)。

**目录结构示例**：

```
$HOME
├── cangjie          # 仓颉 SDK 目录
└── cangjiestdx      # 新建此目录
    └── linux_x86_64_llvm  # 解压对应的 stdx 包，不同 OS 目录名称不同
```

**配置环境变量**（Linux 与 MacOS）：

```bash
# 修改用户家目录的 .bashrc 或 .zshrc（取决于采用 bash 还是 zsh）
export CANGJIE_STDX_PATH=$HOME/cangjiestdx
```

### 运行示例

克隆项目并运行示例：

```bash
git clone https://gitcode.com/Cangjie-SIG/cjoy.git
cd cjoy

# 运行测试
cjpm test

# 构建项目
cjpm build

# 运行示例
cd examples
cjpm run --name examples.tls
```

### 添加依赖

在您的项目 `cjpm.toml` 文件中添加依赖：

```toml
[dependencies]
cjoy = { git = "https://gitcode.com/Cangjie-SIG/cjoy.git", branch = "main" }
```

---

## 快速了解

```cangjie
import cjoy.*

main(): Int64 {
    // 创建 joy 实例
    let joy = Joy.default()

    // 带参路由：GET /{name}
    joy.router.get("/{name}", { ctx: JoyContext =>
        let name = ctx.getParam("name") ?? "no name"
        ctx.string("name in parameter path, name=${name}")
    })

    // 静态路由：GET /abc
    joy.router.get("/abc", { ctx: JoyContext =>
        ctx.string("static path abc")
    })

    // 启动服务
    joy.run("127.0.0.1", 18881)
    return 0
}
```

---

## 使用指导

### 快快通

- [20分钟掌握CJoy](doc/usage_guide/README.md)

### 核心功能

- [服务启动](doc/usage_guide/starter.md)
- [路由](doc/usage_guide/routing.md)
- [请求处理](doc/usage_guide/handler.md)
- [Middleware](doc/usage_guide/middleware.md)
- [路由宏](doc/usage_guide/macro.md)

### 基础服务

- [IoC 服务](doc/usage_guide/ioc.md)
- [配置服务](doc/usage_guide/config.md)
- [调度任务](doc/usage_guide/schedule.md)
- [事件总线](doc/usage_guide/eventbus.md)
- [Http 服务](doc/usage_guide/httpx.md)

### 安全认证

- [认证概述](doc/usage_guide/authentication.md)
- [Basic 认证](doc/usage_guide/authentication.md#basic认证)
- [Token 认证](doc/usage_guide/authentication.md#token认证)
- [JWT 认证](doc/usage_guide/authentication.md#jwt认证)
- [OAuth2 认证](doc/usage_guide/authentication.md#oauth2认证)

### 辅助工具

- [日志](doc/usage_guide/logger.md)
- [参数绑定](doc/usage_guide/binding.md)
- [JSON](doc/usage_guide/json.md)
- [校验](doc/usage_guide/validation.md)

### 协议扩展

- [分块传输](doc/usage_guide/mcp.md)
- [文件服务器](doc/usage_guide/fileserver.md)
- [WebSocket](doc/usage_guide/websocket.md)
- [MultiPart](doc/usage_guide/multipart.md)
- [MCP](doc/usage_guide/mcp.md)

---

## 更多示例

CJoy 内置丰富的示例与测试用例，请移步 [examples](examples/README.md)，也可以参考本项目的测试代码。

---

## 版本说明

CJoy 目前还在开发阶段，主要能力已完成开发，后续重点是提升测试覆盖率，以及扩展各类中间件与服务。在 1.0.0 版本发布之后，项目会稳定 API 与目录结构。

**版本发布方式**：采用打 Tag 的方式。

**依赖引用建议**：

```toml
# 依赖 main 分支（获取稳定最新特性）
[dependencies]
cjoy = { git = "https://gitcode.com/Cangjie-SIG/cjoy.git", branch = "main" }

# 依赖指定 tag
[dependencies]
cjoy = { git = "https://gitcode.com/Cangjie-SIG/cjoy.git", tag = "v0.90.0" }
```

---

## 参与贡献

邀请您与我们共同打造更优秀的 CJoy。

- **分享使用经验**：如果您觉得 CJoy 很实用，您的 **Star** 是对我们最大的鼓励。欢迎在个人博客撰写评测或教程，您的真知灼见能帮助更多人快速上手！
- **参与项目开发**：欢迎给我们提交 PR、Issue，欢迎参与任何形式的贡献。
- **贡献指南**：[contributing](doc/dev_guide/contributing.md)
- **项目维护者**：[@lanlingx](https://gitcode.com/lanlingx)

若您 fork 时请保留上游仓库地址 [Cangjie-SIG/cjoy](https://gitcode.com/Cangjie-SIG/cjoy) 或 [lanlingx/cjoy](https://gitcode.com/lanlingx/cjoy)，让 CJoy 变成仓颉生态中最广为人知的应用开发框架。

---

## 协议

参见 [LICENSE](LICENSE) 文件。
