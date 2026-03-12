# CF-60C Mushroom Strife

## 题面快照

## Description

Pasha and Akim were making a forest map — the lawns were the graph's vertexes and the roads joining the lawns were its edges. They decided to encode the number of laughy mushrooms on every lawn in the following way: on every edge between two lawns they wrote two numbers, the greatest common divisor (GCD) and the least common multiple (LCM) of the number of mushrooms on these lawns. But one day Pasha and Akim had an argument about the laughy mushrooms and tore the map. Pasha was left with just some part of it, containing only m roads. Your task is to help Pasha — use the map he has to restore the number of mushrooms on every lawn. As the result is not necessarily unique, help Pasha to restore any one or report that such arrangement of mushrooms does not exist. It is guaranteed that the numbers on the roads on the initial map were no less that 1 and did not exceed 106.

The first line contains two numbers n and m () which are the numbers of lawns and roads we know about. Each of the following m lines contains four numbers which are the numbers of lawns the road connects, the GCD and the LCM of the numbers of mushrooms on these lawns (1 ≤ GCD, LCM ≤ 106).

It is guaranteed, that no road connects lawn to itself, and no two lawns are connected by more than one road.

The answer should contain "YES" or "NO" on the first line, saying whether it is possible or not to perform the arrangement. If the answer is "YES", print on the following line n numbers which are the numbers of mushrooms on the corresponding lawns.

## Input

The first line contains two numbers n and m () which are the numbers of lawns and roads we know about. Each of the following m lines contains four numbers which are the numbers of lawns the road connects, the GCD and the LCM of the numbers of mushrooms on these lawns (1 ≤ GCD, LCM ≤ 106).

It is guaranteed, that no road connects lawn to itself, and no two lawns are connected by more than one road.

## Output

The answer should contain "YES" or "NO" on the first line, saying whether it is possible or not to perform the arrangement. If the answer is "YES", print on the following line n numbers which are the numbers of mushrooms on the corresponding lawns.

## Samples

```
1 0

```

```
YES
1

```

```
2 1
1 2 1 3

```

```
YES
1 3

```

```
3 2
3 2 1 2
3 1 1 10

```

```
YES
5 1 2

```

```
2 1
1 2 3 7

```

```
NO

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-60C |
| Contest | 60 |
| Index | C |
| Rating | 2100 |
| Points | 1500.0 |
| Codeforces 标签 | `brute force`、`dfs and similar` |
| 镜像标签 | `brute force`、`dfs and similar`、`*2100` |
| Codeforces 通过次数 | 649 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/60/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/60/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P60C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

