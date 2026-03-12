<h1 align="center"><strong>GUI4CJ - 仓颉 GUI 库</strong></h1>

<p align="center">
  <strong>🎨 跨平台 GUI 库 for 仓颉（Cangjie）语言</strong>
</p>

<p align="center">
  <a href="#-最佳实践效果">🎮 最佳实践</a> •
  <a href="#-特性">✨ 特性</a> •
  <a href="#-项目结构">📁 结构</a> •
  <a href="#-安装与构建">📦 安装与依赖</a> •
  <a href="#-使用-gui4cj-到你的项目">🚀 使用</a> •
  <a href="#-api-参考">📖 API</a> •
  <a href="#-示例代码">💡 示例</a> •
  <a href="#-常见问题">❓ FAQ</a>
</p>

---

**gui4cj** 是一个用仓颉（Cangjie）语言编写的**跨平台图形用户界面（GUI）库**，使用 OpenGL 进行硬件加速渲染。

- 🖥️ **跨平台** - 支持 Windows、macOS、Linux，一套代码多端运行
- ⚡ **高性能** - 基于 OpenGL 3.3+ 硬件加速，流畅渲染
- 🧩 **组件丰富** - 提供 Button、Label、Entry、Dialog、List、Table 等常用 UI 组件
- 🎨 **自定义绘图** - Canvas 画布支持矩形、圆形、线条、文本、图片等图元绘制
- 🔤 **中英文支持** - 内置 stb_truetype 字体渲染，完美显示中英文
- 📦 **一键构建** - `cjpm build` 自动编译 Native 库，无需手动配置

---

## 🎮 最佳实践效果

| 坦克大战游戏 | Dialog 弹窗 |
|:---:|:---:|
| <img src="images/tanke.PNG" width="100%"> | <img src="images/dialog.PNG" width="100%"> |

### 1. Tank Battle 坦克大战 (`examples/tank_battle/`)

**运行方式：**
```bash
cd examples/tank_battle
cjpm build && cjpm run
```

### 2. Dialog Demo (`examples/dialog_demo/`)

**运行方式：**
```bash
cd examples/dialog_demo
cjpm build && cjpm run
```

---

## ✨ 特性

### 🖥️ 跨平台支持
| 平台 | 架构 | 状态 |
|------|------|------|
| **Linux** | x86_64, aarch64 | ✅ 支持 |
| **macOS** | Intel (x86_64), Apple Silicon (ARM64) | ✅ 支持 |
| **Windows** | x86_64 | ✅ 支持 |

### 🎯 核心能力

| 特性 | 说明 |
|------|------|
| **硬件加速渲染** | 基于 OpenGL 3.3+，所有绑定调用 native 层 C 函数 |
| **中英文支持** | stb_truetype 动态字形缓存，支持 Unicode |
| **Canvas 画布** | 自定义绘图，支持矩形、圆形、线条、文本、图片 |
| **事件系统** | 键盘、鼠标事件回调 |
| **窗口管理** | 窗口创建、调整大小、固定尺寸、全屏等 |
| **主题系统** | 支持亮色/暗色主题，可自定义颜色风格 |
| **数据绑定** | 双向数据绑定支持 |
| **一键构建** | cjpm build 自动编译 Native 库和 Cangjie 库 |

### 🧩 UI 组件

#### 基础控件
- `Button` - 按钮（支持主要/危险/文本样式）
- `Label` - 标签（支持标题/副标题/正文样式）
- `Entry` - 输入框（支持密码/多行模式）
- `Check` - 复选框
- `RadioGroup` - 单选组
- `Select` - 下拉选择框
- `Slider` - 滑块

#### 布局容器
- `HBox` / `VBox` - 水平/垂直盒子布局
- `Grid` - 网格布局
- `Border` - 边框布局（上下左右中）
- `Stack` - 堆叠布局
- `Form` - 表单布局

#### 高级组件
- `Dialog` - 弹窗对话框
- `List` - 可滚动列表
- `Table` - 表格组件
- `Tree` - 树形控件
- `ProgressBar` - 进度条
- `Menu` / `ContextMenu` - 菜单组件
- `Toolbar` - 工具栏
- `Separator` - 分隔线

