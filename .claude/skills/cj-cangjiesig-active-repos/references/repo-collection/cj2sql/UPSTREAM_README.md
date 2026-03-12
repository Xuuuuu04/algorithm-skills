<div align="center">
<h1>cj2sql</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v0.2.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v0.55.3-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/state-孵化-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-HOS/Cloud-brightgreen" style="display: inline-block;" />
</p>

## <img alt="" src="./doc/readme-image/readme-icon-introduction.png" style="display: inline-block;" width=3%/> 1 介绍
通过宏展开将仓颉函数中特定代码结构转换为 SQL 抽象语法树  

### 1.1 项目特性
- 🚀 生成增删改查 SQL
- 💡 支持常见的操作符以及关键字(如: 加减乘除, like)
- 💡 支持 SQL 内置方法
- 💡 支持动态参数, 代码 if 判断以及 in 列表
- 💡 支持将 if 和 match 改写成 case when 表达式
- 💡 支持 union 表及子查询
- 💪 自动解析参数
- 💪 方言支持

### 1.2 项目计划
1. [ ] 支持自定义配置

## <img alt="" src="./doc/readme-image/readme-icon-framework.png" style="display: inline-block;" width=3%/> 2 架构

### 2.1 项目结构

```shell
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── cjpm.toml
├── doc
    └── readme-image
    └── design.md     接口设计
    └── use.md        使用文档
|
└── src
    └── base          定义 sql 语句使用常量与类信息(用于宏展开)
    └── macros
      └── parser      宏核心解析器
    └── sql
        └── dialect   sql 方言
        └── dml       操作 dml 语句
        └── expr      定义 sql 表达式
        └── meta      定义表信息
        └── statement 定义 sql 语句
        └── use.cj    用户可导入使用的全局方法, 类和枚举 
```

## <img alt="" src="./doc/readme-image/readme-icon-compile.png" style="display: inline-block;" width=3%/> 3 使用说明

### 3.1 编译构建（Win/Linux/Mac）

**注意** 需设置 [STDX](https://gitcode.com/Cangjie/Cangjie-STDX) 模块环境变量  [issue](https://gitcode.com/Cangjie/UsersForum/issues/1889)  
**示例** `CANGJIE_STDX_PATH=path\to\cangjie-stdx-windows-x64-x.x.x.x\windows_x86_64_llvm\dynamic\stdx`

添加依赖配置 `cjpm.toml`:

```toml
[dependencies]
  cj2sql = { git = "https://gitcode.com/Cangjie-SIG/cj2sql" }
```

### 3.2 单元测试
在工程根目录下运行：  
`cjpm test`

### 3.3 功能示例

**[使用文档](doc/use.md)**  
[配合 ORM 使用](https://gitcode.com/devinx3/litem/blob/main/test/HLT/litem_test/src/complex_operation_test.cj)  

```cangjie
@cjSql
public func useCjSql(maxId: Int64, userName: String) {
    // 数组参数
    let list = ArrayList<Int>(5) {i => i + 1}

    // from 表, 创建 select 语句对象
    let u = select<User>()
    // join 表, 创建 join 对象, 并根据主键 与 from 表关联
    let r = u.join<Role>().on {t => t.id == u.roleId}
    // 查询所有列(包含所有 join 表)
    u.addAllSelectItem(includeJoin: true)
    // select 语句
    u.select {
        // 自定义 SQL
        u.id as uid
        u.userName as uname
        u.age as uage
        r.id as rid
        r.roleName
    }
    // where 过滤条件
    u.filter {
        u.id < maxId
        (u.roleId > 2 || u.age > 18)
        if (userName != '') {
            likeAll(u.userName, userName)
        } else if (userName.size > 100) {
            likeRight(u.userName, userName)
        }
        // in 语句
        if (!list.isEmpty()) {
            inn(u.id, list)
        }
        r.id < maxId
        u.userName is notNull
        r.roleName is null
    }.groupBy {
        // group by 字段
        u.id
        u.age
    }.having {
        // having 条件
        u.id > 1
    }.orderBy {
        // 排序字段
        u.id is desc
        r.id
    }
    // 查询列个数
    u.limitOffset(10, 20)
    // 生成 SQL 字符串
    println(u.toBoundSql().sql)
    // 存在的参数个数
    println("param size = ${u.toBoundSql().parameters.size}")
    // 遍历参数列表
    for (param in u.getParameters()) {
        if (let Some(str) <- param.value as ToString) {
            println(str.toString())
        } else {
            println("xxx ignore")
        }
    }
}
```

生成 SQL 示例:
```sql
SELECT
    u.id,
    u.user_name,
    u.age,
    u.role_id,
    r.id,
    r.role_name,
    u.id uid,
    u.user_name uname,
    u.age uage,
    r.id rid,
    r.role_name
FROM user u
JOIN role r ON r.id = u.role_id
WHERE
    u.id < ?
    AND (u.role_id > 2 OR u.age > 18)
    AND u.user_name LIKE ?
    AND u.id IN (?, ?, ?, ?, ?)
    AND r.id < ?
    AND u.user_name IS NOT NULL
    AND r.role_name IS NULL
GROUP BY
    u.id,
    u.age
HAVING
    u.id > 1
ORDER BY
    u.id DESC,
    r.id ASC
LIMIT 
    20, 10
```

## <img alt="" src="./doc/readme-image/readme-icon-contribute.png" style="display: inline-block;" width=3%/> 4 参与贡献

本项目由 devinx3 实现并维护。技术支持和意见反馈请提Issue。

本项目基于 Apache License 2.0，欢迎给我们提交PR，欢迎参与任何形式的贡献。

本项目commiter：[@devinx3](https://gitcode.com/devinx3)