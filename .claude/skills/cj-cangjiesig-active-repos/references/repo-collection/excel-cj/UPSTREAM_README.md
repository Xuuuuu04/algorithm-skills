<div align="center">
<h1>excel-cj</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v1.0.4-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/build-pass-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.x-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjcov-NA-red" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/project-open-brightgreen" style="display: inline-block;" />
</p>

# excel-cj

一个使用仓颉（Cangjie）语言开发的 Excel 文件处理库，支持 XLSX、CSV 格式的读取和写入。

## 功能特性

- ✅ **XLSX 文件支持**
  - 读取 XLSX 文件
  - 写入 XLSX 文件
  - 支持多工作表
  - 支持共享字符串表

- ✅ **CSV 文件支持**
  - 读取 CSV 文件
  - 写入 CSV 文件
  - 可配置分隔符、引用符等参数
  - 自动处理特殊字符转义

- ✅ **数据结构**
  - Workbook（工作簿）- 管理多个工作表
  - Sheet（工作表）- 存储表格数据
  - Cell（单元格）- 存储单个值，支持多种数据类型


## 注意事项

1. **XLSX 支持**：完整支持生成 XLSX 文件，使用自实现的 ZIP 格式生成器（无需外部依赖）。

2. **CSV 处理**：支持从 CSV 字符串解析数据和导出为 CSV 字符串/文件，使用标准 RFC 4180 格式。

3. **编码**：所有字符串处理默认使用 UTF-8 编码。

4. **坐标系统**：行和列索引从 0 开始，Excel 坐标（如 "A1"）可通过辅助函数转换。

5. **数据类型**：单元格支持字符串、数字、布尔值和空值类型，通过 `CellType` 枚举区分。

6. **文件格式**：生成的 XLSX 文件可直接用 Microsoft Excel、WPS、LibreOffice 等软件打开。


## 目录结构

```
excel-cj/
├── src/
│   ├── cj_excel.cj      # 主模块，导出公共接口
│   ├── cell.cj          # 单元格定义
│   ├── sheet.cj         # 工作表定义
│   ├── workbook.cj      # 工作簿定义
│   ├── csv_handler.cj   # CSV 读写处理
│   ├── xlsx_handler.cj  # XLSX 读写处理
│   ├── zip_writer.cj    # ZIP 文件格式生成器
│   ├── zip_reader.cj    # ZIP 文件格式读取器
│   └── test/
│       └── excel_test.cj    # 单元测试
├── cjpm.toml            # 项目配置
└── README.md            # 项目文档
```

## API 文档

### Workbook 类

工作簿是 Excel 文件的顶层容器，包含多个工作表。

| 方法 | 说明 |
|------|------|
| `init()` | 创建空工作簿 |
| `createSheet(name: String): Sheet` | 创建新工作表 |
| `getSheet(index: Int64): Option<Sheet>` | 按索引获取工作表 |
| `getSheetByName(name: String): Option<Sheet>` | 按名称获取工作表 |
| `getActiveSheet(): Option<Sheet>` | 获取活动工作表 |
| `setActiveSheet(index: Int64): Bool` | 设置活动工作表 |
| `getSheetCount(): Int64` | 获取工作表数量 |
| `renameSheet(index: Int64, newName: String): Bool` | 重命名工作表 |
| `forEachSheet(action: (Sheet) -> Unit)` | 遍历所有工作表 |
| `isEmpty(): Bool` | 检查是否为空 |
| `clear()` | 清空工作簿 |
| `activeSheetIndex: Int64` | 当前活动工作表索引 |
| `filePath: String` | 文件路径 |

### Sheet 类

工作表包含行列结构的单元格数据。

| 方法 | 说明 |
|------|------|
| `init(name: String)` | 创建工作表 |
| `init(name: String, index: Int64)` | 创建带索引的工作表 |
| `getCell(row: Int64, col: Int64): Cell` | 获取单元格 |
| `setCell(row: Int64, col: Int64, cell: Cell)` | 设置单元格 |
| `setCellValue(row: Int64, col: Int64, value: String)` | 设置单元格值 |
| `setCellValueByCoord(coordinate: String, value: String)` | 按 Excel 坐标设置值 |
| `getCellByCoord(coordinate: String): Cell` | 按 Excel 坐标获取单元格 |
| `getRowCount(): Int64` | 获取行数 |
| `getColumnCount(): Int64` | 获取列数 |
| `setRow(row: Int64, values: Array<String>)` | 设置整行数据 |
| `appendRow(values: Array<String>): Int64` | 追加一行，返回行索引 |
| `forEachCell(action: (Cell) -> Unit)` | 遍历所有单元格 |
| `clear()` | 清空工作表 |
| `isEmpty(): Bool` | 检查是否为空 |
| `name: String` | 工作表名称 |
| `index: Int64` | 工作表索引 |