#### 画布绘图
- `Painter` - 绘图接口，支持：
  - `fillRect` / `strokeRect` - 矩形
  - `fillRoundedRect` - 圆角矩形
  - `fillCircle` / `strokeCircle` - 圆形
  - `drawLine` - 线条
  - `drawText` / `measureText` - 文本
  - `drawImage` - 图片

---

## 📁 项目结构

```
gui4cj/
├── cjpm.toml               # 项目配置
├── build.cj                # cjpm 构建脚本（自动编译 native 库）
├── README.md               # 说明文档
├── LICENSE                 # MIT 许可证
├── CHANGELOG.md            # 更新日志
├── scripts/                # 平台构建脚本
│   ├── build.sh            # 统一构建入口
│   ├── build_linux.sh      # Linux 构建
│   ├── build_macos.sh      # macOS 构建
│   ├── build_windows.bat   # Windows 构建 (CMD)
│   └── build_windows.ps1   # Windows 构建 (PowerShell)
├── native/                 # C 原生层代码
│   ├── CMakeLists.txt      # CMake 配置
│   ├── gui4cj_native.h     # C API 头文件
│   ├── gui4cj_native.c     # GLFW + OpenGL + 字体渲染实现
│   ├── glad/glad.h         # OpenGL 函数加载器
│   ├── stb_image.h         # 图片加载库
│   └── stb_truetype.h      # 字体光栅化库
├── examples/               # 示例程序
│   ├── dialog_demo/        # Dialog 弹窗示例
│   └── tank_battle/        # 坦克大战游戏示例
└── src/                    # 仓颉源代码
    ├── native_bindgen.cj   # C FFI 绑定层
    ├── driver.cj           # OpenGL 驱动（主循环、渲染）
    ├── window.cj           # 窗口管理、键盘事件、菜单
    ├── app.cj              # 应用程序入口、生命周期
    ├── types.cj            # 基础类型（Color, Size, Rect, Position, Insets）
    ├── theme.cj            # 主题系统（亮色/暗色）
    ├── widget.cj           # Widget 基类
    ├── layout.cj           # 布局容器（HBox, VBox, Border, Grid, Stack, Form）
    ├── button.cj           # 按钮组件
    ├── label.cj            # 标签组件
    ├── entry.cj            # 输入框组件
    ├── check.cj            # 复选框、单选组
    ├── select.cj           # 下拉选择组件
    ├── slider.cj           # 滑块组件
    ├── canvas.cj           # 画布及 CanvasObject 接口
    ├── canvasobjects.cj    # 画布对象（Rectangle, Circle, Line, Text, Image）
    ├── advanced.cj         # 高级组件（Dialog, Table, Tree, List, Menu）
    ├── binding.cj          # 数据绑定
    └── test/               # 单元测试
```

---

## 🏗️ 技术架构

```
┌─────────────────────────────────────────────────────────────┐
│                      用户应用层                              │
│         (App, Window, Dialog, Button, Label...)             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Cangjie UI 框架层                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │CanvasObj │  │  Layout  │  │  Theme   │  │  Binding │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      驱动层 (driver.cj)                      │
│         GLDriver (主循环) + GLPainter (绘制接口)             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  FFI 绑定层 (native_bindgen.cj)              │
│              Cangjie ←→ C 函数调用桥接                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   C Native 层 (gui4cj_native.c)             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │   GLFW   │  │  OpenGL  │  │stb_true- │  │stb_image │    │
│  │ (窗口)   │  │  (渲染)  │  │type(字体)│  │  (图片)  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       操作系统层                             │
│            Windows / macOS / Linux (X11/Wayland)            │
└─────────────────────────────────────────────────────────────┘
```

### 核心技术

| 层次 | 技术 | 说明 |
|------|------|------|
| **窗口管理** | GLFW | 跨平台窗口创建、输入事件处理 |
| **图形渲染** | OpenGL 3.3+ | 着色器渲染矩形、圆形、线条等图元 |
| **字体渲染** | stb_truetype | 动态光栅化 Unicode 字形（支持中英文） |
| **图像加载** | stb_image | PNG/JPG/GIF 纹理加载 |
| **FFI 桥接** | Cangjie @C foreign | Cangjie 调用 C 函数 |
| **构建系统** | cjpm + CMake | Cangjie 包管理 + Native 编译 |

---

## 📦 安装与构建

### 依赖说明

