<div align="center">
<h1>morerandom</h1>
</div>

<p align="center">
<img alt="release" src="https://img.shields.io/badge/release-v0.1.4-brightgreen" style="display: inline-block;" />
<img alt="cjc" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="state" src="https://img.shields.io/badge/state-孵化-brightgreen" style="display: inline-block;" />
</p>

## 1 介绍

morerandom 是一个为 仓颉 (Cangjie) 语言提供的轻量级随机数库，目标是为统计模拟、科学计算和通用应用提供可替换、可复现且易于测试的 PRNG 接口与若干常用实现（例如 LCG、Xorshift、PCG）。

### 1.1 项目特性

- 可重复性：支持通过显式种子重现随机序列。
- 可替换性：定义清晰的 PRNG 抽象，便于替换实现。
- 易测试：接口便于单元测试和统计检验。
- 可扩展：为分布采样器、并行包装和序列化留出扩展点。

### 1.2 项目计划

1. 核心：PRNG 抽象与至少一个实现（LCG）。
2. 分布：实现常见分布采样器（正态、指数等）。

## 2 架构

### 2.1 项目结构

```shell
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── cjpm.toml
├── doc
│   ├── design.md
│   └── feature_api.md
├── src
│   ├── main.cj           # 模块入口
│   ├── core              # PRNG 抽象 (random.cj)
│   ├── impl              # 具体实现 (lcg.cj)
│   ├── distributions     # 基于 PRNG 的分布采样器
│   └── utils             # 工具函数 (time.cj)
├── test                  # 测试代码目录
└── ...
```

包与依赖原则：`core` 为最底层接口，`impl` 依赖 `core`；`utils` 提供运行时工具（如 `nowUnixNano()`），示例或 CLI 负责将种子注入到实现中以避免循环依赖。

## 3 使用说明

### 3.1 编译构建（Win/Linux/Mac）
在工程根目录下运行：  
`cjpm build`

### 3.2 单元测试
在工程根目录下运行：  
`cjpm test`
### 3.3 功能示例
1. 示例代码
下面为一个简短的使用示例（基于 `LCG` 实现）：

```cangjie
import morerandom.impl.*
import morerandom.distributions.*

main() {
    // 1. 初始化基础随机数生成器 (PRNG)
    let lcg = Lcg() // 默认使用系统时间戳作为种子

    // 2. 使用不同的分布采样器
    
    // 正态分布 (均值=0, 标准差=1)
    let normal = Normal(lcg, 0.0, 1.0).sample()
    println("Normal: ${normal}")

    // 伯努利分布 (成功概率=0.5)
    let bernoulli = Bernoulli(lcg, 0.5).sample()
    println("Bernoulli: ${bernoulli}")

    // 狄利克雷分布 (浓度参数=[1.0, 2.0, 3.0])
    let dirichlet = Dirichlet(lcg, [1.0, 2.0, 3.0]).sample()
    println("Dirichlet: ${dirichlet}")

    // 冯·米塞斯分布 (平均方向=0.0, 集中度=1.0)
    let vonMises = VonMises(lcg, 0.0, 1.0).sample()
    println("VonMises: ${vonMises}")
}
```

2. 输出
<img alt="" src="doc\demo.png" style="display: inline-block;" width=80%/>

## 4 参与贡献

欢迎提交 Issue 或 PR。如需贡献代码，请遵循仓库中的 `CONTRIBUTING.md`（若存在）的贡献指南。

本项目采用 MIT 许可：

[MIT License](./LICENSE)
