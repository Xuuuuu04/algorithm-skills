<div align="center">
<h1>aad4cj</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-HOS/Cloud-brightgreen" style="display: inline-block;" />
</p>

## 介绍

aad4cj 是一个基于仓颉（Cangjie）语言实现的 **AAC 音频码流解析与处理组件库**，目前已实现了，AAC解码流程中的所需要的部分关键基础组件，包括：
- 高效的位流读取器 (`bitreader4cj`)
- 符合 MPEG 标准的 ADTS 帧解析器
- Huffman 编码解码工具
- 窗口分组逻辑
- SBR 相关数据结构与表格定义

这些解码组件为最终实现 AAC 音频解码（将压缩数据还原为 PCM 音频样本）奠定了基础。但请注意，**并不直接支持完整的端到端AAC音频解码**，只是提供部分**关键基础组件**。


### 项目特性

- **高性能**：针对音频码流解析进行了优化，提供高效的位级访问能力
- **模块化设计**：各组件独立且可复用，便于扩展和维护
- **符合标准**：遵循MPEG-4 AAC音频编码标准
- **完善的错误处理**：提供详细的错误信息，便于调试和排查问题

### 项目计划

- 2025/01/11 适配仓颉v0.53.18发布
- 2025/07/11 适配仓颉v1.0.0发布

**参考与依赖:**

