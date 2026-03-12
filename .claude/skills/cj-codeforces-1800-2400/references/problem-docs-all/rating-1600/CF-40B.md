# CF-40B Repaintings

## 题面快照

## Description

A chessboard n × m in size is given. During the zero minute we repaint all the black squares to the 0 color. During the i-th minute we repaint to the i color the initially black squares that have exactly four corner-adjacent squares painted i - 1 (all such squares are repainted simultaneously). This process continues ad infinitum. You have to figure out how many squares we repainted exactly x times.

The upper left square of the board has to be assumed to be always black. Two squares are called corner-adjacent, if they have exactly one common point.

The first line contains integers n and m (1 ≤ n, m ≤ 5000). The second line contains integer x (1 ≤ x ≤ 109).

Print how many squares will be painted exactly x times.

## Input

The first line contains integers n and m (1 ≤ n, m ≤ 5000). The second line contains integer x (1 ≤ x ≤ 109).

## Output

Print how many squares will be painted exactly x times.

## Samples

```
3 3
1

```

```
4

```

```
3 3
2

```

```
1

```

```
1 1
1

```

```
1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-40B |
| Contest | 40 |
| Index | B |
| Rating | 1600 |
| Points | 1000.0 |
| Codeforces 标签 | `math` |
| 镜像标签 | `math`、`*1600` |
| Codeforces 通过次数 | 1373 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/40/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/40/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P40B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

