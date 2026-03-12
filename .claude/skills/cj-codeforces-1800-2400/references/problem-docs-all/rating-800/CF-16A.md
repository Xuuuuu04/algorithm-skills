# CF-16A Flag

## 题面快照

## Description

根据一项新的 ISO 标准，每一个国家的国旗应该是一个 $n\times m$ 的格子场，其中每个格子最多有 $10$ 种不同的颜色。并且国旗应该有条纹：旗帜的每一行应包含相同颜色的方块，相邻的行的颜色应该是不同的。Berland 政府要求你找出他们的国旗是否符合新的 ISO 标准。

## Input

输入的第一行包含数 $n$ 和 $m$，其中 $n$ 为行数，$m$ 为列数。

接下来是对旗的描述：以下 $n$ 行中的每一行包含 $m$ 个字符。每个字符是 $0$ 到 $9$ 之间的数字，代表相应正方形的颜色。

## Output

如果国旗符合标准就输出 `YES`，否则输出 `NO`。

## Samples

### Sample 1

Input
```
3 3
000
111
222
```

Output
```
YES
```

### Sample 2

Input
```
3 3
000
000
111
```

Output
```
NO
```

### Sample 3

Input
```
3 3
000
111
002
```

Output
```
NO
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-16A |
| Contest | 16 |
| Index | A |
| Rating | 800 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 16898 |
| 镜像尝试 / 通过 | 3761 / 1657 |
| 时限 | 2000 ms |
| 内存限制 | 64000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/16/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/16/problem/A)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF16A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