| 依赖 | 说明 | 用途 |
|:---|:---|:---|
| **仓颉 SDK** | >= 1.0.4 | Cangjie 编译器和包管理器 |
| **CMake** | >= 3.10 | Native C 代码编译 |
| **GLFW** | 3.x | 跨平台窗口管理和输入处理 |
| **OpenGL** | 3.3+ | 图形渲染（通常系统自带） |
| **libpng** | - | PNG 图片加载支持 |
| **C 编译器** | GCC/Clang/MSVC | 编译 Native 层代码 |

> 💡 **stb_image** 和 **stb_truetype** 已内置于 `native/` 目录，无需额外安装。

---

### 🐧 Linux

#### 1. 安装依赖

**Ubuntu/Debian:**
```bash
sudo apt install libglfw3-dev libpng-dev libgl1-mesa-dev cmake build-essential
```

**Fedora:**
```bash
sudo dnf install glfw-devel libpng-devel mesa-libGL-devel cmake gcc gcc-c++
```

**Arch Linux:**
```bash
sudo pacman -S glfw-x11 libpng mesa cmake
```

#### 2. 构建

```bash
cd /path/to/gui4cj
cjpm build
```

#### 3. 运行测试

放开 `cjpm.toml` 测试注释
```bash
cjpm test
```

---

### 🍎 macOS

#### 1. 安装依赖

```bash
brew install glfw libpng cmake
```

#### 2. 构建

```bash
cd /path/to/gui4cj
cjpm build
```

---

### 🪟 Windows

#### 1. 安装依赖

- **CMake**: https://cmake.org/download/
- **Visual Studio 2022** (带 C++ 工具) 或 **MinGW-w64**
- **GLFW**: https://www.glfw.org/download.html
- **libpng**: 可通过 vcpkg 安装

#### 2. 构建

```powershell
cd C:\path\to\gui4cj
cjpm build
```

---

## 🚀 使用 gui4cj 到你的项目

### 1. 创建项目

创建 `cjpm.toml`（完整配置）:

```toml
[package]
  cjc-version = "1.0.3"
  name = "my_app"
  version = "1.0.0"
  output-type = "executable"
  target-dir = "target"
  src-dir = "src"

[dependencies]
  gui4cj = { path = "/path/to/gui4cj" }

# Linux x86_64
[target.x86_64-unknown-linux-gnu]
  link-option = "-lgui4cj_native -lGL -lglfw -lpng -lm -ldl -lpthread"

# Linux aarch64
[target.aarch64-unknown-linux-gnu]
  link-option = "-lgui4cj_native -lGL -lglfw -lpng -lm -ldl -lpthread"

# macOS Intel
[target.x86_64-apple-darwin]
  link-option = "-lgui4cj_native -framework OpenGL -framework Cocoa -framework IOKit -framework CoreVideo -lglfw -lpng"

# macOS Apple Silicon
[target.aarch64-apple-darwin]
  link-option = "-lgui4cj_native -framework OpenGL -framework Cocoa -framework IOKit -framework CoreVideo -lglfw -lpng"

# Windows MinGW
[target.x86_64-pc-windows-gnu]
  link-option = "-lgui4cj_native -lopengl32 -lgdi32 -luser32 -lglfw3 -lpng"

# Windows MSVC
[target.x86_64-pc-windows-msvc]
  link-option = "-lgui4cj_native -lopengl32 -lgdi32 -luser32"
```

> 💡 `link-option` 用于链接 gui4cj 的 native 库和系统依赖库。

### 2. 编写代码

创建 `src/main.cj`:

```cangjie
package my_app

import gui4cj.*

main(): Int64 {
    let app = App()
    let window = app.newWindow("Hello gui4cj")
    window.resize(Size(400.0, 300.0))
    
    let label = Label("Hello, World!")
    window.setContent(label)
    
    window.show()
    app.run()
    return 0
}
```

### 3. 构建运行

```bash
cjpm build
cjpm run
```

---

## 📖 API 参考

### 核心类型 (types.cj)

