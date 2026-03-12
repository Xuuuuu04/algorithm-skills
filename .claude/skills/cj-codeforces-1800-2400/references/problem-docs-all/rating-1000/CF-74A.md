# CF-74A Room Leader

## 题面快照

## Description

Let us remind you part of the rules of Codeforces. The given rules slightly simplified, use the problem statement as a formal document.

In the beginning of the round the contestants are divided into rooms. Each room contains exactly n participants. During the contest the participants are suggested to solve five problems, A, B, C, D and E. For each of these problem, depending on when the given problem was solved and whether it was solved at all, the participants receive some points. Besides, a contestant can perform hacks on other contestants. For each successful hack a contestant earns 100 points, for each unsuccessful hack a contestant loses 50 points. The number of points for every contestant is represented by the sum of points he has received from all his problems, including hacks.

You are suggested to determine the leader for some room; the leader is a participant who has maximum points.

The first line contains an integer n, which is the number of contestants in the room (1 ≤ n ≤ 50). The next n lines contain the participants of a given room. The i-th line has the format of "handleiplusiminusiaibicidiei" — it is the handle of a contestant, the number of successful hacks, the number of unsuccessful hacks and the number of points he has received from problems A, B, C, D, E correspondingly. The handle of each participant consists of Latin letters, digits and underscores and has the length from 1 to 20 characters. There are the following limitations imposed upon the numbers:

- 0 ≤ plusi, minusi ≤ 50;

- 150 ≤ ai ≤ 500 or ai = 0, if problem A is not solved;

- 300 ≤ bi ≤ 1000 or bi = 0, if problem B is not solved;

- 450 ≤ ci ≤ 1500 or ci = 0, if problem C is not solved;

- 600 ≤ di ≤ 2000 or di = 0, if problem D is not solved;

- 750 ≤ ei ≤ 2500 or ei = 0, if problem E is not solved.

All the numbers are integer. All the participants have different handles. It is guaranteed that there is exactly one leader in the room (i.e. there are no two participants with the maximal number of points).

Print on the single line the handle of the room leader.

## Input

The first line contains an integer n, which is the number of contestants in the room (1 ≤ n ≤ 50). The next n lines contain the participants of a given room. The i-th line has the format of "handleiplusiminusiaibicidiei" — it is the handle of a contestant, the number of successful hacks, the number of unsuccessful hacks and the number of points he has received from problems A, B, C, D, E correspondingly. The handle of each participant consists of Latin letters, digits and underscores and has the length from 1 to 20 characters. There are the following limitations imposed upon the numbers:

- 0 ≤ plusi, minusi ≤ 50;

- 150 ≤ ai ≤ 500 or ai = 0, if problem A is not solved;

- 300 ≤ bi ≤ 1000 or bi = 0, if problem B is not solved;

- 450 ≤ ci ≤ 1500 or ci = 0, if problem C is not solved;

- 600 ≤ di ≤ 2000 or di = 0, if problem D is not solved;

- 750 ≤ ei ≤ 2500 or ei = 0, if problem E is not solved.

All the numbers are integer. All the participants have different handles. It is guaranteed that there is exactly one leader in the room (i.e. there are no two participants with the maximal number of points).

## Output

Print on the single line the handle of the room leader.

## Samples

```
5
Petr 3 1 490 920 1000 1200 0
tourist 2 0 490 950 1100 1400 0
Egor 7 0 480 900 950 0 1000
c00lH4x0R 0 10 150 0 0 0 0
some_participant 2 1 450 720 900 0 0

```

```
tourist

```

## Note

The number of points that each participant from the example earns, are as follows:

- Petr — 3860

- tourist — 4140

- Egor — 4030

- c00lH4x0R —  - 350

- some_participant — 2220

Thus, the leader of the room is tourist.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-74A |
| Contest | 74 |
| Index | A |
| Rating | 1000 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1000` |
| Codeforces 通过次数 | 5766 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/74/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/74/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P74A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