### Cell 类

单元格是存储数据的最小单位。

| 方法 | 说明 |
|------|------|
| `init()` | 创建空单元格 |
| `init(row: Int64, col: Int64, value: String)` | 创建带值单元格 |
| `setString(str: String)` | 设置字符串值 |
| `setNumber(num: Float64)` | 设置浮点数值 |
| `setInt(num: Int64)` | 设置整数值 |
| `setBool(b: Bool)` | 设置布尔值 |
| `getString(): String` | 获取字符串值 |
| `getInt(): Int64` | 获取整数值 |
| `getBool(): Bool` | 获取布尔值 |
| `isEmpty(): Bool` | 检查是否为空 |
| `getCoordinate(): String` | 获取 Excel 坐标（如 "A1"）|
| `columnIndexToName(colIndex: Int64): String` | 静态方法：列索引转列名 |
| `columnNameToIndex(colName: String): Int64` | 静态方法：列名转列索引 |
| `row: Int64` | 行索引（从0开始）|
| `col: Int64` | 列索引（从0开始）|
| `value: String` | 单元格原始值 |
| `cellType: CellType` | 单元格类型 |

### CsvConfig 类

CSV 读写配置。

| 属性/方法 | 说明 |
|----------|------|
| `delimiter: Rune` | 字段分隔符，默认 `,` |
| `quoteChar: Rune` | 引用符，默认 `"` |
| `hasHeader: Bool` | 是否包含表头 |
| `lineTerminator: String` | 行终止符，默认 `\r\n` |
| `withDelimiter(delimiter: Rune): CsvConfig` | 设置分隔符 |
| `withQuoteChar(quoteChar: Rune): CsvConfig` | 设置引用符 |
| `withHeader(hasHeader: Bool): CsvConfig` | 设置表头选项 |

### 便捷函数

| 函数 | 说明 |
|------|------|
| `createWorkbookFromArray(data: Array<Array<String>>, sheetName: String = "Sheet1"): Workbook` | 从数组创建工作簿 |
| `createEmptyWorkbook(sheetNames: Array<String> = ["Sheet1"]): Workbook` | 创建带有指定工作表名的空工作簿 |
| `parseCSV(content: String, sheetName: String = "Sheet1"): Workbook` | 从 CSV 字符串解析创建工作簿 |
| `toCSV(workbook: Workbook, sheetIndex: Int64 = 0): String` | 将工作簿导出为 CSV 字符串 |
| `saveAsXlsx(workbook: Workbook, filePath: String)` | 将工作簿保存为 XLSX 文件 |
| `saveAsCsv(workbook: Workbook, filePath: String, sheetIndex: Int64 = 0)` | 将工作簿保存为 CSV 文件 |
| `readXlsx(filePath: String): Workbook` | 从 XLSX 文件读取工作簿 |
| `readXlsxFromBytes(data: Array<UInt8>): Workbook` | 从字节数组读取 XLSX 工作簿 |
| `readCsv(filePath: String, sheetName: String = "Sheet1"): Workbook` | 从 CSV 文件读取工作簿 |
| `openExcel(filePath: String): Workbook` | 打开 Excel 文件（自动识别 .xlsx/.csv 格式）|
| `generateXlsxContents(workbook: Workbook): ArrayList<XlsxFileEntry>` | 生成 XLSX 文件内容列表（用于高级自定义）|
| `generateCsvContent(sheet: Sheet): String` | 生成单个工作表的 CSV 内容 |

### 读写类

| 类 | 说明 |
|------|------|
| `CsvReader` | CSV 读取器，支持从字符串解析 CSV 内容 |
| `CsvWriter` | CSV 写入器，支持将工作表转换为 CSV 字符串 |
| `XlsxReader` | XLSX 读取器，支持解析 XLSX 文件内容 |
| `XlsxWriter` | XLSX 写入器，支持生成 XLSX 格式的 XML 内容 |
| `ZipReader` | ZIP 文件读取器，用于读取 XLSX 文件（XLSX 是 ZIP 格式）|
| `ZipWriter` | ZIP 文件写入器，用于生成 XLSX 文件 |
| `XlsxFileEntry` | XLSX 文件内容项，包含 `path` 和 `content` 属性 |
| `ZipReadEntry` | ZIP 读取条目，包含 `name`、`data` 属性和 `getDataAsString()` 方法 |


