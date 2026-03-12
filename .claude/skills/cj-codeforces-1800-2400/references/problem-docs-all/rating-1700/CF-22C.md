# CF-22C System Administrator

## 题面快照

## Description

Bob got a job as a system administrator in X corporation. His first task was to connect n servers with the help of m two-way direct connection so that it becomes possible to transmit data from one server to any other server via these connections. Each direct connection has to link two different servers, each pair of servers should have at most one direct connection. Y corporation, a business rival of X corporation, made Bob an offer that he couldn't refuse: Bob was asked to connect the servers in such a way, that when server with index v fails, the transmission of data between some other two servers becomes impossible, i.e. the system stops being connected. Help Bob connect the servers.

The first input line contains 3 space-separated integer numbers n, m, v (3 ≤ n ≤ 105, 0 ≤ m ≤ 105, 1 ≤ v ≤ n), n — amount of servers, m — amount of direct connections, v — index of the server that fails and leads to the failure of the whole system.

If it is impossible to connect the servers in the required way, output -1. Otherwise output m lines with 2 numbers each — description of all the direct connections in the system. Each direct connection is described by two numbers — indexes of two servers, linked by this direct connection. The servers are numbered from 1. If the answer is not unique, output any.

## Input

The first input line contains 3 space-separated integer numbers n, m, v (3 ≤ n ≤ 105, 0 ≤ m ≤ 105, 1 ≤ v ≤ n), n — amount of servers, m — amount of direct connections, v — index of the server that fails and leads to the failure of the whole system.

## Output

If it is impossible to connect the servers in the required way, output -1. Otherwise output m lines with 2 numbers each — description of all the direct connections in the system. Each direct connection is described by two numbers — indexes of two servers, linked by this direct connection. The servers are numbered from 1. If the answer is not unique, output any.

## Samples

```
5 6 3

```

```
1 2
2 3
3 4
4 5
1 3
3 5

```

```
6 100 1

```

```
-1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-22C |
| Contest | 22 |
| Index | C |
| Rating | 1700 |
| Points | - |
| Codeforces 标签 | `graphs` |
| 镜像标签 | `graphs`、`*1700` |
| Codeforces 通过次数 | 3738 |
| 镜像尝试 / 通过 | 3 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/22/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/22/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P22C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

