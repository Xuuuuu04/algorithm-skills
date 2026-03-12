---
name: cj-stdx-reference
description: 仓颉算法题场景下的 stdx 扩展库精确参考技能。仅当题目确实需要 json、url、crypto、http、tls、serialization 等能力时，用于补充最小 API 引用与编译注意事项；默认非必需场景下不主动引入，也不负责通用项目的 stdx 安装和构建配置。
---

# STDX Reference

## 必读参考
- **扩展库速查**: `references/stdx-map.md` — 完整 stdx API 速查

## 默认策略
- ❌ **默认不引入 stdx** — 算法题 99% 只需 std
- ✅ 仅当题目明确涉及以下功能时启用:
  - JSON 解析/生成
  - URL 编解码
  - Base64/Hex 编解码
  - 加密/哈希
  - HTTP 请求
  - 序列化/反序列化

## 边界
- 本 Skill 只服务算法题或竞赛答题中的少量 stdx 引用
- 通用项目里的 stdx API 选型请转到 `cangjie-stdx`
- stdx 下载、`cjpm.toml` 配置、静态库/动态库构建请转到 `cangjie-stdx-config`

## 快速选型

| 需求 | 包 | import |
|------|-----|--------|
| JSON 解析 | `stdx.encoding.json` | `import stdx.encoding.json.*` |
| URL 解析/编码 | `stdx.encoding.url` | `import stdx.encoding.url.*` |
| Base64 编解码 | `stdx.encoding.base64` | `import stdx.encoding.base64.*` |
| Hex 编解码 | `stdx.encoding.hex` | `import stdx.encoding.hex.*` |
| MD5/SHA/SM3 哈希 | `stdx.crypto.digest` | `import stdx.crypto.digest.*` |
| 安全随机数 | `stdx.crypto.crypto` | `import stdx.crypto.crypto.*` |
| SM4 加密 | `stdx.crypto.crypto` | `import stdx.crypto.crypto.*` |
| HTTP 客户端 | `stdx.net.http` | `import stdx.net.http.*` |
| TLS | `stdx.net.tls` | `import stdx.net.tls.*` |
| 序列化 | `stdx.serialization` | `import stdx.serialization.*` |

## 高风险点
1. **外部依赖**: crypto/http/tls 需要 OpenSSL 3 — 竞赛环境可能没有
2. **平台差异**: Linux/macOS/Windows 动态库路径不同
3. **编译参数**: 可能需要额外链接参数
4. **性能**: stdx 操作通常比 std 慢，不适合高频调用

## 竞赛环境确认
使用 stdx 前必须确认:
- [ ] 竞赛环境是否预装 OpenSSL 3
- [ ] 是否允许使用 stdx 包
- [ ] 编译命令是否支持 stdx 链接

## 必要输出
- 给出最小依赖集合 (只 import 需要的)
- 给出编译命令 (如有特殊参数)
- 给出文档来源证据引用
