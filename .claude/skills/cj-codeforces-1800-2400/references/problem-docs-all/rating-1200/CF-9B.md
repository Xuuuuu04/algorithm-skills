# CF-9B Running Student

## 题面快照

## Description

And again a misfortune fell on Poor Student. He is being late for an exam.

Having rushed to a bus stop that is in point (0, 0), he got on a minibus and they drove along a straight line, parallel to axis OX, in the direction of increasing x.

Poor Student knows the following:

-  during one run the minibus makes n stops, the i-th stop is in point (xi, 0)

-  coordinates of all the stops are different

-  the minibus drives at a constant speed, equal to vb

-  it can be assumed the passengers get on and off the minibus at a bus stop momentarily

-  Student can get off the minibus only at a bus stop

-  Student will have to get off the minibus at a terminal stop, if he does not get off earlier

-  the University, where the exam will be held, is in point (xu, yu)

-  Student can run from a bus stop to the University at a constant speed vs as long as needed

-  a distance between two points can be calculated according to the following formula:

-  Student is already on the minibus, so, he cannot get off at the first bus stop

Poor Student wants to get to the University as soon as possible. Help him to choose the bus stop, where he should get off. If such bus stops are multiple, choose the bus stop closest to the University.

The first line contains three integer numbers: 2 ≤ n ≤ 100, 1 ≤ vb, vs ≤ 1000. The second line contains n non-negative integers in ascending order: coordinates xi of the bus stop with index i. It is guaranteed that x1 equals to zero, and xn ≤ 105. The third line contains the coordinates of the University, integers xu and yu, not exceeding 105 in absolute value.

In the only line output the answer to the problem — index of the optimum bus stop.

## Input

The first line contains three integer numbers: 2 ≤ n ≤ 100, 1 ≤ vb, vs ≤ 1000. The second line contains n non-negative integers in ascending order: coordinates xi of the bus stop with index i. It is guaranteed that x1 equals to zero, and xn ≤ 105. The third line contains the coordinates of the University, integers xu and yu, not exceeding 105 in absolute value.

## Output

In the only line output the answer to the problem — index of the optimum bus stop.

## Samples

```
4 5 2
0 2 4 6
4 1

```

```
3

```

```
2 1 1
0 100000
100000 100000

```

```
2

```

## Note

As you know, students are a special sort of people, and minibuses usually do not hurry. That's why you should not be surprised, if Student's speed is higher than the speed of the minibus.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-9B |
| Contest | 9 |
| Index | B |
| Rating | 1200 |
| Points | - |
| Codeforces 标签 | `brute force`、`geometry`、`implementation` |
| 镜像标签 | `brute force`、`geometry`、`implementation`、`*1200` |
| Codeforces 通过次数 | 6129 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/9/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/9/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P9B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