## 编译和测试

### 编译项目

```bash
cjpm build
```

### 运行测试

```bash
cjpm test
```

## 配置到你的工程

### 依赖配置

在 `cjpm.toml` 中添加依赖：

```toml
[dependencies]
  excel_cj = { path = "path/to/excel-cj" }
```

### 环境要求

- 仓颉编译器 cjc 1.0.4 或更高版本
- 仓颉 SDK


## 使用指导

### 导入库

```cangjie
import excel_cj.*
```

### 读取 XLSX 文件

```cangjie
main() {
    // 读取 XLSX 文件
    let workbook = readXlsx("员工信息.xlsx")
    
    // 获取第一个工作表
    let sheet = workbook.getSheet(0).getOrThrow()
    println("工作表名称: ${sheet.name}")
    println("行数: ${sheet.getRowCount()}")
    println("列数: ${sheet.getColumnCount()}")
    
    // 读取单元格数据
    let name = sheet.getCell(1, 0).getString()    // 第2行第1列
    let age = sheet.getCell(1, 1).getString()     // 第2行第2列
    let dept = sheet.getCell(1, 2).getString()    // 第2行第3列
    println("姓名: ${name}, 年龄: ${age}, 部门: ${dept}")
    
    // 遍历所有数据
    var row: Int64 = 0
    while (row < sheet.getRowCount()) {
        var col: Int64 = 0
        var line = ""
        while (col < sheet.getColumnCount()) {
            if (col > 0) { line += "\t" }
            line += sheet.getCell(row, col).getString()
            col += 1
        }
        println(line)
        row += 1
    }
}
```

### 创建并保存 XLSX 文件

```cangjie
main() {
    // 创建新工作簿
    let workbook = Workbook()
    
    // 创建工作表
    let sheet = workbook.createSheet("员工信息")
    
    // 设置表头
    sheet.setCellValue(0, 0, "姓名")
    sheet.setCellValue(0, 1, "年龄")
    sheet.setCellValue(0, 2, "部门")
    
    // 添加数据
    sheet.setCellValue(1, 0, "张三")
    sheet.setCellValue(1, 1, "28")
    sheet.setCellValue(1, 2, "技术部")
    
    sheet.setCellValue(2, 0, "李四")
    sheet.setCellValue(2, 1, "32")
    sheet.setCellValue(2, 2, "市场部")
    
    // 直接保存为 XLSX 文件
    saveAsXlsx(workbook, "员工信息.xlsx")
    println("已保存 XLSX 文件")
    
    // 直接保存为 CSV 文件
    saveAsCsv(workbook, "员工信息.csv")
    println("已保存 CSV 文件")
    
    // 或者导出为字符串
    let csvContent = toCSV(workbook)
    println(csvContent)
    // 输出: 姓名,年龄,部门
    //       张三,28,技术部
    //       李四,32,市场部
}
```

### 从 CSV 内容解析数据

```cangjie
main() {
    // 从 CSV 字符串解析数据
    let csvContent = "Name,Age,Department\nAlice,25,Engineering\nBob,30,Marketing"
    let workbook = parseCSV(csvContent, sheetName: "Employees")
    
    // 获取第一个工作表
    let sheet = workbook.getSheet(0).getOrThrow()
    
    // 读取单元格
    let name = sheet.getCell(1, 0).getString()
    let age = sheet.getCell(1, 1).getInt()
    
    println("姓名: ${name}, 年龄: ${age}")
    
    // 导出为 CSV 字符串
    let csvOutput = toCSV(workbook)
    println(csvOutput)
}
```

### 使用 Excel 坐标

```cangjie
main() {
    let workbook = Workbook()
    let sheet = workbook.createSheet("Sheet1")
    
    // 使用 Excel 坐标设置值
    sheet.setCellValueByCoord("A1", "Hello")
    sheet.setCellValueByCoord("B1", "World")
    sheet.setCellValueByCoord("A2", "100")
    sheet.setCellValueByCoord("B2", "200")
    
    // 使用 Excel 坐标读取值
    let cell = sheet.getCellByCoord("A1")
    println(cell.getString())  // 输出: Hello
}
```

### 快速创建工作簿

```cangjie
main() {
    // 从二维数组创建
    let data = [
        ["Product", "Price", "Quantity"],
        ["Apple", "1.50", "100"],
        ["Banana", "0.75", "200"]
    ]
    let workbook = createWorkbookFromArray(data, sheetName: "Products")
    
    // 创建带多个工作表的空工作簿
    let wb = createEmptyWorkbook(sheetNames: ["Sales", "Inventory", "Reports"])
}
```