| 类型 | 分类 | 说明 | 主要属性/方法 |
|------|------|------|--------------|
| `Position` | struct | 二维坐标 | `x`, `y`, `add()`, `subtract()`, `distanceTo()` |
| `Size` | struct | 尺寸 | `width`, `height`, `isZero()`, `max()`, `min()` |
| `Rect` | struct | 矩形区域 | `x`, `y`, `width`, `height`, `contains()`, `intersects()`, `center` |
| `Color` | struct | RGBA 颜色 | `r`, `g`, `b`, `a`, `fromHex()`, `fromRGB()`, `withAlpha()` |
| `Insets` | struct | 边距 | `top`, `right`, `bottom`, `left`, `horizontal`, `vertical` |
| `Colors` | class | 预定义颜色 | `black`, `white`, `red`, `green`, `blue`, `yellow`, `gray` 等 |
| `TextAlign` | enum | 水平对齐 | `Left`, `Center`, `Right` |
| `TextVAlign` | enum | 垂直对齐 | `Top`, `Middle`, `Bottom` |

### 应用程序 (app.cj)

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `App` | class | 应用程序类 | `newWindow()`, `run()`, `quit()`, `settings()` |
| `Application` | interface | 应用接口 | `uniqueID()`, `newWindow()`, `run()`, `quit()` |
| `Settings` | interface | 设置接口 | `theme()`, `setTheme()`, `scale()`, `setScale()` |
| `Lifecycle` | interface | 生命周期 | `onStart()`, `onStop()` |
| `Preferences` | interface | 首选项存储 | `getString()`, `setString()`, `getInt()`, `setInt()` |
| `Clipboard` | interface | 剪贴板 | `content()`, `setContent()` |
| `Resource` | interface | 资源接口 | `name()`, `content()` |
| `Notification` | class | 系统通知 | `title`, `content` |

**快捷函数:**

| 函数 | 说明 |
|------|------|
| `runApp(title, content)` | 创建并运行应用 |
| `runAppWithSize(title, width, height, content)` | 创建指定尺寸窗口并运行 |

### 窗口 (window.cj)

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `Window` | interface | 窗口接口 | `show()`, `hide()`, `close()`, `resize()`, `setContent()` |
| | | | `setTitle()`, `setFixedSize()`, `setFullScreen()`, `centerOnScreen()` |
| | | | `setOnKeyEvent()`, `isKeyPressed()`, `setCloseIntercept()` |
| `MainMenu` | class | 主菜单 | `append()`, `items()` |
| `MenuItem` | class | 菜单项 | `label()`, `setAction()`, `trigger()`, `setSubmenu()` |
| `Shortcut` | class | 快捷键 | `key()`, `modifiers()` |
| `KeyCode` | struct | 键码 | `code()` |
| `Keys` | class | 键码常量 | `W`, `A`, `S`, `D`, `Up`, `Down`, `Left`, `Right`, `Space`, `Escape`, `Enter` |
| `Modifiers` | class | 修饰键 | `None`, `Shift`, `Control`, `Alt`, `Super` |
| `MouseButton` | enum | 鼠标按钮 | `Left`, `Right`, `Middle` |

### 画布 (canvas.cj)

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `Canvas` | interface | 画布接口 | `content()`, `setContent()`, `size()`, `refresh()`, `focus()`, `unfocus()` |
| `CanvasObject` | interface | 画布对象 | `render()`, `position()`, `size()`, `move()`, `resize()` |
| | | | `show()`, `hide()`, `visible()`, `setVisible()`, `refresh()`, `objects()` |
| `Focusable` | interface | 可获焦 | `focusGained()`, `focusLost()` |
| `Tappable` | interface | 可点击 | `tapped()` |
| `Hoverable` | interface | 可悬停 | `mouseIn()`, `mouseOut()`, `mouseMoved()` |
| `Scrollable` | interface | 可滚动 | `scrolled()` |
| `Draggable` | interface | 可拖拽 | `dragStart()`, `dragged()`, `dragEnd()` |
| `TypedKey` | interface | 键盘输入 | `keyDown()`, `keyUp()` |
| `TypedRune` | interface | 字符输入 | `runeTyped()` |

### 绘图 (Painter)

| 类型 | 分类 | 说明 |
|------|------|------|
| `Painter` | interface | 绘图接口 |

