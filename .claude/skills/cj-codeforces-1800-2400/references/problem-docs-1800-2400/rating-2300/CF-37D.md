# CF-37D Lesson Timetable

## 题面快照

## Description

When Petya has free from computer games time, he attends university classes. Every day the lessons on Petya’s faculty consist of two double classes. The floor where the lessons take place is a long corridor with M classrooms numbered from 1 to M, situated along it.

All the students of Petya’s year are divided into N groups. Petya has noticed recently that these groups’ timetable has the following peculiarity: the number of the classroom where the first lesson of a group takes place does not exceed the number of the classroom where the second lesson of this group takes place.

Once Petya decided to count the number of ways in which one can make a lesson timetable for all these groups. The timetable is a set of 2N numbers: for each group the number of the rooms where the first and the second lessons take place. Unfortunately, he quickly lost the track of his calculations and decided to count only the timetables that satisfy the following conditions:

1) On the first lesson in classroom i exactly Xi groups must be present.

2) In classroom i no more than Yi groups may be placed.

Help Petya count the number of timetables satisfying all those conditionsю As there can be a lot of such timetables, output modulo 109 + 7.

The first line contains one integer M (1 ≤ M ≤ 100) — the number of classrooms.

The second line contains M space-separated integers — Xi (0 ≤ Xi ≤ 100) the amount of groups present in classroom i during the first lesson.

The third line contains M space-separated integers — Yi (0 ≤ Yi ≤ 100) the maximal amount of groups that can be present in classroom i at the same time.

It is guaranteed that all the Xi ≤ Yi, and that the sum of all the Xi is positive and does not exceed 1000.

In the single line output the answer to the problem modulo 109 + 7.

## Input

The first line contains one integer M (1 ≤ M ≤ 100) — the number of classrooms.

The second line contains M space-separated integers — Xi (0 ≤ Xi ≤ 100) the amount of groups present in classroom i during the first lesson.

The third line contains M space-separated integers — Yi (0 ≤ Yi ≤ 100) the maximal amount of groups that can be present in classroom i at the same time.

It is guaranteed that all the Xi ≤ Yi, and that the sum of all the Xi is positive and does not exceed 1000.

## Output

In the single line output the answer to the problem modulo 109 + 7.

## Samples

```
3
1 1 1
1 2 3

```

```
36

```

```
3
1 1 1
1 1 1

```

```
6

```

## Note

In the second sample test the first and the second lessons of each group must take place in the same classroom, that’s why the timetables will only be different in the rearrangement of the classrooms’ numbers for each group, e.g. 3! = 6.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-37D |
| Contest | 37 |
| Index | D |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `combinatorics`、`dp`、`math` |
| 镜像标签 | `combinatorics`、`dp`、`math`、`*2300` |
| Codeforces 通过次数 | 507 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/37/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/37/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P37D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

