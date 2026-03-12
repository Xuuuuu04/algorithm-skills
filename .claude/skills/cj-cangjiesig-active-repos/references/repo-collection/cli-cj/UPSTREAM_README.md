<div align="center">
<h1>CLI-CJ</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.2.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/build-pass-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/license-MulanPSL 2.0-blue" style="display: inline-block;" />
</p>

## 简介

这是一个使用仓颉语言编写的命令行框架，旨在简化命令行界面 (CLI) 的创建过程。**cli-cj** 提供了一种声明式的方式来定义命令、子命令和参数，自动处理输入解析、帮助信息生成和参数验证。

## 特性

*   声明式命令定义
*   参数处理 (短名称/长名称选项, 位置参数, 必需参数)
*   参数动作 (`Set`, `SetTrue`, `SetFalse`, `Append`)
*   自动帮助信息生成
*   子命令嵌套
*   参数分组
*   类型安全的参数访问
*   基本的错误处理

## 快速上手

### 安装 

在项目的`cjpm.toml`中，`[dependencies]`下添加以下内容：

```toml
cli = { git = "https://gitcode.com/mcbbsandnz/cli-cj", branch = "main" }
```

### 基本用法

1.  **导入 `cli` 包:**

    ```cj
    package main

    import cli.{Command, Arg, ArgAction, ArgMatch}
    ```

2.  **创建根命令:**

    ```cj
    main(): Unit {
        let rootCmd = Command("mycli")
            .about("我的简单 CLI 应用程序")
            .usage("mycli")
            .action { argMatch =>
                println("欢迎使用 mycli!")
                // 如果需要，可以使用 argMatch 访问参数
            }
    }
    ```

3.  **为命令添加参数:**

    ```cj
    main(): Unit {
        let rootCmd = Command("mycli")
            .about("我的简单 CLI 应用程序")
            .usage("mycli [--name <name>]")
            .arg(Arg("name")
                .help("你的名字")
                .defaultValue<String>("访客"))
            .action { argMatch =>
                let name = argMatch.getString("name") // 获取 String 类型的参数
                println("你好, ${name}!")
            }
    }
    ```

4.  **添加子命令:**

    ```cj
    main(): Unit {
        let rootCmd = Command("mycli")
            .about("我的简单 CLI 应用程序")
            .usage("mycli [--name <name>]")
            .arg(Arg("name")
                .help("你的名字")
                .defaultValue<String>("访客"))
            .action { argMatch =>
                let name = argMatch.getString("name") // 获取 String 类型的参数
                println("你好, ${name}!")
            }

        let greetCmd = Command("greet")
            .about("问候用户")
            .usage("mycli greet --name <name>")
            .arg(Arg("name")
                .help("要问候的名字")
                .required(true))
            .action { argMatch =>
                let name = argMatch.getString("name")
                println("你好, ${name}!")
            }

        rootCmd.subcommand(greetCmd)
    }
    ```

5.  **构建并运行 CLI:**

    ```cj
    main(): Unit {
        // ... (命令定义如上) ...
    
        rootCmd.build() // 开始处理命令行输入
    }
    ```

    对于**简单**的代码您可以直接这样：
    ```cj
    main(): Unit {
        Command("mycli")
            .about("我的简单 CLI 应用程序")
            .usage("mycli [--name <name>]") // 根命令 usage
            .arg(Arg("name")
                .help("你的名字")
                .defaultValue<String>("访客"))
            .action { argMatch =>
                let name = argMatch.getString("name") // 获取 String 类型的参数
                println("你好, ${name}!")
            }
            .subcommand(Command("greet")
                .about("问候用户")
                .usage("mycli greet --name <name>") // 子命令 usage
                .arg(Arg("name")
                    .help("要问候的名字")
                    .required(true))
                .action { argMatch =>
                    let name = argMatch.getString("name")
                    println("你好, ${name}!")
                })
            .build()
    }
    ```

    现在您可以从命令行运行您的 CLI：

    ```bash
    # 对于基本示例:
    ./mycli
    
    # 带参数:
    ./mycli --name John
    
    # 带子命令:
    ./mycli greet --name Alice
    
    # 获取帮助:
    ./mycli --help
    ./mycli greet --help
    ```

