# CF-67D Optical Experiment

## 题面快照

## Description

Professor Phunsuk Wangdu has performed some experiments on rays. The setup for n rays is as follows.

There is a rectangular box having exactly n holes on the opposite faces. All rays enter from the holes of the first side and exit from the holes of the other side of the box. Exactly one ray can enter or exit from each hole. The holes are in a straight line.

Professor Wangdu is showing his experiment to his students. He shows that there are cases, when all the rays are intersected by every other ray. A curious student asked the professor: "Sir, there are some groups of rays such that all rays in that group intersect every other ray in that group. Can we determine the number of rays in the largest of such groups?".

Professor Wangdu now is in trouble and knowing your intellect he asks you to help him.

The first line contains n (1 ≤ n ≤ 106), the number of rays. The second line contains n distinct integers. The i-th integer xi (1 ≤ xi ≤ n) shows that the xi-th ray enters from the i-th hole. Similarly, third line contains n distinct integers. The i-th integer yi (1 ≤ yi ≤ n) shows that the yi-th ray exits from the i-th hole. All rays are numbered from 1 to n.

Output contains the only integer which is the number of rays in the largest group of rays all of which intersect each other.

## Input

The first line contains n (1 ≤ n ≤ 106), the number of rays. The second line contains n distinct integers. The i-th integer xi (1 ≤ xi ≤ n) shows that the xi-th ray enters from the i-th hole. Similarly, third line contains n distinct integers. The i-th integer yi (1 ≤ yi ≤ n) shows that the yi-th ray exits from the i-th hole. All rays are numbered from 1 to n.

## Output

Output contains the only integer which is the number of rays in the largest group of rays all of which intersect each other.

## Samples

```
5
1 4 5 2 3
3 4 2 1 5

```

```
3

```

```
3
3 1 2
2 3 1

```

```
2

```

## Note

For the first test case, the figure is shown above. The output of the first test case is 3, since the rays number 1, 4 and 3 are the ones which are intersected by each other one i.e. 1 is intersected by 4 and 3, 3 is intersected by 4 and 1, and 4 is intersected by 1 and 3. Hence every ray in this group is intersected by each other one. There does not exist any group containing more than 3 rays satisfying the above-mentioned constraint.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-67D |
| Contest | 67 |
| Index | D |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `binary search`、`data structures`、`dp` |
| 镜像标签 | `binary search`、`data structures`、`dp`、`*1900` |
| Codeforces 通过次数 | 1747 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/67/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/67/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P67D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

