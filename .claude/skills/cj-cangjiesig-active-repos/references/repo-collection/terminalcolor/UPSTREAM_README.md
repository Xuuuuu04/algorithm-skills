# terminalcolor

[![Crates.io](https://img.shields.io/badge/terminalcolor-0.2.1-2A6FDD)](https://gitcode.com/Cangjie-SIG/terminalcolor/overview) [![Crates.io](https://img.shields.io/badge/license-MulanPSL2-3DA638)](https://gitcode.com/Cangjie-SIG/terminalcolor/blob/main/LICENSE)


> 单元测试在每日构建版 1.1.0-alpha.20251228020001 全部通过，认为已支持 1.1.0-alpha.20251228020001 <br/>


Coloring terminal so simple, you already know how to do it!

```java
    "this is blue".colored.blue()
    "this is red".colored.red()
    "this is red with bold".colored.red().bold()
    "this is also red with bold".colored.bold().red()
    "bright colors are welcome as well".colored.brightGreen()
    "you can also make bold comments".colored.bold()
    '${"or use".colored.cyan()} ${"any".colored.italic()} ${"style type".colored.yellow()}'
    "or change advice. This is red".colored.yellow().blue().red()
    "or clear things up. This is default color and style".colored.red().bold().clear()
    "or just clear font color".colored.white().underline().clearFgColor()
    "or just clear style".colored.black().blink().clearStyle()
    "any order is allowed,it just work".colored.reversed().strikethrough().brightMagenta()
```
```java
// need import
// import terminalcolor.color.Color
// import terminalcolor.style.Style
"this is another way to write red and bold".colored(color: TerminalColor.Red, style: TerminalStyle.Bold)
"only color is ok".colored(color: TerminalColor.Blue)
"only style is welcome as well".colored(style: TerminalStyle.Underline)
"font color,background color and style".colored(fgcolor: TerminalColor.Red, bgcolor: TerminalColor.Cyan,
        style: TerminalStyle.Italic)
```


![图片.png](https://raw.gitcode.com/user-images/assets/4027567/5ea4e8b2-043c-4438-83ac-cd5fa53cf5eb/a.png)

![图片.png](https://raw.gitcode.com/user-images/assets/4027567/743f03e8-0e21-430b-ae7e-5f02e873e918/b.png)

This is the effect of all colors and styles.(Hidden style can't be displayed)

![Peek 2024-07-30 00-38.gif](https://raw.gitcode.com/user-images/assets/4027567/743d0285-3357-41b8-9843-f55bd572d35e/c.gif)

## How to use

1. Add this in your `cjpm.toml`:

```toml
[dependencies]
terminalcolor = { git = "https://gitcode.com/Cangjie-SIG/terminalcolor.git", tag = "0.2.0" }
```
2. run `cjpm update` to update cjpm.lock file

3. add this to your code:

```java
    import terminalcolor.Colorize

    // color function return `ColoredString` type
    // but you can treat is as String
    main():Unit {
        // Ta-da!red text is shown
        println("this is red".colored.red())
    }
```

## Features
- 4-bit(16) ANSI colors support
- 8 style support
- Great editor support. Completion everywhere. Less time debugging.
- Don't intend to support 256 colors
- Don't intend to support truecolors
- Test on Linux、Windows 10 21H2（powershell and cmd）、macOS 11 Big Sur

completion

![image.png](https://raw.gitcode.com/user-images/assets/4027567/337564f2-a38b-4f4b-af16-e1d202c89c4c/d.png)



#### Colors:

- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- brightblack
- brightred
- brightgreen
- brightyellow
- brightblue
- brightmagenta
- brightcyan
- brightwhite

#### Styles:

- bold
- dimmed
- italic
- underline
- blink
- reversed
- hidden
- strikethrough


## Credits
This library wouldn't have been the same without the marvelous rust crate [colored](https://github.com/colored-rs/colored).


## Minimum Supported Cangjie Version (cjnative)
The minimum version is `1.0.0`.

## License

[Mulan Permissive Software License v2](https://opensource.org/license/mulanpsl-2-0). See the
[LICENSE](https://gitcode.com/xffish/terminalcolor/blob/main/LICENSE) file at the
root of the repository.


## Contributors

- xffish: [@xffsh](https://gitcode.com/xffish)

## 更新列表
从0.2.0之后的版本开始列出