### 帮助信息输出模板
![示例图片](docs/images/帮助信息模板.png)

## 定义命令和子命令

使用 `Command` 类来定义命令和子命令。

*   **`Command(name: String)`:** 创建一个具有给定名称的新命令。该名称用于从命令行调用命令。
*   **`.about(about: String)`:** 设置命令的简短描述，显示在帮助信息中。
*   **`.usage(usage: String)`:** 设置命令的自定义用法字符串（可选）。
*   **`.group(group: String)`:** 将命令分配给帮助输出中的特定组（默认为 "Commands"）。
*   **`.arg(arg: Arg): This`:** 向当前命令添加参数
*   **`.args(args: Array<Arg>): This`:** 批量添加多个参数。
*   **`.action(action: (ArgMatch) -> Unit)`:** 设置在调用命令时要执行的动作。动作是一个函数，它接受一个 `ArgMatch` 对象作为输入，提供对已解析参数的访问。
*   **`.noInputBuild(args: Array<String>): This`:** 设置当命令在没有提供任何输入参数时使用的默认参数。这允许为无输入参数命令定义默认行为。
*   **`.subcommand(subcommand: Command)`:** 向当前命令添加子命令。您可以嵌套子命令以创建复杂的 CLI 结构。
*   **`.subcommands(subcommands: Array<Command>): This`:** 批量添加多个子命令。
*   **`.build()`:** 启动 CLI 应用程序，处理命令行参数并执行相应的命令动作。
*   **`.ident(ident: Int64)`:** 设置子命令和参数帮助输出的缩进级别。
*   **`.helpIdent(helpIdent: Int64)`:** 设置参数和子命令帮助输出中帮助文本本身的缩进级别。

## 定义参数

使用 `Arg` 类为命令定义参数。

* **`Arg(name: String)`:** 创建一个具有给定长名称的新参数（例如，`--name`）。

* **`Arg(short: Rune)`:** 创建一个仅具有短名称的参数（例如，`-n`）。这种参数在帮助信息中只显示短名称。

* **`.short(short: Rune)`:** 为参数设置一个短名称（例如，`-n`）。

* **`.group(group: String)`:** 将参数分配给帮助输出中的特定组（默认为 "Options"）。

* **`.defaultValue<T>(value: T)` / `.defaultValue<T>(value: Iterable<T>)`:** 如果用户未提供参数，则为其设置默认值。支持单个值和可迭代对象，用于可以接受多个值的参数。

* **`.help(help: String)`:** 设置参数的描述，显示在帮助信息中。

* **`.required(required: Bool)`:** 将参数标记为是否必需。如果缺少必需参数，CLI 将显示错误。

*   **`.action(action: ArgAction)`:** 设置参数的动作类型。可用的动作有：
    *   **`ArgAction.Set` (默认):** 将参数的值设置为提供的输入。
    *   **`ArgAction.SetTrue`:** 当标志存在时，将参数的值设置为 `true`，否则设置为 `false`。对于没有值的布尔标志非常有用（例如，`--verbose`）。
    *   **`ArgAction.SetFalse`:** 当标志存在时，将参数的值设置为 `false`，否则设置为 `true`。
    *   **`ArgAction.Append`:** 当参数多次指定时，将多个值附加到参数。
    
