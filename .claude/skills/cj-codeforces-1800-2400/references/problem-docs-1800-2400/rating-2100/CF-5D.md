# CF-5D Follow Traffic Rules

## 题面快照

## Description

Everybody knows that the capital of Berland is connected to Bercouver (the Olympic capital) by a direct road. To improve the road's traffic capacity, there was placed just one traffic sign, limiting the maximum speed. Traffic signs in Berland are a bit peculiar, because they limit the speed only at that point on the road where they are placed. Right after passing the sign it is allowed to drive at any speed.

It is known that the car of an average Berland citizen has the acceleration (deceleration) speed of a km/h2, and has maximum speed of v km/h. The road has the length of l km, and the speed sign, limiting the speed to w km/h, is placed d km (1 ≤ d < l) away from the capital of Berland. The car has a zero speed at the beginning of the journey. Find the minimum time that an average Berland citizen will need to get from the capital to Bercouver, if he drives at the optimal speed.

The car can enter Bercouver at any speed.

The first line of the input file contains two integer numbers a and v (1 ≤ a, v ≤ 10000). The second line contains three integer numbers l, d and w (2 ≤ l ≤ 10000; 1 ≤ d < l; 1 ≤ w ≤ 10000).

Print the answer with at least five digits after the decimal point.

## Input

The first line of the input file contains two integer numbers a and v (1 ≤ a, v ≤ 10000). The second line contains three integer numbers l, d and w (2 ≤ l ≤ 10000; 1 ≤ d < l; 1 ≤ w ≤ 10000).

## Output

Print the answer with at least five digits after the decimal point.

## Samples

```
1 1
2 1 3

```

```
2.500000000000

```

```
5 70
200 170 40

```

```
8.965874696353

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-5D |
| Contest | 5 |
| Index | D |
| Rating | 2100 |
| Points | - |
| Codeforces 标签 | `implementation`、`math` |
| 镜像标签 | `implementation`、`math`、`*2100` |
| Codeforces 通过次数 | 1902 |
| 镜像尝试 / 通过 | 2 / 1 |
| 时限 | 1000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/5/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/5/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P5D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

