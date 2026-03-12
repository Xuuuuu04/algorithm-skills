# CF-50A Domino piling

## 题面快照

## Description

给定一个 $M \times N$ 的矩形棋盘。你还拥有无限数量的标准多米诺骨牌，每个多米诺骨牌可以覆盖 $2 \times 1$ 的格子。你可以旋转这些多米诺骨牌。请你在如下条件下尽可能多地在棋盘上放置多米诺骨牌：

1. 每个多米诺骨牌完全覆盖两个格子。
2. 任何两个多米诺骨牌不能重叠。
3. 每个多米诺骨牌必须完全放在棋盘内，可以接触棋盘的边缘。

请你求出在这些限制下，可以放置的多米诺骨牌的最大数量。

## Input

输入仅一行，包含两个整数 $M$ 和 $N$，表示棋盘的大小（$1\leq M\leq N\leq16$）。

## Output

输出一个整数，表示最多可以放置多少个多米诺骨牌。

## Samples

### Sample 1

Input
```
2 4
```

Output
```
4
```

### Sample 2

Input
```
3 3
```

Output
```
4
```

## Note

由 ChatGPT 5 翻译

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-50A |
| Contest | 50 |
| Index | A |
| Rating | 800 |
| Points | 500.0 |
| Codeforces 标签 | `greedy`、`math` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 311754 |
| 镜像尝试 / 通过 | 1983 / 1319 |
| 时限 | 2000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/50/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/50/problem/A)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF50A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

