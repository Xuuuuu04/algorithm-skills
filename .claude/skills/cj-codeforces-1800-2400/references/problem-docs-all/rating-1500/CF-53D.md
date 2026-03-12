# CF-53D Physical Education

## 题面快照

## Description

Vasya is a school PE teacher. Unlike other PE teachers, Vasya doesn't like it when the students stand in line according to their height. Instead, he demands that the children stand in the following order: a1, a2, ..., an, where ai is the height of the i-th student in the line and n is the number of students in the line. The children find it hard to keep in mind this strange arrangement, and today they formed the line in the following order: b1, b2, ..., bn, which upset Vasya immensely. Now Vasya wants to rearrange the children so that the resulting order is like this: a1, a2, ..., an. During each move Vasya can swap two people who stand next to each other in the line. Help Vasya, find the sequence of swaps leading to the arrangement Vasya needs. It is not required to minimize the number of moves.

The first line contains an integer n (1 ≤ n ≤ 300) which is the number of students. The second line contains n space-separated integers ai (1 ≤ ai ≤ 109) which represent the height of the student occupying the i-th place must possess. The third line contains n space-separated integers bi (1 ≤ bi ≤ 109) which represent the height of the student occupying the i-th place in the initial arrangement. It is possible that some students possess similar heights. It is guaranteed that it is possible to arrange the children in the required order, i.e. a and b coincide as multisets.

In the first line print an integer k (0 ≤ k ≤ 106) which is the number of moves. It is not required to minimize k but it must not exceed 106. Then print k lines each containing two space-separated integers. Line pi, pi + 1 (1 ≤ pi ≤ n - 1) means that Vasya should swap students occupying places pi and pi + 1.

## Input

The first line contains an integer n (1 ≤ n ≤ 300) which is the number of students. The second line contains n space-separated integers ai (1 ≤ ai ≤ 109) which represent the height of the student occupying the i-th place must possess. The third line contains n space-separated integers bi (1 ≤ bi ≤ 109) which represent the height of the student occupying the i-th place in the initial arrangement. It is possible that some students possess similar heights. It is guaranteed that it is possible to arrange the children in the required order, i.e. a and b coincide as multisets.

## Output

In the first line print an integer k (0 ≤ k ≤ 106) which is the number of moves. It is not required to minimize k but it must not exceed 106. Then print k lines each containing two space-separated integers. Line pi, pi + 1 (1 ≤ pi ≤ n - 1) means that Vasya should swap students occupying places pi and pi + 1.

## Samples

```
4
1 2 3 2
3 2 1 2

```

```
4
2 3
1 2
3 4
2 3

```

```
2
1 100500
1 100500

```

```
0

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-53D |
| Contest | 53 |
| Index | D |
| Rating | 1500 |
| Points | 2000.0 |
| Codeforces 标签 | `sortings` |
| 镜像标签 | `sortings`、`*1500` |
| Codeforces 通过次数 | 2531 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/53/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/53/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P53D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