| 方法 | 说明 |
|------|------|
| `fillRect(rect, color)` | 填充矩形 |
| `strokeRect(rect, color, thickness)` | 绘制矩形边框 |
| `fillRoundedRect(rect, radius, color)` | 填充圆角矩形 |
| `fillCircle(center, radius, color)` | 填充圆形 |
| `strokeCircle(center, radius, color, thickness)` | 绘制圆形边框 |
| `drawLine(start, end, color, thickness)` | 绘制线条 |
| `drawText(text, position, color)` | 绘制文本 |
| `measureText(text)` | 测量文本尺寸，返回 Size |
| `drawImage(image, rect)` | 绘制图片 |
| `setClipRect(rect)` | 设置裁剪区域 |
| `clearClipRect()` | 清除裁剪区域 |

### 基础组件

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `Label` | class | 标签 | `text()`, `setText()`, `textColor()`, `setTextColor()` |
| `Button` | class | 按钮 | `text()`, `setText()`, `setOnTapped()`, `setImportance()` |
| `Entry` | class | 输入框 | `text()`, `setText()`, `placeholder()`, `setOnChanged()` |
| `Check` | class | 复选框 | `checked()`, `setChecked()`, `setOnChanged()` |
| `RadioGroup` | class | 单选组 | `options()`, `selected()`, `setOnChanged()` |
| `Select` | class | 下拉选择 | `options()`, `setOptions()`, `selected()`, `setOnChanged()` |
| `Slider` | class | 滑块 | `value()`, `setValue()`, `min()`, `max()`, `setOnChanged()` |

**快捷函数:**

| 函数 | 说明 |
|------|------|
| `label(text)` | 创建标签 |
| `heading(text)` | 创建标题标签 |
| `button(text, onTapped)` | 创建按钮 |
| `primaryButton(text, onTapped)` | 创建主要按钮 |
| `entry()` | 创建输入框 |
| `passwordEntry()` | 创建密码输入框 |
| `check(text, onChanged)` | 创建复选框 |
| `select(options, onChanged)` | 创建下拉选择 |
| `slider(min, max, onChanged)` | 创建滑块 |

### 布局容器 (layout.cj)

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `Layout` | interface | 布局接口 | `layout()`, `minSize()` |
| `Container` | class | 容器基类 | `addChild()`, `removeChild()`, `setPadding()` |
| `HBox` | class | 水平盒子 | `setSpacing()` |
| `VBox` | class | 垂直盒子 | `setSpacing()` |
| `Grid` | class | 网格布局 | `setRows()`, `setCols()`, `setSpacing()` |
| `Border` | class | 边框布局 | `setTop()`, `setBottom()`, `setLeft()`, `setRight()`, `setCenter()` |
| `Stack` | class | 堆叠布局 | - |
| `Form` | class | 表单布局 | `appendItem()` |
| `FormItem` | class | 表单项 | `label`, `field` |

**快捷函数:**

| 函数 | 说明 |
|------|------|
| `hBox(children)` | 创建水平盒子 |
| `vBox(children)` | 创建垂直盒子 |
| `grid(columns, children)` | 创建网格布局 |
| `stack(children)` | 创建堆叠布局 |
| `center(child)` | 创建居中容器 |
| `padded(padding, child)` | 创建带内边距容器 |

### 高级组件 (advanced.cj)

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `Dialog` | class | 对话框 | `show()`, `hide()`, `addButton()`, `clearButtons()`, `setOnResult()` |
| `DialogType` | enum | 对话框类型 | `Information`, `Confirmation`, `Warning`, `Error` |
| `DialogResult` | enum | 结果类型 | `Confirm`, `Cancel`, `Yes`, `No`, `Ok` |
| `List` | class | 列表 | `setItems()`, `appendItem()`, `selectedIndex()`, `setOnSelected()` |
| `Table` | class | 表格 | `setColumns()`, `setRows()`, `setOnCellSelected()` |
| `TableColumn` | class | 表格列 | `header`, `width` |
| `Tree` | class | 树形控件 | `setRoot()`, `expandAll()`, `collapseAll()` |
| `TreeNode` | class | 树节点 | `text()`, `children()`, `addChild()`, `expanded()` |
| `ProgressBar` | class | 进度条 | `value()`, `setValue()`, `min()`, `max()` |
| `Menu` | class | 菜单 | `addItem()`, `show()` |
| `MenuAction` | class | 菜单动作 | `label()`, `action()` |
| `ContextMenu` | class | 右键菜单 | `addItem()`, `showAt()` |
| `Toolbar` | class | 工具栏 | `addItem()` |
| `Separator` | class | 分隔线 | - |

