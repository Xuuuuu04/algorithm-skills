# CF-59A Word

## 题面快照

## Description

Vasya 对许多人在网络上将大写字母和小写字母混用在同一个单词里感到十分不满。因此，他打算为自己最喜欢的浏览器开发一个扩展程序，将每个单词的字母变为全小写或全大写，以保证一个单词只包含一种字母大小写。并且，整个单词中应尽可能少地更改字母。例如，单词 HoUse 应被替换为 house，而单词 ViP 应被替换为 VIP。如果一个单词中大写和小写字母数量相等，则应将所有字母改为小写。例如，maTRIx 应被替换为 matrix。你的任务是对给定的单词，按照上述方法进行处理。

## Input

第一行包含一个单词 $s$ ——它只包含大写和小写的拉丁字母，长度为 $1$ 到 $100$。

## Output

输出纠正后的单词 $s$。如果原单词 $s$ 中大写字母数量严格多于小写字母，则将单词全部转换为大写；否则，全部转换为小写。

## Samples

### Sample 1

Input
```
HoUse
```

Output
```
house
```

### Sample 2

Input
```
ViP
```

Output
```
VIP
```

### Sample 3

Input
```
maTRIx
```

Output
```
matrix
```

## Note

由 ChatGPT 5 翻译

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-59A |
| Contest | 59 |
| Index | A |
| Rating | 800 |
| Points | 500.0 |
| Codeforces 标签 | `implementation`、`strings` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 223261 |
| 镜像尝试 / 通过 | 3789 / 1928 |
| 时限 | 2000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/59/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/59/problem/A)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF59A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