* **`.positionalArgsSet(onlyPositionalArgs: Bool, priority: UInt64, inputCountRange: Range<UInt64>)`** 

  **`.positionalArgsSet(onlyPositionalArgs: Bool, priority: UInt64, min!: UInt64 = UInt64.Min, max!: UInt64 = UInt64.Max)`** 
    
  设置位置参数的相关属性，只有调用该方法后，参数才会开始接收位置参数。该方法重载了两种输入方式，相同的输入参数的作用分别为：
    *   **`onlyPositionalArgs`:** 设置参数是否只接收位置参数输入，若为`true`，将无法在终端输入时调用到该参数，且`help`输出中也不会打印该参数的信息。
    *   **`priority` :**设置参数接收位置参数的顺序优先级，位置参数会首先按照最高优先级的`inputCountRange`进行传入，然后再处理优先级第二高的，以此类推，直到所有位置参数都已传入参数中。当前`0`为最高优先级，数字越大优先级越小
    
    重载的参数作用分别为：
    *   **`inputCountRange` :** 位置参数传入次数的区间。起始位为最小值，结束位为最大值，起始位必须≤结束位
    *   **`min, max` :** 位置参数传入次数的最小值和最大值。默认值为`UInt64.Min`和`UInt64.Max`，`min`必须≤`max`，允许两个值都不设置

    | 当`inputCountRange`和`min, max`同时存在时，优先选择`inputCountRange`


## 在动作中访问参数

在命令的 `action` 函数中，您会收到一个 `ArgMatch` 对象。此对象提供以类型安全的方式访问已解析参数的方法。

*   **`args.get<T>(name: String): T`:** 获取具有给定名称的参数的值，类型为 `T`。如果找不到参数或无法解析为 `T`，则抛出错误。 `T` 必须实现 `Parsable<T>`。
*   **`args.tryGet<T>(name: String): Option<T>`:** 尝试获取具有给定名称的参数的值，类型为 `T`，如果找不到参数或无法解析，则返回 `None`。
*   **`args.getArray<T>(name: String): Array<T>`:** 获取具有给定名称的参数的所有值，类型为 `T` 的数组。对于具有 `ArgAction.Append` 或默认值为列表的参数很有用。
*   **`args.tryGetArray<T>(name: String): Option<Array<T>>`:** 尝试获取所有值作为数组，如果找不到参数或任何值无法解析，则返回 `None`。
*   **`args.isEnabled(name: String): Bool`:** 检查标志参数（例如，带有 `ArgAction.SetTrue` 或 `ArgAction.SetFalse` 的参数）是否已启用（在命令行上存在）。
*   **`args.getString(name: String): String`:** 获取参数值作为 String。如果未找到，则抛出错误。
*   **`args.tryGetString(name: String): Option<String>`:** 尝试获取参数值作为 String，如果未找到，则返回 `None`。
*   **`args.getStringArray(name: String): Array<String>`:** 获取所有参数值作为 String 数组。
*   **`args.tryGetStringArray(name: String): Option<Array<String>>`:** 尝试获取所有参数值作为 String 数组，如果未找到，则返回 `None`。

## 帮助系统

该框架自动提供帮助系统。

*   **`--help` 标志:** 向任何命令或子命令添加 `--help` 将显示该命令的帮助信息。
*   **帮助信息内容:** 帮助信息包括：
    *   命令描述 (`.about()`)
    *   用法说明 (`.usage()`)
    *   子命令列表及描述
    *   参数列表 (描述, 短名称, 分组)
    
    > help不会打印位置参数设置了`onlyPositionalArgs = true`的参数信息

## 错误处理

框架提供基本的错误处理:

*   无效参数错误
*   缺少必需参数错误
*   参数解析错误

## 示例：更复杂的 CLI

