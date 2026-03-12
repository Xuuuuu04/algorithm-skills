# CF-45G Prime Problem

## 题面快照

## Description

在 Berland，质数非常流行——只有体面的市民才住在楼号是质数的楼层。钱币收藏家特别珍视面值为质数的硬币。所有质数日期都会被宣布为节日！

然而，这一切还不足以让 Berland 的人民感到满足。在首都的主街道上有 $n$ 幢房子，编号从 1 到 $n$。政府决定将每一幢房子刷上一种颜色，使得每种颜色所刷房子的编号之和都是质数。

但是，并不是所有市民都赞同这一决定——许多人抗议，因为他们不希望主街道上的房子被涂成太多不同的颜色。因此，决定尽可能使用最少的颜色数。房子不要求连续涂色，但每一幢房子必须被刷上某种颜色。同一颜色的房子无需相邻，涂色方式任意。

距离开刷还有不超过 5 小时，请你帮助政府找到一种方案，使得每种颜色所刷房子的编号之和为质数，并且所用颜色数最少。

## Input

输入仅一行，包含一个整数 $n$（$2\leq n \leq 6000$），表示主街道上的房屋数量。

## Output

输出 $n$ 个数的序列，其中第 $i$ 个数表示第 $i$ 号房子所使用的颜色编号。颜色编号从 1 开始连续编号。房子的涂色顺序任意，如果有多种涂色方案，输出任意一种即可。如果无法完成涂色，输出单独的一个 $-1$。

## Samples

### Sample 1

Input
```
8
```

Output
```
1 2 2 1 1 1 1 2
```

## Note

由 ChatGPT 5 翻译

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-45G |
| Contest | 45 |
| Index | G |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `number theory` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 1216 |
| 镜像尝试 / 通过 | 1868 / 681 |
| 时限 | 1000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/45/G)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/45/problem/G)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF45G)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

