# Kafka.cj - Apache Kafka Client for Cangjie

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Cangjie](https://img.shields.io/badge/cangjie-1.0.0+-green.svg)](https://cangjie-lang.cn)
[![Kafka](https://img.shields.io/badge/kafka-0.10%2B%20to%203.x-orange.svg)](https://kafka.apache.org)

基于仓颉语言实现的高性能 Apache Kafka 客户端库，提供完整的生产者和消费者 API，支持现代 Kafka 集群的所有核心功能。

## ✨ 核心特性

### 🚀 协议支持
- **完整协议实现**: 支持 Kafka 0.10+ 到 3.x 版本的核心协议
- **API 覆盖**: Produce、Fetch、Metadata、OffsetCommit、JoinGroup 等 10+ 种 API
- **版本兼容**: 自动协商协议版本，确保最佳兼容性

### 📤 生产者功能
- **高性能发送**: 支持同步/异步消息发送
- **智能分区**: 内置 RoundRobin 和 Hash 分区策略
- **批量处理**: 可配置的批次大小和延迟优化
- **确认机制**: 支持 0、1、-1 三种确认级别
- **错误重试**: 可配置的重试策略和退避算法

### 📥 消费者功能
- **消费者组**: 完整的消费者组协调和重平衡
- **偏移量管理**: 自动/手动偏移量提交
- **分区分配**: Range 和 RoundRobin 分配策略
- **会话管理**: 心跳机制和会话超时处理
- **暂停恢复**: 支持分区级别的消费控制

### 🗜️ 压缩支持
- **多种算法**: GZIP、SNAPPY、LZ4、ZSTD
- **自动检测**: 智能压缩算法选择
- **性能优化**: 流式压缩和内存优化

### 🔒 安全特性
- **TLS 加密**: 完整的 SSL/TLS 连接支持
- **认证机制**: 支持多种 SASL 认证方式
- **证书管理**: 灵活的证书配置和验证

### 🎯 高级功能
- **连接池**: 智能连接复用和管理
- **元数据缓存**: 自动元数据刷新和路由
- **监控指标**: 内置性能指标和监控
- **错误诊断**: 详细的错误信息和解决建议

## 🏗️ 架构设计

Kafka.cj 采用分层架构设计，模块化程度高，易于维护和扩展：

```
┌─────────────────────────────────────────────────────────────┐
│                    应用层 (Application Layer)                │
├─────────────────────────────────────────────────────────────┤
│  生产者API (Producer)  │  消费者API (Consumer)  │  示例程序   │
├─────────────────────────────────────────────────────────────┤
│                    客户端核心层 (Client Core)                │
├─────────────────────────────────────────────────────────────┤
│  元数据管理  │  分区器  │  配置管理  │  生命周期管理           │
├─────────────────────────────────────────────────────────────┤
│                    协议层 (Protocol Layer)                   │
├─────────────────────────────────────────────────────────────┤
│  Produce  │  Fetch  │  Metadata  │  OffsetCommit  │  JoinGroup │
├─────────────────────────────────────────────────────────────┤
│                    网络传输层 (Network Layer)                │
├─────────────────────────────────────────────────────────────┤
│  TCP传输  │  TLS加密  │  连接池  │  请求路由  │  错误重试     │
├─────────────────────────────────────────────────────────────┤
│                    基础设施层 (Infrastructure)               │
└─────────────────────────────────────────────────────────────┘
│  编解码器  │  压缩模块  │  错误处理  │  工具类  │  时间管理    │
└─────────────────────────────────────────────────────────────┘
```

### 📁 项目结构

```
kafka.cj/
├── src/                    # 源代码目录
│   ├── client/            # 客户端核心模块
│   │   └── pkg.cj         # KafkaClient、MetadataCache
│   ├── producer/          # 生产者模块
│   │   └── pkg.cj         # Producer、ProducerBuilder
│   ├── consumer/          # 消费者模块
│   │   ├── pkg.cj         # Consumer、ConsumerBuilder
│   │   ├── assignor.cj    # 分区分配器接口
│   │   └── range_assignor.cj # Range分配策略
│   ├── protocol/          # 协议实现模块
│   │   ├── produce.cj     # Produce API
│   │   ├── fetch.cj       # Fetch API
│   │   ├── metadata.cj    # Metadata API
│   │   ├── offset_*.cj    # 偏移量管理API
│   │   └── *_group.cj     # 消费者组API
│   ├── network/           # 网络传输模块
│   │   ├── pkg.cj         # Transport、NetworkClient
│   │   └── tls.cj         # TLS加密支持
│   ├── compression/       # 压缩模块
│   │   └── pkg.cj         # 多种压缩算法实现
│   ├── codecs/           # 编解码模块
│   │   └── pkg.cj         # ByteWriter、ByteReader
│   ├── error/            # 错误处理模块
│   │   ├── pkg.cj         # KafkaCode、错误类型
│   │   └── diagnostics.cj # 错误诊断
│   ├── utils/            # 工具类模块
│   │   └── time.cj        # 时间处理工具
│   ├── examples/         # 示例代码
│   │   ├── producer/     # 生产者示例
│   │   ├── consumer/     # 消费者示例
│   │   └── simple_client/ # 简单客户端示例
│   └── tests/            # 测试代码
│       ├── integration_test.cj # 集成测试
│       ├── comprehensive_integration_test.cj # 综合测试
│       └── *_test.cj      # 各模块单元测试
├── docs/                  # 完整技术文档
│   ├── architecture/     # 架构设计文档
│   ├── api/              # API 使用指南
│   ├── protocol/         # 协议实现文档
│   ├── examples/         # 示例和最佳实践
│   └── development/      # 开发指南
├── cjpm.toml             # 项目配置文件
└── README.md             # 项目说明
```

## 🚀 快速开始

### 📦 安装依赖

在您的 `cjpm.toml` 文件中添加依赖：

```toml
[dependencies]
kafka = { path = "path/to/kafka.cj" }
```

### 📤 生产者示例

#### 基础生产者

```cangjie
import kafka.{Producer, ProducerBuilder, ProducerRecord}
import kafka.error.{KafkaError}
import std.time.{Duration}

main() {
    // 使用构建器模式创建生产者
    let producerResult = ProducerBuilder()
        .withBrokers(["localhost:9092"])
        .withClientId("my-producer")
        .withRequiredAcks(RequiredAcks.One)
        .withCompression(Compression.GZIP)
        .withTimeout(Duration.seconds(30))
        .build()
    
    match (producerResult) {
        case Ok(producer) => {
            // 创建消息记录
            let record = ProducerRecord.create(
                topic: "test-topic",
                value: "Hello Kafka from Cangjie!".getBytes()
            )
            
            // 同步发送消息
            match (producer.send(record)) {
                case Ok(metadata) => {
                    println("消息发送成功: topic=${metadata.topic}, partition=${metadata.partition}, offset=${metadata.offset}")
                }
                case Err(error) => {
                    println("发送失败: ${error}")
                }
            }
            
            // 确保所有消息都已发送
            producer.flush()
            producer.close()
        }
        case Err(error) => {
            println("创建生产者失败: ${error}")
        }
    }
}
```

#### 异步生产者

```cangjie
// 异步发送消息
let record = ProducerRecord.withKey(
    topic: "user-events",
    key: "user-123".getBytes(),
    value: "{\"action\": \"login\", \"timestamp\": 1234567890}".getBytes()
)

// 异步发送并处理回调
producer.sendAsync(record, { result =>
    match (result) {
        case Ok(metadata) => println("异步发送成功: ${metadata}")
        case Err(error) => println("异步发送失败: ${error}")
    }
})
```

### 📥 消费者示例

#### 基础消费者

```cangjie
import kafka.{Consumer, ConsumerBuilder, ConsumerRecord}
import kafka.{TopicPartition, OffsetResetStrategy}
import std.time.{Duration}

main() {
    // 使用构建器模式创建消费者
    let consumerResult = ConsumerBuilder()
        .withBrokers(["localhost:9092"])
        .withGroupId("my-consumer-group")
        .withClientId("my-consumer")
        .withAutoOffsetReset(OffsetResetStrategy.Latest)
        .withEnableAutoCommit(true)
        .withAutoCommitInterval(Duration.seconds(5))
        .build()
    
    match (consumerResult) {
        case Ok(consumer) => {
            // 订阅主题
            consumer.subscribe(["test-topic", "user-events"])
            
            // 消费消息循环
            while (true) {
                match (consumer.poll(Duration.seconds(1))) {
                    case Ok(records) => {
                        for (record in records) {
                            println("收到消息: topic=${record.topic}, partition=${record.partition}, offset=${record.offset}")
                            println("消息内容: ${String.fromUtf8(record.value)}")
                            
                            // 处理消息逻辑
                            processMessage(record)
                        }
                        
                        // 手动提交偏移量（如果禁用了自动提交）
                        // consumer.commitSync()
                    }
                    case Err(error) => {
                        println("拉取消息失败: ${error}")
                    }
                }
            }
        }
        case Err(error) => {
            println("创建消费者失败: ${error}")
        }
    }
}

func processMessage(record: ConsumerRecord): Unit {
    // 在这里处理您的业务逻辑
    println("处理消息: ${record.topic}")
}
```

#### 手动分区分配

```cangjie
// 手动分配特定分区
let partitions = [
    TopicPartition("test-topic", 0),
    TopicPartition("test-topic", 1)
]
consumer.assign(partitions)

// 从特定偏移量开始消费
consumer.seek(TopicPartition("test-topic", 0), 100)
```

## 🔧 构建和运行

### 构建项目

```bash
# 检查项目配置
cjpm check

# 构建项目
cjpm build

# 构建并运行测试
cjpm build --test

# 清理构建产物
cjpm clean
```

### 运行示例

```bash
# 运行简单客户端示例
cjpm run --name kafka.examples.simple_client

# 运行生产者示例
cjpm run --name kafka.examples.producer

# 运行消费者示例
cjpm run --name kafka.examples.consumer
```

### 运行测试

```bash
# 运行所有测试
cjpm test

# 运行集成测试
cjpm run --name kafka.tests.integration_test

# 运行综合集成测试
cjpm run --name kafka.tests.comprehensive_integration_test

# 运行特定测试
cjpm test src/tests/snappy_test.cj
cjpm test src/tests/tls_test.cj
```

## 📋 API 文档

详细的 API 文档请参考：

- [📖 完整文档](./docs/README.md) - 技术文档总览
- [🏗️ 架构设计](./docs/architecture/README.md) - 系统架构和设计原则
- [📤 生产者 API](./docs/api/producer.md) - 生产者完整使用指南
- [📥 消费者 API](./docs/api/consumer.md) - 消费者完整使用指南
- [🔌 协议实现](./docs/protocol/README.md) - Kafka 协议实现详解
- [🌐 网络层](./docs/network/README.md) - 网络传输和连接管理
- [🗜️ 压缩模块](./docs/compression/README.md) - 压缩算法和配置
- [💡 示例代码](./docs/examples/README.md) - 丰富的使用示例和最佳实践
- [🛠️ 开发指南](./docs/development/README.md) - 开发环境搭建和贡献指南

## 🔧 配置选项

### 生产者配置

```cangjie
let producer = ProducerBuilder()
    .withBrokers(["broker1:9092", "broker2:9092"])  // Kafka集群地址
    .withClientId("my-app-producer")                 // 客户端标识
    .withRequiredAcks(RequiredAcks.All)              // 确认级别: 0, 1, -1
    .withTimeout(Duration.seconds(30))               // 请求超时时间
    .withRetries(3)                                  // 重试次数
    .withBatchSize(16384)                           // 批次大小(字节)
    .withLingerMs(5)                                // 批次延迟时间
    .withCompression(Compression.SNAPPY)            // 压缩算法
    .withPartitioner(HashPartitioner())             // 分区策略
    .build()
```

### 消费者配置

```cangjie
let consumer = ConsumerBuilder()
    .withBrokers(["broker1:9092", "broker2:9092"])  // Kafka集群地址
    .withGroupId("my-consumer-group")               // 消费者组ID
    .withClientId("my-app-consumer")                // 客户端标识
    .withAutoOffsetReset(OffsetResetStrategy.Latest) // 偏移量重置策略
    .withEnableAutoCommit(false)                    // 禁用自动提交
    .withMaxPollRecords(500)                        // 单次拉取最大记录数
    .withSessionTimeout(Duration.seconds(30))       // 会话超时时间
    .withHeartbeatInterval(Duration.seconds(3))     // 心跳间隔
    .withFetchMinBytes(1024)                        // 最小拉取字节数
    .withFetchMaxWait(Duration.milliseconds(500))   // 最大等待时间
    .build()
```

## 🔒 安全配置

### TLS 加密连接

```cangjie
let tlsConfig = TlsConfig(
    enabled: true,
    keystorePath: "/path/to/keystore.jks",
    keystorePassword: "keystore-password",
    truststorePath: "/path/to/truststore.jks",
    truststorePassword: "truststore-password"
)

let producer = ProducerBuilder()
    .withBrokers(["secure-broker:9093"])
    .withTlsConfig(tlsConfig)
    .build()
```

## 🚀 性能优化

### 生产者性能调优

```cangjie
// 高吞吐量配置
let highThroughputProducer = ProducerBuilder()
    .withBatchSize(65536)                    // 增大批次大小
    .withLingerMs(20)                        // 增加批次等待时间
    .withCompression(Compression.LZ4)        // 使用高效压缩
    .withRequiredAcks(RequiredAcks.One)      // 降低确认级别
    .build()

// 低延迟配置
let lowLatencyProducer = ProducerBuilder()
    .withBatchSize(1024)                     // 减小批次大小
    .withLingerMs(0)                         // 立即发送
    .withCompression(Compression.NONE)       // 禁用压缩
    .withRequiredAcks(RequiredAcks.One)      // 平衡确认级别
    .build()
```

### 消费者性能调优

```cangjie
// 高吞吐量消费配置
let highThroughputConsumer = ConsumerBuilder()
    .withMaxPollRecords(2000)                // 增大单次拉取记录数
    .withFetchMinBytes(65536)                // 增大最小拉取字节数
    .withFetchMaxWait(Duration.seconds(1))   // 适当增加等待时间
    .build()
```

## 🔍 监控和指标

```cangjie
// 获取生产者指标
let metrics = producer.getMetrics()
println("发送总数: ${metrics.recordSendTotal}")
println("发送速率: ${metrics.recordSendRate}")
println("平均延迟: ${metrics.recordSendLatencyAvg}")

// 获取消费者指标
let consumerMetrics = consumer.getMetrics()
println("消费总数: ${consumerMetrics.recordConsumeTotal}")
println("消费速率: ${consumerMetrics.recordConsumeRate}")
println("处理延迟: ${consumerMetrics.recordProcessLatencyAvg}")
```

## 🐛 错误处理

```cangjie
// 生产者错误处理
match (producer.send(record)) {
    case Ok(metadata) => {
        // 发送成功
    }
    case Err(error) => {
        match (error) {
            case NetworkError(msg) => {
                // 网络错误，可能需要重试
                println("网络错误: ${msg}")
            }
            case KafkaError(code, msg) => {
                // Kafka 服务器错误
                println("Kafka错误 [${code}]: ${msg}")
            }
            case _ => {
                // 其他错误
                println("未知错误: ${error}")
            }
        }
    }
}
```

## 🔄 兼容性

| 组件 | 版本要求 | 说明 |
|------|----------|------|
| **仓颉语言** | 1.0.0+ | 需要支持最新语法特性 |
| **Kafka 集群** | 0.10+ 到 3.x | 支持所有主流 Kafka 版本 |
| **操作系统** | macOS, Linux, Windows | 跨平台支持 |
| **TLS** | 1.2+ | 安全连接支持 |

## 📊 开发状态

| 模块 | 状态 | 功能完成度 | 说明 |
|------|------|------------|------|
| 🔧 **核心协议** | ✅ 完成 | 95% | 支持 10+ 种 Kafka API |
| 📤 **生产者** | ✅ 完成 | 90% | 同步/异步发送，分区策略 |
| 📥 **消费者** | ✅ 完成 | 85% | 消费者组，偏移量管理 |
| 🗜️ **压缩** | ✅ 完成 | 80% | GZIP, SNAPPY 完整支持 |
| 🔒 **安全** | ✅ 完成 | 75% | TLS 加密连接 |
| 🌐 **网络** | ✅ 完成 | 90% | 连接池，错误重试 |
| 📊 **监控** | 🚧 开发中 | 60% | 基础指标收集 |
| 🧪 **测试** | ✅ 完成 | 85% | 单元测试，集成测试 |
| 📚 **文档** | ✅ 完成 | 95% | 完整的 API 文档 |

## 🤝 贡献指南

我们欢迎社区贡献！请参考 [开发指南](./docs/development/README.md) 了解：

- 🛠️ 开发环境搭建
- 📝 代码规范和最佳实践
- 🧪 测试要求和流程
- 📋 提交和审查流程

## 📄 许可证

本项目采用 [Apache License 2.0](LICENSE) 开源协议。

## 🙏 致谢

感谢以下项目和社区的启发：

- [Apache Kafka](https://kafka.apache.org/) - 原始 Kafka 项目
- [仓颉语言](https://cangjie-lang.cn/) - 现代化的编程语言
- Kafka 社区的各种客户端实现

---

**📞 联系我们**

- 🐛 [报告问题](https://gitcode.com/louloulin/kafka.cj/issues)
- 💡 [功能建议](https://gitcode.com/louloulin/kafka.cj/discussions)
- 📧 邮件: kafka-cj@example.com

**⭐ 如果这个项目对您有帮助，请给我们一个 Star！**
