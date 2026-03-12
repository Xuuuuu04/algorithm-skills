<div align="center">
<h1>终端输出文本颜色与格式控制的ANSI转义序列构造器</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.1.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v0.55.3-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/state-孵化-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-HOS/Cloud-brightgreen" style="display: inline-block;" />
</p>

## <img alt="" src="./doc/assets/readme/readme-icon-introduction.png" style="display: inline-block;" width=3%/> 1 介绍

以ANSI转义序列生成为基础，实现仓颉语言控制台应用程序中输出文本的颜色、样式、输出位置和屏幕区域擦除等功能，以提升UI质量和用户体验。

### 1.1 项目特性
+ 🚀 ANSI转义序列生成
+ 💡 支持3/4/8/24bit颜色
+ 💡 支持自定义调色板
+ 💡 支持粗体、斜体、模糊、隐藏、闪烁、下划线、删除线、反转等样式的设置和重置
+ 💡 支持光标移动
+ 💡 支持屏幕区域擦除
+ 💪 ANSI转义序列的函数式命令
+ 💪 支持宏
+ 💪 文本输出样式控制的快捷工具类（ColorText）

### 1.2 项目计划
1. [ ] ANSI转义序列生成，基于ANSI转义序列的文本输出控制
2. [ ] 文本屏幕窗口（SDI）
3. [ ] 文本屏幕窗口（MDI）
4. [ ] 多线程支持

## <img alt="" src="./doc/assets/readme/readme-icon-framework.png" style="display: inline-block;" width=3%/> 2 架构

### 2.1 项目结构

```shell
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── cjpm.toml
├── doc
    ├── assets
      └── ...               文档中使用的图片等资源       
    ├── design.md           设计方案
    └── feature_api.md      接口说明
├── src
    ├── core
        ├── c0.cj           C0符号定义
        ├── c1.cj           C1符号定义
        ├── csi.cj          CSI序列生成函数
        ├── osc.cj          OSC序列生成函数
        ├── ansicolor.cj    AnsiColor类型定义，背景色和前景色控制序列生成
        ├── ansistyle.cj    AnsiStyle，输出字符样式定义，设置和取消设置控制序列生成
        └── ...             字体选择等控制序列生成器
    ├── macros
        └── csi_marcos.cj   基于转义序列的输出控制宏集合
    ├── helpers
        ├── csi_builder.cj  转义序列构造器(为旧版本保留)
        ├── colorize.cj     着色器助手
        ├── textstyle.cj    样式控制助手（颜色和样式的整体处理助手）
        ├── cusor.cj        光标控制助手
        └── screen.cj       屏幕擦除助手
    ├── utils
        ├── colortext.cj    样式化文本工具类
        └── commands.cj     转义序列的函数化支持
    └── test
        └── color_test.cj   ANSI转义序列颜色控制序列测试
└── ...
```

## <img alt="" src="./doc/assets/readme/readme-icon-compile.png" style="display: inline-block;" width=3%/> 3 使用说明

### 3.1 编译构建（Win/Linux/Mac）
在工程根目录下运行：  
`cjpm build`

### 3.2 单元测试
在工程根目录下运行：  
`cjpm test`

### 3.4 功能示例
1. 颜色和样式

