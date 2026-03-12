# CF-91B Queue

## 题面快照

## Description

There are n walruses standing in a queue in an airport. They are numbered starting from the queue's tail: the 1-st walrus stands at the end of the queue and the n-th walrus stands at the beginning of the queue. The i-th walrus has the age equal to ai.

The i-th walrus becomes displeased if there's a younger walrus standing in front of him, that is, if exists such j (i < j), that ai > aj. The displeasure of the i-th walrus is equal to the number of walruses between him and the furthest walrus ahead of him, which is younger than the i-th one. That is, the further that young walrus stands from him, the stronger the displeasure is.

The airport manager asked you to count for each of n walruses in the queue his displeasure.

The first line contains an integer n (2 ≤ n ≤ 105) — the number of walruses in the queue. The second line contains integers ai (1 ≤ ai ≤ 109).

Note that some walruses can have the same age but for the displeasure to emerge the walrus that is closer to the head of the queue needs to be strictly younger than the other one.

Print n numbers: if the i-th walrus is pleased with everything, print "-1" (without the quotes). Otherwise, print the i-th walrus's displeasure: the number of other walruses that stand between him and the furthest from him younger walrus.

## Input

The first line contains an integer n (2 ≤ n ≤ 105) — the number of walruses in the queue. The second line contains integers ai (1 ≤ ai ≤ 109).

Note that some walruses can have the same age but for the displeasure to emerge the walrus that is closer to the head of the queue needs to be strictly younger than the other one.

## Output

Print n numbers: if the i-th walrus is pleased with everything, print "-1" (without the quotes). Otherwise, print the i-th walrus's displeasure: the number of other walruses that stand between him and the furthest from him younger walrus.

## Samples

```
6
10 8 5 3 50 45

```

```
2 1 0 -1 0 -1

```

```
7
10 4 6 3 2 8 15

```

```
4 2 1 0 -1 -1 -1

```

```
5
10 3 1 10 11

```

```
1 0 -1 -1 -1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-91B |
| Contest | 91 |
| Index | B |
| Rating | 1500 |
| Points | 1000.0 |
| Codeforces 标签 | `binary search`、`data structures` |
| 镜像标签 | `binary search`、`data structures`、`*1500` |
| Codeforces 通过次数 | 7579 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/91/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/91/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P91B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