```cj
package cangjie

import cli.*

// 创建 'file' 命令
func createFileCommand(): Command {
    Command("file")
        .about("与文件相关的操作。")
        .usage("mytool file [command] [options]")
        .action {
            args => println("请使用 'mytool file --help' 查看文件操作相关命令。")
        }
        .subcommands([createFileCountCommand(), createFileListCommand()]) // 批量添加子命令
}

// 创建 'file list' 子命令 - 使用批量参数添加
func createFileListCommand(): Command {
    Command("list")
        .about("列出文件")
        .usage("mytool file list [--all] [--size] [--time]")
        .args(
            Arg(r'a').help("显示所有文件"), // 仅短名称参数
            Arg("size").short(r's').help("显示文件大小"),
            Arg("time").short(r't').help("显示修改时间")
        )
        .action { args =>
            if (args.isEnabled("a")) {
                println("显示所有文件...")
            }
            if (args.isEnabled("size")) {
                println("显示文件大小...")
            }
            if (args.isEnabled("time")) {
                println("显示修改时间...")
            }
        }
}

// 创建 'file count' 子命令
func createFileCountCommand(): Command {
    Command("count")
        .about("计算文件中的行数或字数。")
        .usage("mytool file count --filepath <filepath> [--words]")
        .arg(Arg("filepath").help("文件路径").required(true))
        .arg(Arg("words").short(r'w').action(ArgAction.SetTrue).help("计算字数而不是行数"))
        .action {
            args =>
            let filepath = args.getString("filepath")
            let countWords = args.isEnabled("words")

            println("正在处理文件: ${filepath}")
            if (countWords) {
                println("正在计算字数...")
            // ... 字数统计逻辑 ...
            } else {
                println("正在计算行数...")
                // ... 行数统计逻辑 ...
            }
        }
}

// 创建 'network' 命令
func createNetworkCommand(): Command {
    Command("network")
        .about("网络相关实用程序。")
        .usage("mytool network [command] [options]")
        .action {
            args => println("请使用 'mytool network --help' 查看网络相关工具。")
        }
        .subcommand(createNetworkPingCommand())
}

// 创建 'network ping' 子命令
func createNetworkPingCommand(): Command {
    Command("ping")
        .about("向网络主机发送 ICMP 回显请求。")
        .usage("mytool network ping --host <host> [--count <count>]")
        .arg(Arg("host") // 链式添加参数
            .help("要 ping 的主机名或 IP 地址").required(true))
        .arg(Arg("count") // 链式添加参数
            .short(r'c').defaultValue(4).help("要发送的 ping 包数量"))
        .noInputBuild("--host", "localhost") // 无输入参数时默认ping本地主机
        .action {
            args =>
            let host = args.getString("host")
            let count = args.get<Int64>("count")

            println("正在 ping ${host} ${count} 次...")
            // ... ping 逻辑 ...
        }
}

// 创建'network download' 子命令
func createDownloadCommand(): Command {
    Command("download")
        .about("下载指定url的文件")
        .usage("mytool network download [--verbose] url")
        .arg(Arg("verbose").action(ArgAction.SetTrue).help("设置是否打印具体下载过程"))
        .arg(Arg("url").positionalArgsSet(true, 0, max: 1))
        .noInputBuild("--verbose", "https://example.com/default.txt") // 无输入参数时使用默认URL和详细模式
        .action {
            args => if (args.isEnabled("verbose")) {
                "开启详细过程打印\n" |> println
            }

            "正在下载${args.getString("url")}" |> println
        }
}

// 在main中创建根命令
main(): Unit {
    Command("ping")
        .about("向网络主机发送 ICMP 回显请求。")
        .usage("mytool network ping --host <host> [--count <count>]")
        .args(
            Arg("host")
                .help("要 ping 的主机名或 IP 地址")
                .required(true),
            Arg("count").short(r'c')
                .defaultValue(4)
                .help("要发送的 ping 包数量")
        )
        .action {
            args =>
            let host = args.getString("host")
            let count = args.get<Int64>("count")

            println("正在 ping ${host} ${count} 次...")
            // ... ping 逻辑 ...
        }
        .subcommands(
            createFileCommand(),
            createNetworkCommand(),
            createDownloadCommand()
        )
        .build()
}

```

## 贡献指南

欢迎任何形式的贡献，commit 风格信息参考[Conventional Commits（约定式提交规范）](https://www.conventionalcommits.org/zh-hans/v1.0.0/)。

## 开源协议

本项目在 [MulanPSL-2.0](./LICENSE) 协议下开源。

## 鸣谢

此程序在编写时参考了 [clap](https://github.com/clap-rs/clap) 的实现。