```cangjie
    //标准色
    let colors: Array<AnsiColor> = [
        AnsiColor.Black,
        AnsiColor.Red,
        AnsiColor.Green,
        AnsiColor.Yellow,
        AnsiColor.Blue,
        AnsiColor.Magenta,
        AnsiColor.Cyan,
        AnsiColor.White,
        AnsiColor.BrightBlack,
        AnsiColor.BrightRed,
        AnsiColor.BrightGreen,
        AnsiColor.BrightYellow,
        AnsiColor.BrightBlue,
        AnsiColor.BrightMagenta,
        AnsiColor.BrightCyan,
        AnsiColor.BrightWhite,
        AnsiColor.Default
    ]
    println("标准色")
    for (c in colors[0 .. 8]) {
        env.getStdOut().write(Colorize.background(c) + "   " + c.toString() + "   " + Colorize.reset() + "  ")
    }
    println()
    //高强度颜色
    println("高强度色")
    for (c in colors[8 .. 16]) {
        env.getStdOut().write(Colorize.background(c) + " " + c.toString() + " " + Colorize.reset() + "  ")
    }
    println()
    //256色颜色
    println("256色")
    for ( cv in 0 .. 255) {
        if (cv % 20 == 0) {
            println()
        }
        env.getStdOut().write(Colorize.background(AnsiColor.Color8b(UInt8(cv))) + " " + cv.format("03") + " " + Colorize.reset())
    }
    println()

    //真彩色
    println("真彩色")
    env.getStdOut().write(Colorize.background(0u8, 134u8, 139u8) + " 0x00868B " + Colorize.reset() + "  " + Colorize.reset())
    env.getStdOut().write(Colorize.background(AnsiColor.Color24b(0x00868B)) + " 0x00868B " + Colorize.reset() + "  " + Colorize.reset())
    println()
```
<img alt="效果图" src="./doc/assets/readme/colors.png" style="display: inline-block;" width=80%/>

2. 自定义调色板
```cangjie
    //颜色索引模式
    let palette = HashMap<String, UInt32>([
        ("BROWN", 0xA52A2A),
        ("DARKGOLDENROD", 0x08860B),
        ("BURLYWOOD", 0x0EB887) //,
        //......
    ])
    env.getStdOut().write(Colorize.background(AnsiColor.createFrom("BROWN", palette)) + " BROWN " + Colorize.reset() + "  " + Colorize.reset())
    env.getStdOut().write(Colorize.background(AnsiColor.createFrom("DARKGOLDENROD", palette)) + " DARKGOLDENROD " + Colorize.reset() + "  " + Colorize.reset())

    println("\n\n")

    let palette = HashMap<String, (r: Byte, g: Byte, b: Byte)>([
        ("DARKCYAN", (0x00u8, 0x8bu8, 0x8bu8)),
        ("DARKGRAY", (0x09u8, 0xA9u8, 0xA9u8)),
        ("DARKGREEN", (0x00u8, 0x64u8, 0x00u8)) //,
        // ......
    ])
    env.getStdOut().write(Colorize.background(AnsiColor.createFrom("DARKCYAN", palette)) + " DARKCYAN " + Colorize.reset() + "  " + Colorize.reset())
    env.getStdOut().write(Colorize.background(AnsiColor.createFrom("DARKGREEN", palette)) + " DARKGREEN " + Colorize.reset() + "  " + Colorize.reset())

    println()
```
3. 助手模式

可使用的助手有屏幕助手、光标助手、颜色助手和文本样式助手，其中文本样式助手包括颜色和样式设置。
``` cangjie
    Screen.clear()      //清除屏幕
    println(Colorize.foreground(AnsiColor.Red) + "hello world." + Colorize.reset()) //前景色着色
    println(Colorize.fbColor(AnsiColor.Red， ANSIColor.Color8b(189u8)) + "hello world." + Colorize.reset()) /着色前景和背景
    Cursor.to(3, 21) //将光标定位于第3行，第21列
    Cursor.toCol(42) //将光标移动到其所在行的第42列
```
4. 函数命令模式
```
    import ansies.utils.*

    setForeground(AnsiColor.Blue)   // 设置前景色
    gotoXY(4, 8)                    // 移动光标
    env.getStdOut().write("this is a test.")
    reset()                         // 重置色彩和样式
```
5. 着色文本类ColorText模式
```
    ColorText("这是一个测试。")
        .color("red", "white")      //设置前景色和背景色
        .styles(AnsiStyle.ITALIC)   //设置样式
        .printAt(11, 23)            //打印到控制台的确定位置
```


**[使用文档](doc/design.md)**

## <img alt="" src="./doc/assets/readme/readme-icon-contribute.png" style="display: inline-block;" width=3%/> 4 参与贡献

本项目由 vchuoshen6 实现并维护。技术支持和意见反馈请提Issue。

本项目基于 木兰宽松许可证 2.0，欢迎给我们提交PR，欢迎参与任何形式的贡献。

本项目commiter：[@vchuoshen6](https://gitcode.com/vchuoshen6)