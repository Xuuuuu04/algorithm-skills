<div align="center">
<h1>仓颉函数调用图</h1>
</div>

<p align="center">
<img alt="release" src="https://img.shields.io/badge/release-v1.3.1-brightgreen" style="display: inline-block;" />
<img alt="cjc" src="https://img.shields.io/badge/cjc-1.0.1-blue" style="display: inline-block;" />
<img alt="status" src="https://img.shields.io/badge/status-active-blueviolet" style="display: inline-block;" />
<img alt="license" src="https://img.shields.io/badge/license-MIT-lightgrey" style="display: inline-block;" />
</p>

## 项目简介

仓颉函数调用图（Cangjie Call Graph）是一款针对仓颉语言的静态分析工具。程序使用官方 AST 访问器遍历代码，记录函数定义与调用关系，并导出多种可视化格式，帮助团队快速识别耦合热点、递归路径以及模块间的交互情况。

### 核心特性

- 基于 AST 的精确遍历，同时捕获直接调用、变量声明中的延迟调用及递归边。
- 支持多种输出格式：JSON（便于二次加工）、DOT（Graphviz）、Mermaid（文档嵌入）以及 Markdown 分析摘要。
- 自适应项目发现逻辑，可扫描常见的仓颉工程结构（`src/`、`lib/`、`tests/`、`examples/`）或单个 `.cj` 文件。
- 提供命令行接口，支持 `--input`、`--output`、`--project`、`--format`、`--verbose`、`--recursive` 等参数。
- 内置统计信息，展示解析的文件数量、函数数量以及调用关系总数。

### 发展规划

- v1.4.0：在报告中增加模块级指标与热点路径分析。
- v1.5.0：集成可选的 HTML 报告与 CI 友好型退出码。

## 项目架构

本项目结构紧凑，单一入口负责分析流程，配合多个辅助函数完成 I/O、命令行解析与输出格式化。

### 源码目录

```text
.
├── README.md                   # 项目概览
├── LICENSE                     # MIT 许可证
├── cjpm.toml                   # 包描述与编译器版本
├── config/
│   ├── cangjie-config.json     # 编译/模板配置
│   └── project-template.conf   # 项目模板示例
├── scripts/
│   ├── analyze-project.ps1     # PowerShell 分析脚本（Windows）
│   ├── analyze-cangjie-project.bat # 批处理分析脚本（Windows）
│   ├── build.sh                # 示例构建脚本（类 Unix）
│   └── run.sh                  # 示例运行脚本（类 Unix）
├── src/
│   └── main.cj                 # 调用图生成器入口
├── target/
│   └── release/                # 编译产物与缓存（按需生成）
└── tests/
    ├── src/                    # 测试用仓颉源码
    └── build/                  # 调用图与报告示例输出
```

### 关键模块

- `CallGraphVisitor`：基于 `std.ast.Visitor` 的自定义访问器，负责维护函数上下文并记录调用边。
- `discover_cangjie_files`：根据常见仓颉项目布局收集候选源文件。
- `build_call_graph_{json,dot,mermaid}`：将分析结果渲染为不同格式的输出。
- `parse_arguments`：封装 `std.argopt`，统一解析 CLI 参数并控制输出模式。

## 使用说明

### 先决条件

- 仓颉工具链（含标准库与 `cjc` 编译器），版本需 ≥ 1.0.1。
- Windows 或 Linux 环境，需对目标输出目录拥有写权限。

### 编译

可直接调用编译器或使用 `cjpm`：

```powershell
# 编译至 target/release/bin/main.exe
cjc src/main.cj -o target/release/bin

# 或者使用 cjpm
cjpm build
```

### 运行

```powershell
# 分析 ./src 下的源码并输出到 ./build
target/release/bin/main.exe --input ./src --output ./build --project DemoProject

# 打开详细日志，仅生成 Mermaid 输出
target/release/bin/main.exe -i ./tests -o ./build -p TestsOnly --format mermaid --verbose
```

### 命令行接口一览

| 选项 | 说明 | 默认值 |
| --- | --- | --- |
| `-h`, `--help` | 显示帮助信息并退出 | - |
| `-V`, `--version` | 显示版本信息并退出 | - |
| `-i <DIR>`, `--input <DIR>` | 指定要分析的仓颉项目目录 | `./src` |
| `-o <DIR>`, `--output <DIR>` | 指定输出目录 | `./build` |
| `-p <NAME>`, `--project <NAME>` | 报告中使用的项目名 | `CangjieProject` |
| `-f <FORMAT>`, `--format <FORMAT>` | 输出格式：`all`, `json`, `dot`, `mermaid`，可逗号分隔 | `all` |
| `-v`, `--verbose` | 打开详细日志 | 关闭 |
| `-r`, `--recursive` | 递归扫描子目录 | 关闭 |

常见示例：

- 仅生成 JSON 与 DOT：`main.exe --format json,dot --recursive`
- 指定项目名与输出目录：`main.exe -i ../cangjie-demo/src -o ./build -p MyDemo -v`
- 查看帮助：`main.exe --help`

#### 在 Windows 上使用脚本快速分析

```powershell
# PowerShell（推荐）
.\scripts\analyze-project.ps1 -ProjectPath "." -OutputPath "./analysis-output" -ProjectName "CangjieProject"

# CMD 批处理
scripts\analyze-cangjie-project.bat "D:\MyCangjieProject"
```

> 注意：脚本默认在 `D:\cangjie-build\main.exe` 路径查找分析器，可根据需要修改脚本内路径或将可执行文件编译到该位置。

生成的文件包括：

- `call-graph.json` —— 机器可读的调用关系。
- `call-graph.dot` —— 用于 Graphviz 的描述，可导出为 PNG/SVG。
- `call-graph.mermaid.md` —— Mermaid 图块，方便嵌入文档。
- `analysis-report.md` —— Markdown 统计报告，附带后续分析建议。

## 约束与限制

- 当前实现依赖仓颉编译器运行时和标准库。
- 数组仍采用手动扩容策略，超大型项目需等待后续的动态集合支持。
- 运行前需确保输出目录存在，否则文件写入将失败。

## 开源协议

本项目遵循 [MIT License](./LICENSE)。

## 参与贡献

欢迎提交 Issue 与 Pull Request。若遇到解析或访问器回归，请附带可复现的示例及相关 `call-graph.json` 片段，便于定位问题。