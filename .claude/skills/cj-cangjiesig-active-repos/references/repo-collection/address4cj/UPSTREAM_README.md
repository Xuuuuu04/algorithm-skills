<div align="center">
<h1>address4cj</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
</p>

## 介绍
<p>
address4cj 用于全面处理全球地址的表示、验证与格式化，内置支持约 200 个国家的地址格式与地区信息，适用于表单填写、地址展示与国际化场景。
</p>
项目参考自：

- [address](https://github.com/bojanz/address)

### 项目特性

- 地址类（Address Class）
- 约 200 个国家的地址格式支持
- 约 50 个国家的行政区划信息，并在必要时提供本地语言名称（例如：Okinawa / 沖縄県）
- 基于 CLDR v47 的国家列表
- 引入 AOT（Ahead-of-Time）编译方式，在运行时实时从 cldr-json 仓库更新 CLDR 国家列表数据，确保国家列表数据始终最新
- HTML 地址格式化器
- HTTP 处理器，可将地址格式和地区信息以 JSON 形式提供

### 项目计划

1. 2025 年 4 月发布 1.0.0 版本。
2. 对项目进行后续维护。

## 项目架构

- [doc](doc) 文档目录，用于存放接口文档
- [src](src) 源码目录，用于存放源代码
- [src/test](src/test) 测试目录，用于存放测试用例


### 源码目录

```shell
.
├── doc                             # 文档目录
│   └── feature_api.md              # 特性接口文档
├── src                             # 源码目录
│   └── address.cj                  # 地址数据的结构化存储与验证
│   └── const.cj                    # 地址字段类型管理
│   └── countries.cj                # CLDR 国家列表数据
│   └── format.cj                   # 国家标准地址格式库
│   └── formatter.cj                # 地址格式化器
│   └── http.cj                     # 多语言地址格式的 HTTP API 服务
│   └── locale.cj                   # 国际化语言标识处理
│   └── test                        # 测试代码目录
│       └── address_test.cj         # 
│       └── const_test.cj           # 
│       └── example_test.cj         # 
│       └── formatter_test.cj       # 
│       └── http_test.cj            # 
│       └── locale_test.cj          # 
├── build.cj                        # 构建脚本
├── cjpm.toml                       # 项目配置文件
├── CHANGLOG.md                     # 变更日志
├── README.md                       # 项目介绍
└── LICENSE                         # 许可证
```

### 接口说明

主要类和函数接口说明，详见 [API](./doc/feature_api.md)


## 使用说明
### 依赖引入

```shell
[dependencies]
    address4cj = { git = "https://gitcode.com/Pocahontas-1120/address4cj.git" }
```

### 编译构建

```shell
cjpm update
cjpm build
```

### 构建脚本（可选）

项目中`countries.cj`是基于以下数据源动态生成的：
- [CLDR version](https://gitee.com/mirrors_unicode-org/cldr-json/raw/main/cldr-json/cldr-localenames-full/package.json)
- [CLDR country names](https://gitee.com/mirrors_unicode-org/cldr-json/raw/main/cldr-json/cldr-localenames-full/main/en/territories.json)

仓库中已包含截至最新提交时的预生成版本。如果您希望始终使用最新数据，请将`build.cj`文件移动至您的仓颉项目主目录下（即与`cjpm.toml`同级），这样编译时相关文件将更新为最新内容。

请注意，仓库会定期更新这些文件，因此您可以放心跳过此步，不会影响项目的正常运行。


### 功能示例

#### 地址格式化功能示例

以国家的地址格式将地址显示为 HTML。包装元素（例如 "p"）和类名（例如 "address"）可以进行配置。国家名称可以省略，适用于所有地址均属于同一国家的场景。

示例代码如下：

```cangjie
import address4cj.*

main() {
    var locale = newLocale("en")
    var formatter = newFormatter(locale)
    var addr = Address(
        line1: "1098 Alta Ave",
        locality: "Mountain View",
        region: "CA",
        postalCode: "94043",
        countryCode: "US"
    )
    println(formatter.format(addr))

    locale = newLocale("zh")
    formatter = newFormatter(locale)
    formatter.noCountry = true
    formatter.wrapperElement = "div"
    formatter.wrapperClass = "postal-address"
    addr = Address(
        line1: "幸福中路",
        sublocality: "新城区",
        locality: "西安市",
        region: "SN",
        postalCode: "710043",
        countryCode: "CN"
    )
    println(formatter.format(addr))
}
```

执行结果如下：

```shell
<p class="address" translate="no">
<span class="line1">1098 Alta Ave</span><br>
<span class="locality">Mountain View</span>, <span class="region">CA</span> <span class="postal-code">94043</span><br>
<span class="country" data-value="US">United States</span>
</p>
<div class="postal-address" translate="no">
<span class="postal-code">710043</span><br>
<span class="region">陕西省</span><span class="locality">西安市</span><span class="sublocality">新城区</span><br>
<span class="line1">幸福中路</span>
</div>
```

#### HTTP API 地址格式分发功能示例

通过 RESTful 接口动态提供各国地址 JSON 格式，实现多语言与区域适配。详见 [http_test.cj](./src/test/http_test.cj)

#### 语言区域解析与标准化功能示例

将不同格式的语言标识（如en-US、sr_rs_latn）自动标准化为统一的BCP 47格式（如sr-Latn-RS），并支持提取语言、脚本、国家/地区等细分组件。

示例代码如下：

```cangjie
import address4cj.*

main() {
    let firstLocale = newLocale("en-US")
    println(firstLocale.toString())
    println("${firstLocale.language} ${firstLocale.territory}")

    // Locale IDs are normalized.
    let secondLocale = newLocale("sr_rs_latn")
    println(secondLocale.toString())
    println("${secondLocale.language} ${secondLocale.script} ${secondLocale.territory}")
}
```

执行结果如下：

```shell
en-US
en US
sr-Latn-RS
sr Latn RS
```


#### 地址表示与序列化功能示例

创建地址对象并转换为JSON格式。

示例代码如下：

```cangjie
import address4cj.*
import stdx.encoding.json.stream.*
import std.io.ByteArrayStream

main() {
    let addr = Address(
        line1: "幸福中路",
        sublocality: "新城区",
        locality: "西安市",
        region: "SN",
        postalCode: "710043",
        countryCode: "CN"
    )

    let stream = ByteArrayStream()
    let writer = JsonWriter(stream)
    writer.writeValue(addr)
    writer.flush()
    println(String.fromUtf8(stream.readToEnd()))
}
```

执行结果如下：

```shell
{"line1":"幸福中路","line2":"","line3":"","sublocality":"新城区","locality":"西安市","region":"SN","postal_code":"710043","country":"CN"}
```

#### 地址验证功能示例

验证国家代码、必填字段、邮政编码格式。

示例代码如下：

```cangjie
import address4cj.*

main() {
    let format = getFormat("US") // 获取美国地址格式

    // 验证国家代码
    if (!checkCountryCode("XX")) {
        println("无效的国家代码")
    }
    // 验证必填字段
    if (!format.checkRequired(FieldLine1, "")) {
        println("line1是必填字段")
    }
    // 验证邮政编码（匹配美国邮编格式\d{5}）
    if (!format.checkPostalCode("ABC123")) {
        println("邮政编码格式错误")
    }
}
```

执行结果如下：

```shell
无效的国家代码
line1是必填字段
邮政编码格式错误
```

#### 地址本地化模板选择示例

根据地区选择布局和区域名称。

示例代码如下：

```cangjie
import address4cj.*

main() {
    let jpFormat = getFormat("JP") // 获取日本地址格式

    // 选择适合日语的布局
    let layout = jpFormat.selectLayout(newLocale("ja"))
    println("布局模板: ${layout}")

    // 获取本地化的区域名称（如显示"東京"而非"Tokyo"）
    let localRegions = jpFormat.selectRegions(newLocale("ja"))
    println(localRegions.get("13")[0]) // 输出: 東京都
}
```

执行结果如下：

```shell
布局模板: 〒%P
%R%L
%1
%2
%3
東京都
```

#### 格式配置管理功能示例

访问国家特定的地址规则。

示例代码如下：

```cangjie
import address4cj.*

main() {
    let cnFormat = getFormat("CN")

    // 检查中国是否需要显示区域ID
    println("显示区域ID? ${cnFormat.showRegionID}")

    // 获取中国邮政编码的正则规则
    println("邮编验证规则: ${cnFormat.postalCodeValidationPattern()}")
    // 输出: ^\d{6}$
}
```

执行结果如下：

```shell
显示区域ID? false
邮编验证规则: ^\d{6}$
```

#### 区域数据管理功能示例

处理行政区划映射表。

示例代码如下：

```cangjie
import address4cj.*
import std.collection.*

main() {
    // 创建自定义区域映射
    let regions = newRegionMap(
        pairs: ArrayList<String>(
            ["15", "Artemisa", "09", "Camagüey", "08", "Ciego de Ávila", "06", "Cienfuegos", "12", "Granma", "14",
                "Guantánamo"]))

    // 查询区域
    let (shName, exists) = regions.get("12")
    if (exists) {
        println("12对应名称: " + shName)
    }
}
```

执行结果如下：

```shell
12对应名称: Granma
```

## 约束与限制
在下述版本验证通过：
```shell
Cangjie Version: 0.53.18
```

## 开源协议
[MIT License](./LICENSE)

## 参与贡献

本项目由 [SIGCANGJIE / 仓颉兴趣组](https://gitcode.com/SIGCANGJIE) 实现并维护。技术支持和意见反馈请提Issue。

欢迎给我们提交PR，欢迎参与任何形式的贡献。

本项目committer：[@Pocahontas-1120](https://gitcode.com/Pocahontas-1120)

This project is supervised by [@zhangyin_gitcode](https://gitcode.com/zhangyin_gitcode) (HUAWEI Developer Advocate).

![](https://raw.gitcode.com/SIGCANGJIE/homepage/attachment/uploads/9b648c07-efc2-4eb3-b02f-eab18c77beea/devadvocate.png)