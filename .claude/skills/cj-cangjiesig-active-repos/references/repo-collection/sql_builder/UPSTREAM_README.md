<div align="center">
<h1>sql_builder</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v1.0.4-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/build-pass-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/project-open-brightgreen" style="display: inline-block;" />
</p>

## 介绍

sql_builder 库是一个使用仓颉语言数据库ORM组件。


### 特性

- 🚀 支持`Oracle`、`MSSQL`、`MySQL`、`PostgresSQL`、`Sqlite`五种数据库方言格式
- 🚀 支持`Select`、`Update`、`Delete`、`Join`、`Union`、`Where`、`Group by`、`Order by`、`Limit`、`Having`等操作
- 💪 支持`AND`、`OR`、`IN/NOT IN`、`LIKE/NOT LIKE`、`IN/NOT IN`、`==/<>`、`>/>=`、`</<=`、`BETHEEN`、`NULL/NOT NULL`
- 🛠️ 支持声明`Expr（表达式）`，`Select`、`Update`、`Delete`等Builder中间层
- 🌍 支持生成带占位符的SQL及相关参数数组`builder.toSQL()`
- 🌍 支持生成完整的SQL`builder.toBoundSQL()`
- 🚀 支持ORM操作
- 🚀 支持将QueryResult反序列化成对象


## 软件架构

### 架构图

<p align="center">
<img src="./doc/assets/frame.png" width="60%" >
</p>

架构图文字说明，包括模块说明、架构层次等详细说明。

### 源码目录

```shell
.
├── doc
│   ├── assets
│   └── frame.md
├── src
│   ├── builder
│       ├── builder_apis.cj
│       ├── builder.cj
│       ├── condition_apis.cj
│       ├── condition.cj
│       └── sql.cj
│   ├── orm
│       ├── builder.cj
│       ├── session_builder.cj
│       ├── session.cj
│   └── sql2
│       └── sql.cj
├── test
│    ├── HLT
│    ├── LLT
│    └── UT
├── gitee_gate.cfg
├── LICENSE.txt
├── module.json
├── README.md

```

- `doc`  存放库的设计文档、使用文档、LLT 用例覆盖报告
- `src`  是库源码目录
- `test` 存放 HLT 测试用例、LLT 自测用例和 UT 单元测试用例

### 接口说明

主要类和函数接口说明详见 [API](./doc/api.md)


## 使用说明

### 编译构建

描述具体的编译过程：

```shell
cpm build
```

### 功能示例
#### 构建SQL
```cangjie
package test

import sql_builder.builder.*

main() {
    let sql = select("c, d").setFrom("table1").setWhere(Eq("a", 1)).toBoundSQL()
    println("sql: ${sql}")
    return 0
}

```

执行结果如下： 
```cangjie
sql: SELECT c, d FROM table1 WHERE a=1
```


#### 

## 开源协议



## 参与贡献

欢迎给我们提交PR，欢迎给我们提交Issue，欢迎参与任何形式的贡献。