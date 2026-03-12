# CF-29A Spit Problem

## 题面快照

## Description

In a Berland's zoo there is an enclosure with camels. It is known that camels like to spit. Bob watched these interesting animals for the whole day and registered in his notepad where each animal spitted. Now he wants to know if in the zoo there are two camels, which spitted at each other. Help him to solve this task.

The trajectory of a camel's spit is an arc, i.e. if the camel in position x spits d meters right, he can hit only the camel in position x + d, if such a camel exists.

The first line contains integer n (1 ≤ n ≤ 100) — the amount of camels in the zoo. Each of the following n lines contains two integers xi and di ( - 104 ≤ xi ≤ 104, 1 ≤ |di| ≤ 2·104) — records in Bob's notepad. xi is a position of the i-th camel, and di is a distance at which the i-th camel spitted. Positive values of di correspond to the spits right, negative values correspond to the spits left. No two camels may stand in the same position.

If there are two camels, which spitted at each other, output YES. Otherwise, output NO.

## Input

The first line contains integer n (1 ≤ n ≤ 100) — the amount of camels in the zoo. Each of the following n lines contains two integers xi and di ( - 104 ≤ xi ≤ 104, 1 ≤ |di| ≤ 2·104) — records in Bob's notepad. xi is a position of the i-th camel, and di is a distance at which the i-th camel spitted. Positive values of di correspond to the spits right, negative values correspond to the spits left. No two camels may stand in the same position.

## Output

If there are two camels, which spitted at each other, output YES. Otherwise, output NO.

## Samples

```
2
0 1
1 -1

```

```
YES

```

```
3
0 1
1 1
2 -2

```

```
NO

```

```
5
2 -10
3 10
0 5
5 -5
10 1

```

```
YES

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-29A |
| Contest | 29 |
| Index | A |
| Rating | 1000 |
| Points | 500.0 |
| Codeforces 标签 | `brute force` |
| 镜像标签 | `brute force`、`*1000` |
| Codeforces 通过次数 | 8119 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/29/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/29/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P29A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

