<div align="center">
<h1>UMI</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.0.1-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.4-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjcov-0.0%25-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/state-孵化/毕业-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-OHOS/Cloud-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/points- ？/100-brightgreen" style="display: inline-block;" />
</p>

- points将由官方团队给出  

# 声明  
本开源项目目前仅是一个探索性项目，不代表最终结果，欢迎大家提出宝贵意见。

# UMI

AI-Driven Universal Model Interface for Cangjie Programming Language
UMI是新一代AI驱动仓颉编程语言通用模型接口。实现仓颉生态对多种类型数据库的便捷访问和编程，并集成高效的数据一致性同步API，实现可编程的接口层分布式数据总线，面向AI代码生成友好，可有效提高AI代码生成的准确性和代码质量。

## 特性

- 🚀 模式定义与自动代码生成
- 🗄️ 多数据库统一访问，包括关系型数据库和NoSQL数据库等（MySQL、PostgreSQL、SQLite、Oracle、MSSQL、MongoDB）
- 🔄 支持完整的数据库相关开发流水线，可从数据库schema自动生成ORM模型定义文件，同时也支持手动编写ORM模型定义文件。可从模型定义文件生成多端一致的ORM客户端。可从ORM模型定义文件推送数据库schema变更。
- 🧩 ORM客户端提供简洁的API接口，使开发者能够方便地进行数据库操作，如查询、插入、更新、删除等。、
- 🧱 模块化设计，可灵活扩展和集成第三方组件。
- 🔁 内置集成多端数据一致性同步API，支持实时数据同步和跨端数据访问，实现可编程的ORM层分布式数据总线。
- 🔄 高效数据同步与一致性保证
- 🤖 AI友好的API设计
- 🔒 基于角色的访问控制（RBAC）
- 📊 性能监控与指标收集
- 🛠️ 完整的CLI工具集，UMI的全部功能都可以通过命令行工具进行操作，便于与AI系统集成和互操作。
- 📋 规范驱动开发（SDD），基于spec-kit 开发v0.0.1版本，代码全部由AI生成

## 快速开始

### 安装

```bash
# 使用 cjpm 安装
cjpm add umi
```

### 基本使用

``cangjie
import umi.*

// 创建数据库配置
let config = DatabaseConfig(
    type: DatabaseType.PostgreSQL,
    host: "localhost",
    port: 5432,
    database: "myapp",
    username: "user",
    password: "password"
)

// 初始化ORM
let orm = UMI(config: config)
await orm.initialize()

// 定义模式
let schema = Schema(
    name: "myapp",
    version: "1.0.0",
    tables: [
        Table(
            name: "users",
            fields: [
                Field(name: "id", type: FieldType.Long, nullable: false),
                Field(name: "username", type: FieldType.String(maxLength: 50), nullable: false, unique: true),
                Field(name: "email", type: FieldType.String(maxLength: 255), nullable: false, unique: true),
                Field(name: "created_at", type: FieldType.DateTime, nullable: false)
            ],
            primaryKey: ["id"]
        )
    ]
)

// 生成客户端代码
let generator = CodeGenerator()
await generator.generate(schema: schema, outputPath: "./src/models/")
```

## CLI 使用

```bash
# 初始化ORM项目
umi init --name myapp --database PostgreSQL

# 生成客户端代码
umi generate --input schema.json --output ./src/models/

# 数据库迁移
umi migrate up

# 数据同步
umi sync --source mysql://user:pass@source/db --target postgresql://user:pass@target/db

# 运行测试
umi test --unit --integration
```

### 项目计划

介绍开发和维护等关键里程碑  
2025.11.16 完成项目架构设计，依赖库的选型和设计  
2025.11.23 完成项目0.0.1版本代码实现，包括ORM模型定义文件、主要开发流水线、核心功能的命令行工具、多端一致的ORM客户端代码生成等。  
2025.11.30 完成项目0.0.2版本代码实现，包括模块化机制，集成第三方分布式通信组件，完善文档、示例代码、测试用例等。  
2025.12.07 完成项目0.0.3版本代码实现，包括新增功能、性能优化、 bug修复等。  

## 项目架构

架构图文说明，包括模块说明、架构层次等详细说明。
UMI在OpenCangjie开发框架中的架构如下：
<img alt="" src="./docs/assets/UMI.png" style="display: inline-block;" width=60%/>

UMI主要开发流水线:
<img alt="" src="./docs/assets/UMI-Pipeline.png" style="display: inline-block;" width=60%/>

## 依赖  
https://gitcode.com/Cangjie-SIG/sql_builder

## 约束与限制
描述环境限制，版本限制，依赖版本等
### 项目适用的开发场景
适用于鸿蒙应用、Web应用、服务器端等全栈应用的数据库相关开发

### 项目适用的开发平台
适配HarmonyOS NEXT、Linux、Windows、MacOS等主流操作系统。

## 开源生态对标
nodejs生态的开源项目prisma orm，https://github.com/prisma  
vue生态的开源项目 pinia orm，https://pinia-orm.codedredd.de  
HarmonyOS生态的开源项目 rdbstore，https://github.com/bytedance/rdbStore  

## 文档
- [开源仓库](https://gitcode.com/Cangjie-SIG/UMI-ORM)
- [API 文档](docs/api.md)
- [模式定义指南](docs/schema-definition.md)
- [数据库配置](docs/database-config.md)
- [数据同步](docs/data-sync.md)
- [安全配置](docs/security.md)
- [设计文档](docs/design.md)
- [功能API](docs/feature_api.md)

## 参考资料
- [采用规范驱动开发AI辅助开发仓颉第三方库UMI-ORM](https://developer.huawei.com/consumer/cn/blog/topic/03198695458774023)

## 贡献
本项目采用SDD方法论开发参考[spec-kit](https://github.com/github/spec-kit)和[openspec](https://github.com/Fission-AI/OpenSpec)，建议采用一致方法论开发和贡献    
欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细信息。

## 许可证

Apache 2.0 License - 查看 [LICENSE](LICENSE) 文件了解详细信息。

## 支持

- 🐛 [问题反馈](https://gitcode.com/Cangjie-SIG/UMI-ORM/issues)
- 💬 [讨论区](https://gitcode.com/Cangjie-SIG/UMI-ORM/discussions)

## 已知问题
cjlint -f ./src/monitoring -o ./report/lint_report_monitoring.json -r json 无法运行出结果