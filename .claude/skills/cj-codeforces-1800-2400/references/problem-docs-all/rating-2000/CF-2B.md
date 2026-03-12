# CF-2B The least round way

## 题面快照

## Description

给定由非负整数组成的 $n\times n$ 的正方形矩阵，你需要寻找一条路径：

+ 以左上角为起点。
+ 每次只能向右或向下走。
+ 以右下角为终点。
+ 如果我们把沿路遇到的数进行相乘，积应当以尽可能少的 $0$ 结尾。

## Input

第一行包含一个整数 $n (2 \leq n \leq 1000)$，$n$ 为矩阵的规模，接下来的 $n$ 行包含矩阵的元素（不超过 $10^9$ 的非负整数）。

## Output

第一行应包含结尾最少的 $0$ 的个数，第二行打印出相应的路径（译注：`D` 为下，`R`  为右）。

## Samples

### Sample 1

Input
```
3
1 2 3
4 5 6
7 8 9
```

Output
```
0
DDRR
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-2B |
| Contest | 2 |
| Index | B |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `dp`、`math` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 12750 |
| 镜像尝试 / 通过 | 8630 / 1822 |
| 时限 | 2000 ms |
| 内存限制 | 64000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/2/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/2/problem/B)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF2B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