**快捷函数:**

| 函数 | 说明 |
|------|------|
| `showInfo(title, message)` | 显示信息对话框 |
| `showWarning(title, message)` | 显示警告对话框 |
| `showError(title, message)` | 显示错误对话框 |
| `showConfirm(title, message, onResult)` | 显示确认对话框 |
| `list(items, onSelected)` | 创建列表 |
| `table(columns)` | 创建表格 |
| `tree(root)` | 创建树 |
| `progressBar()` | 创建进度条 |

### 画布对象 (canvasobjects.cj)

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `Rectangle` | class | 矩形 | `setColor()`, `setCornerRadius()` |
| `Circle` | class | 圆形 | `setColor()`, `setRadius()` |
| `Line` | class | 线条 | `setColor()`, `setThickness()` |
| `Text` | class | 文本 | `setText()`, `setColor()` |
| `Image` | class | 图片 | `setPath()`, `setFillMode()` |
| `LinearGradient` | class | 线性渐变 | `setColors()`, `setDirection()` |
| `ImageFillMode` | enum | 图片填充模式 | `Stretch`, `Contain`, `Cover`, `Tile` |

**快捷函数:**

| 函数 | 说明 |
|------|------|
| `rectangle(size, color)` | 创建矩形 |
| `circle(radius, color)` | 创建圆形 |
| `line(start, end, color)` | 创建线条 |
| `text(content, color)` | 创建文本 |
| `image(path)` | 创建图片 |

### 数据绑定 (binding.cj)

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `DataBinding<T>` | interface | 数据绑定接口 | `get()`, `set()`, `addListener()` |
| `BindString` | class | 字符串绑定 | `get()`, `set()` |
| `BindInt` | class | 整数绑定 | `get()`, `set()` |
| `BindFloat` | class | 浮点绑定 | `get()`, `set()` |
| `BindBool` | class | 布尔绑定 | `get()`, `set()` |
| `BindList<T>` | class | 列表绑定 | `get()`, `append()`, `remove()` |

**快捷函数:**

| 函数 | 说明 |
|------|------|
| `bindString(value)` | 创建字符串绑定 |
| `bindInt(value)` | 创建整数绑定 |
| `bindFloat(value)` | 创建浮点绑定 |
| `bindBool(value)` | 创建布尔绑定 |
| `bindLabel(label, binding)` | 绑定标签 |
| `bindEntry(entry, binding)` | 绑定输入框 |
| `bindCheck(check, binding)` | 绑定复选框 |
| `bindSlider(slider, binding)` | 绑定滑块 |

### 主题 (theme.cj)

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `Theme` | interface | 主题接口 | `backgroundColor()`, `foregroundColor()`, `buttonColor()` 等 |
| `ThemeVariant` | enum | 主题变体 | `Light`, `Dark`, `System` |
| `DefaultTheme` | class | 默认亮色主题 | - |
| `DarkTheme` | class | 暗色主题 | - |

**快捷函数:**

| 函数 | 说明 |
|------|------|
| `currentTheme()` | 获取当前主题 |

### 纹理 (native_bindgen.cj)

| 类型 | 分类 | 说明 | 主要方法 |
|------|------|------|---------|
| `Texture` | class | 纹理类 | `width()`, `height()`, `size()`, `destroy()` |

---

## 💡 示例代码

### 示例 1：Hello World

```cangjie
package hello

import gui4cj.*

main(): Int64 {
    let app = App()
    let window = app.newWindow("Hello gui4cj")
    window.resize(Size(400.0, 300.0))
    
    let lbl = Label("Hello, World!")
    window.setContent(lbl)
    
    window.show()
    app.run()
    return 0
}
```

### 示例 2：自定义绘图 (CanvasObject)

