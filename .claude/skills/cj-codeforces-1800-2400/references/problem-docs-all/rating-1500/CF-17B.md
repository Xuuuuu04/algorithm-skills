# CF-17B Hierarchy

## 题面快照

## Description

Nick's company employed n people. Now Nick needs to build a tree hierarchy of «supervisor-surbodinate» relations in the company (this is to say that each employee, except one, has exactly one supervisor). There are m applications written in the following form: «employee ai is ready to become a supervisor of employee bi at extra cost ci». The qualification qj of each employee is known, and for each application the following is true: qai > qbi.

Would you help Nick calculate the minimum cost of such a hierarchy, or find out that it is impossible to build it.

The first input line contains integer n (1 ≤ n ≤ 1000) — amount of employees in the company. The following line contains n space-separated numbers qj (0 ≤ qj ≤ 106)— the employees' qualifications. The following line contains number m (0 ≤ m ≤ 10000) — amount of received applications. The following m lines contain the applications themselves, each of them in the form of three space-separated numbers: ai, bi and ci (1 ≤ ai, bi ≤ n, 0 ≤ ci ≤ 106). Different applications can be similar, i.e. they can come from one and the same employee who offered to become a supervisor of the same person but at a different cost. For each application qai > qbi.

Output the only line — the minimum cost of building such a hierarchy, or -1 if it is impossible to build it.

## Input

The first input line contains integer n (1 ≤ n ≤ 1000) — amount of employees in the company. The following line contains n space-separated numbers qj (0 ≤ qj ≤ 106)— the employees' qualifications. The following line contains number m (0 ≤ m ≤ 10000) — amount of received applications. The following m lines contain the applications themselves, each of them in the form of three space-separated numbers: ai, bi and ci (1 ≤ ai, bi ≤ n, 0 ≤ ci ≤ 106). Different applications can be similar, i.e. they can come from one and the same employee who offered to become a supervisor of the same person but at a different cost. For each application qai > qbi.

## Output

Output the only line — the minimum cost of building such a hierarchy, or -1 if it is impossible to build it.

## Samples

```
4
7 2 3 1
4
1 2 5
2 4 1
3 4 1
1 3 5

```

```
11

```

```
3
1 2 3
2
3 1 2
3 1 3

```

```
-1

```

## Note

In the first sample one of the possible ways for building a hierarchy is to take applications with indexes 1, 2 and 4, which give 11 as the minimum total cost. In the second sample it is impossible to build the required hierarchy, so the answer is -1.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-17B |
| Contest | 17 |
| Index | B |
| Rating | 1500 |
| Points | - |
| Codeforces 标签 | `dfs and similar`、`dsu`、`greedy`、`shortest paths` |
| 镜像标签 | `dfs and similar`、`dsu`、`greedy`、`shortest paths`、`*1500` |
| Codeforces 通过次数 | 5908 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/17/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/17/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P17B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