### 读取并修改 XLSX 文件

```cangjie
main() {
    // 读取现有 XLSX 文件
    let workbook = readXlsx("销售报表.xlsx")
    
    // 获取并修改工作表
    let sheet = workbook.getSheet(0).getOrThrow()
    
    // 在末尾添加一行数据
    let newRowIndex = sheet.getRowCount()
    sheet.setCellValue(newRowIndex, 0, "新产品")
    sheet.setCellValue(newRowIndex, 1, "199.99")
    sheet.setCellValue(newRowIndex, 2, "50")
    
    // 保存修改
    saveAsXlsx(workbook, "销售报表_更新.xlsx")
    println("文件已更新")
}
```

### 使用 openExcel 自动识别格式

```cangjie
main() {
    // 自动识别文件格式（支持 .xlsx 和 .csv）
    let workbook = openExcel("数据文件.xlsx")  // 或 "数据文件.csv"
    
    // 获取工作表信息
    println("工作表数量: ${workbook.getSheetCount()}")
    
    workbook.forEachSheet { sheet =>
        println("工作表: ${sheet.name}")
        println("  行数: ${sheet.getRowCount()}")
        println("  列数: ${sheet.getColumnCount()}")
    }
}
```

### 读取多工作表 XLSX 文件

```cangjie
main() {
    let workbook = readXlsx("多表格文件.xlsx")
    
    // 按索引访问工作表
    let sheet1 = workbook.getSheet(0).getOrThrow()
    println("第一个工作表: ${sheet1.name}")
    
    // 按名称访问工作表
    let salesSheet = workbook.getSheetByName("销售数据")
    if (salesSheet.isSome()) {
        let sheet = salesSheet.getOrThrow()
        println("找到销售数据工作表，共 ${sheet.getRowCount()} 行")
    }
    
    // 遍历所有工作表
    workbook.forEachSheet { sheet =>
        println("处理工作表: ${sheet.name}")
        // ... 处理数据
    }
}
```

### 配置 CSV 格式

```cangjie
main() {
    // 使用分号分隔、单引号引用
    let config = CsvConfig()
        .withDelimiter(r';')
        .withQuoteChar(r'\'')
        .withHeader(true)
    
    // 使用自定义配置的读取器解析 CSV
    let csvContent = "Name;Age\nAlice;25\nBob;30"
    let reader = CsvReader(config)
    let workbook = reader.parseContent(csvContent, "DataSheet")
    
    // 使用自定义配置的写入器生成 CSV
    let sheet = workbook.getSheet(0).getOrThrow()
    let writer = CsvWriter(config)
    let output = writer.generateContent(sheet)
    println(output)
}
```

### 处理多工作表

```cangjie
main() {
    let workbook = Workbook()
    
    // 创建多个工作表
    let salesSheet = workbook.createSheet("Sales")
    let inventorySheet = workbook.createSheet("Inventory")
    let reportsSheet = workbook.createSheet("Reports")
    
    // 填充数据...
    
    // 遍历所有工作表
    workbook.forEachSheet { sheet =>
        println("工作表: ${sheet.name}, 行数: ${sheet.getRowCount()}")
    }
    
    // 设置活动工作表
    workbook.setActiveSheet(1)
    
    // 按名称获取工作表
    let sheet = workbook.getSheetByName("Sales")
    if (sheet.isSome()) {
        println("找到工作表: ${sheet.getOrThrow().name}")
    }
}
```

### 单元格类型处理

```cangjie
main() {
    let cell = Cell()
    
    // 设置字符串
    cell.setString("Hello World")
    println(cell.getString())  // 输出: Hello World
    
    // 设置数字
    cell.setNumber(3.14159)
    println(cell.getString())  // 输出: 3.14159
    
    // 设置整数
    cell.setInt(42)
    let intVal = cell.getInt()
    println("整数值: ${intVal}")  // 输出: 整数值: 42
    
    // 设置布尔值
    cell.setBool(true)
    let boolVal = cell.getBool()
    println("布尔值: ${boolVal}")  // 输出: 布尔值: true
    
    // 检查类型
    if (cell.cellType == CellType.BoolType) {
        println("这是布尔单元格")
    }
    
    // 获取单元格坐标
    let coordCell = Cell(5, 2, "Test")
    println("坐标: ${coordCell.getCoordinate()}")  // 输出: 坐标: C6
}
```


## 许可证

本项目基于 [Apache License](./LICENSE) ，请自由地享受和参与开源。

## 贡献

欢迎提交 Issue 和 Pull Request！

