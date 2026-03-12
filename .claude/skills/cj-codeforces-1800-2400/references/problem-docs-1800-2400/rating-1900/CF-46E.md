# CF-46E Comb

## 题面快照

## Description

Having endured all the hardships, Lara Croft finally found herself in a room with treasures. To her surprise she didn't find golden mountains there. Lara looked around and noticed on the floor a painted table n × m panels in size with integers written on the panels. There also was a huge number of stones lying by the wall. On the pillar near the table Lara found a guidance note which said that to get hold of the treasures one has to choose some non-zero number of the first panels in each row of the table and put stones on all those panels to push them down. After that she will receive a number of golden coins equal to the sum of numbers written on the chosen panels. Lara quickly made up her mind on how to arrange the stones and was about to start when she noticed an addition to the note in small font below. According to the addition, for the room ceiling not to crush and smash the adventurer, the chosen panels should form a comb. It was explained that the chosen panels form a comb when the sequence c1, c2, ..., cn made from the quantities of panels chosen in each table line satisfies the following property: c1 > c2 < c3 > c4 < ..., i.e. the inequation mark interchanges between the neighboring elements. Now Lara is bewildered and doesn't know what to do. Help her to determine the largest number of coins she can get and survive at the same time.

The first line contains a pair of integers n, m (2 ≤ n, m ≤ 1500). Next n lines contain m integers each — that is the table itself. The absolute value of the numbers in the table does not exceed 10000.

Print the single number — the maximum number of coins Lara can get.

## Input

The first line contains a pair of integers n, m (2 ≤ n, m ≤ 1500). Next n lines contain m integers each — that is the table itself. The absolute value of the numbers in the table does not exceed 10000.

## Output

Print the single number — the maximum number of coins Lara can get.

## Samples

```
2 2
-1 2
1 3

```

```
2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-46E |
| Contest | 46 |
| Index | E |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `data structures`、`dp` |
| 镜像标签 | `data structures`、`dp`、`*1900` |
| Codeforces 通过次数 | 1144 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/46/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/46/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P46E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