- 本项目参考了 [Comcast/gaad](https://github.com/Comcast/gaad) 的实现
- 由于项目庞大，将其中的bitreader独立成项目： [mumu_xsy/bitreader4cj](https://gitcode.com/mumu_xsy/bitreader4cj)

## 项目架构

### 源码目录

```shell
.
├── README.md
├── LICENSE
├── cjpm.toml
|
└── src                  # 源码目录
    ├── aac_parser.cj            # AAC解析器实现
    ├── aac_huffman_util.cj       # 哈夫曼编码工具
    ├── aac_sbr_tables.cj         # SBR扩展表格定义
    ├── aac_window_grouping.cj    # 窗口分组处理
    ├── aac_utils.cj             # AAC工具函数
    ├── bitreader/              # 位读取器相关
    │   ├── bitreader.cj        # 位读取器实现
    │   └── errors.cj           # 错误处理
    └── test/                   # 测试代码目录
        ├── bitreader_test.cj   # BitReader单元测试
        ├── aac_parser_test.cj   # AAC解析器单元测试
        ├── aac_window_grouping_test.cj  # 窗口分组处理单元测试
        ├── aac_sbr_tables_test.cj       # SBR表格单元测试
        ├── extension_data_sbr_test.cj   # SBR扩展数据单元测试
        ├── fill_element_test.cj         # 填充元素单元测试
        └── aac_utils_test.cj            # AAC工具函数单元测试
```

### 接口说明

主要类和函数接口说明如下，详见 [API](./doc/feature_api.md)

#### Adts解析API

```cangjie
/** Adts帧解析函数
 * 
 * 解析AAC音频数据传输流(Adts)格式的音频帧
 *
 * @param byteArray 包含Adts帧数据的字节数组
 * @return 元组(Adts, Exception)，包含解析后的Adts结构和可能的错误
 */
public func parseAdts(byteArray: Array<UInt8>): (Adts, Exception)
```

```cangjie
/** Adts类 - AAC音频数据传输流容器
 *
 * 表示AAC音频数据传输流(Adts)格式的封装容器
 * 包含Adts帧的头部信息和数据内容
 * 用于解析和访问Adts格式的AAC音频流
 */
public class Adts {
    // 基本属性
    public var bitrate: UInt32              // 音频比特率，单位为比特每秒
    public var channelConfiguration: UInt8  // 声道配置，指定音频声道的数量和排列
    public var layer: UInt8                 // 层信息，在Adts格式中的层级
    public var mpegVersion: UInt8           // MPEG版本，区分MPEG-4和MPEG-2
    public var profile: UInt8               // AAC编码配置文件(Main、LC、SSR等)
    public var samplingFrequency: UInt32    // 音频采样率，单位为赫兹
    public var vbrMode: Bool                // 是否使用可变比特率编码
    public var frameLength: UInt16          // 当前Adts帧的总长度，单位为字节
    public var reader: BitReader            // 用于从字节流中读取位数据的比特流读取器
    
    /** 
     * adtsFrame函数 - 解析Adts帧
     *
     * 对应标准中的Table 1.A.5 – Syntax of adtsFrame()
     * 负责解析完整的Adts帧，包括固定头部、可变头部和原始数据块
     * 
     * @return 解析过程中的异常，如果解析成功则返回空异常
     */
    public func adtsFrame(): Exception
}
```

#### 音频元素类型常量

```cangjie
// 音频元素类型常量
public let idSce: UInt8 = 0x00 // "Single Channel Element"（单声道元素）
public let idCpe: UInt8 = 0x01 // "Channel Pair Element"（声道对元素）
public let idCce: UInt8 = 0x02 // "Coupling Channel Element"（耦合声道元素）
public let idLfe: UInt8 = 0x03 // "LFE Channel Element"（低频效果声道元素）
public let idDse: UInt8 = 0x04 // "Data Stream Element"（数据流元素）
public let idPce: UInt8 = 0x05 // "Program Config Element"（程序配置元素）
public let idFil: UInt8 = 0x06 // "Fill Element"（填充元素）
public let idEnd: UInt8 = 0x07 // "End"（结束标记）
```

#### Huffman工具API

```cangjie
/** 解码哈夫曼编码的比例因子
 *
 * 该函数从比特流读取器中读取哈夫曼编码的比例因子(Scale Factor)，并进行解码
 *
 * @param reader 比特流读取器
 * @return 元组，包含解码后的比例因子值和可能的异常
 */
public func hcodSf(reader: BitReader): (UInt8, Exception)
```

```cangjie
/** 使用两步查找法解码哈夫曼编码
 *
 * 该函数在可能的情况下使用两步查找法来解码哈夫曼编码，提高解码效率
 *
 * @param reader 比特流读取器
 * @param codebook 使用的编码本编号
 * @param values 用于存储解码结果的数组
 * @return 可能的异常信息
 */
public func hcod2Step(reader: BitReader, codebook: UInt8, values: Array<Int8>): Exception
```

#### 窗口分组API

```cangjie
/**
 * 设置窗口分组参数
 * 
 * 根据窗口序列类型和采样频率索引设置窗口分组相关参数
 * 
 * @param info IcsInfo结构，包含窗口序列和分组信息
 * @param sfi 采样频率索引
 * @param framelength 帧长度
 */
public func windowGrouping(info: IcsInfo, sfi: UInt8, framelength: UInt16)
```

```cangjie
/**
 * 窗口分组相关的表格和常量类
 * 提供AAC编解码所需的窗口分组参数
 * 包含了不同采样率下长/短窗口的子带宽度偏移表
 */
public class WindowGroupTables {
    // 长窗口子带宽度数量表，二维数组[帧长索引][采样率索引]
    public static let numSwbLongWindows: Array<Array<UInt8>>
    
    // 短窗口子带宽度数量表，按采样率索引排列
    public static let numSwbShortWindow: Array<UInt8>
}
```

```cangjie
// 仅使用长窗口的序列类型
public let onlyLongSequence: UInt8 = 0
// 长窗口开始序列类型
public let longStartSequence: UInt8 = 1
// 8个短窗口序列类型
public let eightShortSequence: UInt8 = 2
// 长窗口结束序列类型
public let longStopSequence: UInt8 = 3
```

## 使用说明

### 编译构建

描述具体的编译过程：

```shell
cjpm update
cjpm build
```

### 功能示例

#### 窗口分组示例

功能示例描述: 本示例展示了如何使用IcsInfo类和windowGrouping函数设置和管理AAC音频的窗口分组信息，包括窗口序列、子带信息等。

```cangjie
import aad4cj.*

main() {
    // 创建IcsInfo实例
    let info = IcsInfo()
    
    // 设置窗口序列类型 (例如使用八短序列)
    info.windowSequence = eightShortSequence  // 值为2
    
    // 设置比例因子分组位 (影响短窗口的分组)
    info.scaleFactorGrouping = 0x2D  // 二进制: 00101101
    
    // 预先初始化必要的数组
    info.sectSfbOffset = Array<Array<UInt16>>()
    info.sfbOffset = Array<UInt16>()
    
    // 执行窗口分组 (使用采样频率索引0和帧长度1024)
    windowGrouping(info, 0, 1024)
    
    // 输出分组结果
    println("窗口分组结果:")
    println("窗口数量: ${info.numWindows}")
    println("窗口组数量: ${info.numWindowGroups}")
    println("最大子带: ${info.maxSfb}")
    println("每组窗口长度:")
    
    for (i in 0..Int64(info.numWindowGroups)) {
        println("组 ${i+1}: ${info.windowGroupLength[i]}")
    }
    
    // 显示子带偏移信息
    println("子带偏移量:")
    for (i in 0..info.sfbOffset.size) {
        println("子带 ${i}: ${info.sfbOffset[i]}")
    }
}
```

执行结果如下：

```shell
窗口分组结果:
窗口数量: 8
窗口组数量: 4
最大子带: 12
每组窗口长度:
组 1: 1
组 2: 3
组 3: 2
组 4: 2
子带偏移量:
子带 0: 0
子带 1: 4
子带 2: 8
子带 3: 12
子带 4: 16
子带 5: 20
子带 6: 24
子带 7: 32
子带 8: 40
子带 9: 48
子带 10: 64
子带 11: 92
子带 12: 128
```


#### 哈夫曼解码示例

功能示例描述: 本示例展示了如何使用哈夫曼编码工具进行解码，包括两步查找法解码和比例因子解码功能。

```cangjie
import aad4cj.*
import aad4cj.bitreader.*
import encoding.hex.*

main() {
    println("哈夫曼解码示例:")
    
    // 创建一个测试数据
    // 这个数据使用编码本8的哈夫曼编码，用于演示解码过程
    let data = Array<UInt8>(4, item: 0)
    data[0] = 0xA5  // 10100101
    data[1] = 0xC7  // 11000111
    data[2] = 0x21  // 00100001
    data[3] = 0xF0  // 11110000
    
    println("使用测试数据: [0xA5, 0xC7, 0x21, 0xF0]")
    
    // 创建BitReader
    let reader = BitReader(data)
    
    // 创建用于存储解码值的数组
    let values = Array<Int8>(2, item: 0)
    
    try {
        // 使用解码本8进行哈夫曼解码
        let codebook: UInt8 = 8
        
        // 使用两步查找法解码哈夫曼编码
        let exception = hcod2Step(reader, codebook, values)
        
        if (exception.message == "无错误") {
            println("哈夫曼解码成功!")
            println("解码结果 (编码本 ${codebook}):")
            
            for (i in 0..Int64(values.size)-1) {
                println("  值${i+1}: ${values[i]}")
            }
            
            // 重置位置，尝试解码比例因子
            reader.reset()
            reader.skipBits(16) // 跳过前两个字节
            
            let (sf, sfException) = hcodSf(reader)
            if (sfException.message == "无错误") {
                println("比例因子解码成功!")
                println("比例因子值: ${sf}")
            } else {
                println("比例因子解码失败: ${sfException.message}")
            }
            
            // 显示哈夫曼编码本常量
            println("Huffman编码本常量:")
            println("零码本: ${zeroHcb}")
            println("第一对码本: ${firstPairHcb}")
            println("噪声码本: ${noiseHcb}")
            println("强度立体声码本: ${intensityHcb}")
        } else {
            println("哈夫曼解码失败: ${exception.message}")
        }
    } catch (e: Exception) {
        println("解码过程中发生错误: ${e.message}")
    }
}
```

执行结果如下：

```shell
哈夫曼解码示例:
使用测试数据: [0xA5, 0xC7, 0x21, 0xF0]
哈夫曼解码成功!
解码结果 (编码本 8):
  值1: 2
比例因子解码成功!
比例因子值: 60
Huffman编码本常量:
  零码本: 0
  第一对码本: 5
  噪声码本: 13
  强度立体声码本: 15
```

#### Adts帧解析

功能示例描述: 本示例展示了如何手动解析AAC音频中的Adts帧头信息，读取其中的关键参数，而不依赖于文件输入。

```cangjie
import aad4cj.*
import aad4cj.bitreader.*

main() {
    println("Adts帧解析示例:")
    
    // 直接创建Adts帧数据数组
    // 数据为 0xFF, 0xF1, 0x50, 0x80 (有效Adts帧的开始部分)
    let data = Array<UInt8>(4, item: 0)
    data[0] = 0xFF  // 同步字高8位
    data[1] = 0xF1  // 同步字低4位 + MPEG版本(0) + 层(00) + 有无保护位(1)
    data[2] = 0x50  // 配置文件(01) + 采样率索引(0100) + 私有位(0)
    data[3] = 0x80  // 通道配置(100) + ...
    
    println("使用创建的Adts帧数据: [0xFF, 0xF1, 0x50, 0x80]")
    
    // 创建BitReader直接解析Adts头部
    let reader = BitReader(data)
    
    try {
        // 读取Adts同步字 (12位)
        let syncWord = reader.readBitsAsUInt16(12)
        println("同步字: 0x${syncWord}")
        
        // 读取Adts头信息
        let id = reader.readBit() // MPEG版本: 0=MPEG-4, 1=MPEG-2
        let layer = reader.readBitsAsUInt8(2) // 应该是0
        let protectionAbsent = reader.readBitAsBool() // CRC校验标识: true=无CRC
        let profile = reader.readBitsAsUInt8(2) // AAC配置文件
        let samplingFrequencyIndex = reader.readBitsAsUInt8(4) // 采样率索引
        let privateBit = reader.readBit() // 私有位
        let channelConfiguration = reader.readBitsAsUInt8(3) // 通道配置
        
        // 输出关键信息
        println("Adts帧头信息:")
        println("  MPEG版本: ${if (id == 1) {"MPEG-2"} else {"MPEG-4"}}")
        println("  配置文件: ${profile + 1}") // 配置文件从0开始，显示时+1
        println("  采样率索引: ${samplingFrequencyIndex}")
        
        // 获取实际采样率
        let freqs = [96000, 88200, 64000, 48000, 44100, 32000, 24000, 22050, 16000, 12000, 11025, 8000, 7350, 0, 0, 0]
        if (Int64(samplingFrequencyIndex) < freqs.size) {
            let actualRate = freqs[Int64(samplingFrequencyIndex)]
            println("  采样率: ${actualRate} Hz")
        }
        
        println("  通道配置: ${channelConfiguration}")
    } catch (e: Exception) {
        println("解析过程中发生错误: ${e.message}")
    }
}
```

执行结果如下：

```shell
Adts帧解析示例:
使用创建的Adts帧数据: [0xFF, 0xF1, 0x50, 0x80]
同步字: 0x4095
Adts帧头信息:
  MPEG版本: MPEG-4
  配置文件: 2
  采样率索引: 4
  采样率: 44100 Hz
  通道配置: 2
```

## 约束与限制

- **音频格式支持限制**：
  - 当前初步版本主要支持AAC-LC(低复杂度)格式的完整解析
  - 支持HE-AACv1(带SBR)格式，但某些复杂的SBR配置可能解析不完整
  - 不支持HE-AACv2(带参数立体声)格式的完整解析
  - 不支持一些AAC扩展特性，如MPEG环绕声(SAC)的完整处理

- **实践限制**：
  - 大文件处理时建议使用流式解码方式，避免一次性加载整个文件导致内存问题
  - 部分高级功能(如多通道处理和复杂的SBR配置等)暂时采用了简化实现，可能影响后续解析的准确性，将在后续版本进行优化

在处理非标准或复杂AAC流时，可能需要额外的错误检查和处理逻辑。

## 开源协议
本项目基于 MIT License

## 参与贡献

欢迎给我们提交PR，欢迎给我们提交Issue，欢迎参与任何形式的贡献。

本项目committer：[@mumu_xsy](https://gitcode.com/mumu_xsy)/[@leaveWhite9088](https://gitcode.com/leaveWhite9088)

This project is supervised by [@zhangyin_gitcode](https://gitcode.com/zhangyin_gitcode) (HUAWEI Developer Advocate).

![img](https://raw.gitcode.com/SIGCANGJIE/homepage/attachment/uploads/9b648c07-efc2-4eb3-b02f-eab18c77beea/devadvocate.png)