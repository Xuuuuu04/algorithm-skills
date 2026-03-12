# CF-39F Pacifist frogs

## 题面快照

## Description

Thumbelina has had an accident. She has found herself on a little island in the middle of a swamp and wants to get to the shore very much.

One can get to the shore only by hills that are situated along a straight line that connects the little island with the shore. Let us assume that the hills are numbered from 1 to n and the number of a hill is equal to the distance in meters between it and the island. The distance between the n-th hill and the shore is also 1 meter.

Thumbelina is too small to make such jumps. Fortunately, a family of frogs living in the swamp suggests to help her. Each frog agrees to give Thumbelina a ride but Thumbelina should choose only one frog. Each frog has a certain jump length. If Thumbelina agrees to accept help from a frog whose jump length is d, the frog will jump from the island on the hill d, then — on the hill 2d, then 3d and so on until they get to the shore (i.e. find itself beyond the hill n).

However, there is one more problem: mosquitoes also live in the swamp. At the moment they have a siesta, and they are having a nap on some hills. If the frog jumps on a hill with a mosquito the frog will smash it. The frogs Thumbelina has met are pacifists, so they will find the death of each mosquito very much sad. Help Thumbelina choose a frog that will bring her to the shore and smash as small number of mosquitoes as possible.

## Input

Input

The first line contains three integers n, m and k (1 ≤ n ≤ 109, 1 ≤ m, k ≤ 100) — the number of hills, frogs and mosquitoes respectively. The second line contains m integers di (1 ≤ di ≤ 109) — the lengths of the frogs’ jumps. The third line contains k integers — the numbers of the hills on which each mosquito is sleeping. No more than one mosquito can sleep on each hill. The numbers in the lines are separated by single spaces.

## Output

Output

In the first line output the number of frogs that smash the minimal number of mosquitoes, in the second line — their numbers in increasing order separated by spaces. The frogs are numbered from 1 to m in the order of the jump length given in the input data.

## Samples

### Sample 1

Input
```
5 3 5
2 3 4
1 2 3 4 5
```

Output
```
2
2 3
```

### Sample 2

Input
```
1000000000 2 3
2 5
999999995 999999998 999999996
```

Output
```
1
2
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Codeforces 官方镜像 |
| 编号 | CF-39F |
| Contest | 39 |
| Index | F |
| Rating | 1300 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 1937 |
| 镜像尝试 / 通过 | - / - |
| 时限 | 2 seconds |
| 内存限制 | 64 megabytes |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/39/F)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/39/problem/F)
- Codeforces 官方镜像：[mirror](https://mirror.codeforces.com/problemset/problem/39/F)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

