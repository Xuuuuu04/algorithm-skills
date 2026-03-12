# CF-76F Tourist

## 题面快照

## Description

Tourist walks along the X axis. He can choose either of two directions and any speed not exceeding V. He can also stand without moving anywhere. He knows from newspapers that at time t1 in the point with coordinate x1 an interesting event will occur, at time t2 in the point with coordinate x2 — another one, and so on up to (xn, tn). Interesting events are short so we can assume they are immediate. Event i counts visited if at time ti tourist was at point with coordinate xi.

Write program tourist that will find maximum number of events tourist if:

-  at the beginning (when time is equal to 0) tourist appears at point 0,

-  tourist can choose initial point for himself.

Yes, you should answer on two similar but different questions.

The first line of input contains single integer number N (1 ≤ N ≤ 100000) — number of interesting events. The following N lines contain two integers xi and ti — coordinate and time of the i-th event. The last line of the input contains integer V — maximum speed of the tourist. All xi will be within range  - 2·108 ≤ xi ≤ 2·108, all ti will be between 1 and 2·106 inclusive. V will be positive and will not exceed 1000. The input may contain events that happen at the same time or in the same place but not in the same place at the same time.

The only line of the output should contain two space-sepatated integers — maximum number of events tourist can visit in he starts moving from point 0 at time 0, and maximum number of events tourist can visit if he chooses the initial point for himself.

## Input

The first line of input contains single integer number N (1 ≤ N ≤ 100000) — number of interesting events. The following N lines contain two integers xi and ti — coordinate and time of the i-th event. The last line of the input contains integer V — maximum speed of the tourist. All xi will be within range  - 2·108 ≤ xi ≤ 2·108, all ti will be between 1 and 2·106 inclusive. V will be positive and will not exceed 1000. The input may contain events that happen at the same time or in the same place but not in the same place at the same time.

## Output

The only line of the output should contain two space-sepatated integers — maximum number of events tourist can visit in he starts moving from point 0 at time 0, and maximum number of events tourist can visit if he chooses the initial point for himself.

## Samples

```
3
-1 1
42 7
40 8
2

```

```
1 2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-76F |
| Contest | 76 |
| Index | F |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `binary search`、`data structures`、`dp` |
| 镜像标签 | `binary search`、`data structures`、`dp`、`*2300` |
| Codeforces 通过次数 | 759 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/76/F)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/76/problem/F)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P76F)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

