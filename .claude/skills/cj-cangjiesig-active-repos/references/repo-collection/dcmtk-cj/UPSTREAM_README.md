# dcmtkcj

## 项目简介

`dcmtkcj` 是一个专为华为仓颉（Cangjie）编程语言打造的项目，它对 DCMTK 3.9.6 的 C++ 接口进行了封装，旨在为仓颉开发者提供便捷的 DICOM 相关功能调用能力，助力开发者在仓颉生态中更高效地进行医疗影像相关应用的开发。

## 背景

DCMTK（DICOM Toolkit）是一个功能强大的开源软件包，包含了一系列用于处理 DICOM 标准的库和应用程序，广泛应用于医疗影像领域。而仓颉语言是华为推出的新一代编程语言，具有安全、高效、简洁等特性。`dcmtkcj` 项目应运而生，填补了仓颉语言在 DCMTK 接口封装方面的空白，使仓颉开发者能够轻松利用 DCMTK 的强大功能。

## 功能特性

- 基于 DCMTK 3.9.6 版本进行封装，涵盖了 DCMTK 众多核心模块的功能，如 `dcmdata`（数据编码 / 解码库）、`dcmnet`（网络库）、`dcmjpeg`（JPEG 压缩 / 解压缩库）等。
- 提供了符合仓颉语言风格的接口，降低了仓颉开发者使用 DCMTK 的学习成本和开发难度。
- 支持动态链接库输出，方便集成到各类仓颉应用程序中。
- 包含演示程序，帮助开发者快速了解和使用 `dcmtkcj`。

## 安装指南

### 前置条件

- 确保系统中已安装 CMake（版本 3.7.0 及以上）。
- 安装仓颉语言开发环境及相关工具链（如 `cjpm`）。

### Windows 系统安装步骤

1. 克隆项目代码到本地：

   

   ```bash
   git clone <项目仓库地址>
   cd dcmtkcj
   ```

2. 执行构建脚本：

   

   ```bash
   build-win.bat
   ```

   

   该脚本会完成 DCMTK 的构建安装以及 `dcmtkcj` 项目的编译。

### macOS 系统安装步骤

1. 克隆项目代码到本地：

   

   ```bash
   git clone <项目仓库地址>
   cd dcmtkcj
   ```

   

2. 执行构建脚本：

   

   ```bash
   chmod +x build-mac.sh
   ./build-mac.sh
   ```

   

   脚本将处理 DCMTK 的构建安装和 `dcmtkcj` 的编译工作。

###  Linux/HarmonyOS 正在适配中



## 使用示例

以下是一个简单的使用示例，展示如何使用 `dcmtkcj` 进行一些基础操作（具体示例需根据实际封装接口进行编写）：

```cangjie
// 引入 dcmtkcj 相关模块
import dcmtkcj.*

// 进行 DICOM 文件操作示例
let file = DicomFile(filename:"testdata/IM-0001-0375.dcm")
let dataset = file.getDataset()
let patientNameTag = dataset.getElement(tag:DicomTags.PatientName)
try{
	println("PatientName is ${patientNameTag.getOrThrow().getString()}")
}catch (error:Error) {
	println("illegal dicom file")    
}
```

更多详细的使用示例可参考项目中的 `dcmtkcj.demo` 模块。

## 项目结构

- `dcmtk/`：包含 DCMTK 相关源码及配置文件，是封装的基础。
- cjpm.toml：项目配置文件，指定了项目名称、版本、编译选项等信息。
- build-win.bat：Windows 系统下的构建脚本。
- build-mac.sh：macOS 系统下的构建脚本。
- CHANGELOG.md：项目变更日志，记录了各版本的更新内容。
- `dcmtkcj.demo/`：演示程序模块，包含示例代码。

## 配置说明

项目的主要配置信息在 cjpm.toml 文件中：

- `package` 部分：定义了项目的基本信息，如名称、版本、描述等。
- `compile-option`：指定了编译时的链接选项，需确保指向正确的 DCMTK 库文件路径。
- `package.package-configuration."dcmtkcj.demo"`：配置了演示程序的输出类型为可执行文件。

## 贡献指南

我们非常欢迎开发者为 `dcmtkcj` 项目贡献代码或提供反馈。

### 提交 Bug 报告

如果您发现项目中存在 Bug，请按照以下步骤提交报告：

1. 确认您使用的是最新版本的 `dcmtkcj`。

2. 检查是否已有类似的 Bug 报告，避免重复提交。

3. 若确认为新 Bug，可发送邮件至

    

   [shawn.ming@outlook.com](mailto:shawn.ming@outlook.com)

   ，邮件中需包含：

   - 期望的行为和实际发生的行为。
   - 详细的复现步骤，最好能提供最小可复现示例。
   - 相关的环境信息（如操作系统、编译器版本等）。
   - 若已找到修复方法，可附上补丁文件或通过 GitHub Pull Request 提交。

### 代码贡献

在贡献代码时，请确保：

- 您对所贡献的代码拥有 100% 的版权，且代码符合 [DCMTK 许可证](https://support.dcmtk.org/docs/file_copyright.html)（与 BSD 许可证兼容）。
- 代码风格尽量与项目现有代码保持一致。
- 提交前进行充分的测试，确保代码的正确性。

## 许可证信息

`dcmtkcj` 项目的许可证遵循 DCMTK 的许可证，与 [BSD 许可证](https://opensource.org/license/bsd-3-clause) 兼容。具体信息可参考 DCMTK 相关的版权文件。

项目中所使用的 DCMTK 包含多个子模块，部分子模块（如 `dcmjpeg` 中使用的 IJG JPEG 软件、`dcmjpls` 中使用的 CharLS 库等）有其各自的许可证，详情请查阅相关子模块的文档。

## 相关链接

- [DCMTK 官方网站](https://dcmtk.org/)
- [DCMTK 在线文档](https://support.dcmtk.org/docs/)
- [DCMTK Wiki](https://support.dcmtk.org/wiki/)
- [DCMTK 公共讨论论坛](https://forum.dcmtk.org/)
- [仓颉语言官方文档](https://cangjie-lang.cn/)

## 联系方式

如果您在使用 `dcmtkcj` 过程中有任何问题或建议，可通过以下方式联系我们：

- 项目仓库 [Issues](https://gitcode.com/Cangjie-SIG/dcmtk-cj/issues)
- 开发者邮箱：[shawn.ming@outlook.com](mailto:shawn.ming@outlook.com)