```cangjie
package drawing

import gui4cj.*
import std.collection.*

public class MyDrawing <: CanvasObject {
    private var _position: Position = Position(0.0, 0.0)
    private var _size: Size = Size(400.0, 300.0)
    private var _visible: Bool = true
    
    public func minSize(): Size { return Size(100.0, 100.0) }
    public func position(): Position { return _position }
    public func size(): Size { return _size }
    public func visible(): Bool { return _visible }
    public func move(pos: Position): Unit { _position = pos }
    public func resize(size: Size): Unit { _size = size }
    public func show(): Unit { _visible = true }
    public func hide(): Unit { _visible = false }
    public func setVisible(v: Bool): Unit { _visible = v }
    public func refresh(): Unit {}
    public func objects(): ArrayList<CanvasObject> { return ArrayList<CanvasObject>() }
    
    public func render(painter: Painter, bounds: Rect): Unit {
        // 绘制背景
        painter.fillRect(bounds, Color(0.1, 0.1, 0.2, 1.0))
        
        // 绘制红色矩形
        painter.fillRect(Rect(50.0, 50.0, 100.0, 80.0), Colors.red)
        
        // 绘制绿色圆形
        painter.fillCircle(Position(250.0, 100.0), 40.0, Colors.green)
        
        // 绘制黄色线条
        painter.drawLine(Position(50.0, 200.0), Position(350.0, 200.0), Colors.yellow, 2.0)
        
        // 绘制白色文本
        painter.drawText("gui4cj 自定义绘图", Position(100.0, 250.0), Colors.white)
    }
}

main(): Int64 {
    let app = App()
    let window = app.newWindow("Custom Drawing")
    window.resize(Size(400.0, 300.0))
    window.setContent(MyDrawing())
    window.show()
    app.run()
    return 0
}
```

### 示例 3：键盘事件处理

```cangjie
package keyboard

import gui4cj.*

main(): Int64 {
    let app = App()
    let window = app.newWindow("Keyboard Demo")
    window.resize(Size(400.0, 300.0))
    
    // 设置键盘事件回调
    window.setOnKeyEvent { key, pressed =>
        if (pressed) {
            if (key.code() == Keys.Escape.code()) {
                window.close()
            } else if (key.code() == Keys.Space.code()) {
                println("Space pressed!")
            }
        }
    }
    
    let lbl = Label("Press ESC to exit, Space to print")
    window.setContent(lbl)
    window.show()
    app.run()
    return 0
}
```

### 示例 4：Dialog 对话框

```cangjie
package dialog

import gui4cj.*

main(): Int64 {
    let app = App()
    let window = app.newWindow("Dialog Demo")
    window.resize(Size(400.0, 300.0))
    
    let dialog = Dialog("确认", "是否继续操作？", DialogType.Confirmation)
    dialog.clearButtons()
    dialog.addButton("确定", DialogResult.Confirm)
    dialog.addButton("取消", DialogResult.Cancel)
    
    dialog.setOnResult { result =>
        match (result) {
            case DialogResult.Confirm => println("用户点击了确定")
            case DialogResult.Cancel => println("用户点击了取消")
            case _ => ()
        }
    }
    
    dialog.show()
    window.setContent(dialog)
    window.show()
    app.run()
    return 0
}
```

---

## ❓ 常见问题

### Q: 构建时报错找不到 glfw 或其他依赖？

确保已安装所有前置依赖（参见"安装与构建"章节）。

### Q: 运行时报错找不到 libgui4cj_native.so？

尝试重新构建：
```bash
cjpm clean
cjpm build
```

### Q: 链接时报错找不到 gui4cj_native？

确保用户项目的 `cjpm.toml` 中配置了正确的 `link-option`：
```toml
[target.x86_64-unknown-linux-gnu]
  link-option = "-lgui4cj_native -lGL -lglfw -lpng -lm -ldl -lpthread"
```

### Q: 如何固定窗口大小？

```cangjie
window.setFixedSize(true)
```

### Q: 如何处理键盘输入？

```cangjie
// 方式 1：事件回调（适合单次按键）
window.setOnKeyEvent { key, pressed =>
    if (key.code() == Keys.Space.code() && pressed) {
        // 处理空格键按下
    }
}

// 方式 2：轮询状态（适合游戏循环中的长按检测）
if (window.isKeyPressed(Keys.W)) {
    // W 键被按住
}
```

---

## 📋 其他

| 项目 | 说明 |
|:---|:---|
| **依赖** | 仓颉 SDK >= 1.0.4 |
| **许可证** | [Apache License](./LICENSE) |
| **贡献** | 欢迎提交 Issue 和 Pull Request！ |

---

<p align="center">
  Made with ❤️ for the Cangjie community
</p>

