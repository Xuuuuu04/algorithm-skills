# CF-93E Lostborn

## 题面快照

## Description

Igor K. very much likes a multiplayer role playing game WineAge II. Who knows, perhaps, that might be the reason for his poor performance at the university. As any person who plays the game, he is interested in equipping his hero with as good weapon and outfit as possible.

One day, as he was reading the game's forum yet again, he discovered a very interesting fact. As it turns out, each weapon in the game is characterised with k different numbers: a1, ..., ak. They are called hit indicators and according to the game developers' plan they are pairwise coprime.

The damage that is inflicted during a hit depends not only on the weapon's characteristics, but also on the hero's strength parameter. Thus, if the hero's strength equals n, than the inflicted damage will be calculated as the number of numbers on the segment , that aren't divisible by any hit indicator ai.

Recently, having fulfilled another quest, Igor K. found a new Lostborn sword. He wants to know how much damage he will inflict upon his enemies if he uses it.

The first line contains two integers: n and k (1 ≤ n ≤ 1013, 1 ≤ k ≤ 100). They are the indicator of Igor K's hero's strength and the number of hit indicators.

The next line contains space-separated k integers ai (1 ≤ ai ≤ 1000). They are Lostborn sword's hit indicators. The given k numbers are pairwise coprime.

Print the single number — the damage that will be inflicted by Igor K.'s hero when he uses his new weapon.

Please, do not use the %lld specificator to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specificator.

## Input

The first line contains two integers: n and k (1 ≤ n ≤ 1013, 1 ≤ k ≤ 100). They are the indicator of Igor K's hero's strength and the number of hit indicators.

The next line contains space-separated k integers ai (1 ≤ ai ≤ 1000). They are Lostborn sword's hit indicators. The given k numbers are pairwise coprime.

## Output

Print the single number — the damage that will be inflicted by Igor K.'s hero when he uses his new weapon.

Please, do not use the %lld specificator to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specificator.

## Samples

```
20 3
2 3 5

```

```
6

```

```
50 2
15 8

```

```
41

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-93E |
| Contest | 93 |
| Index | E |
| Rating | 2600 |
| Points | 2500.0 |
| Codeforces 标签 | `dp`、`math`、`number theory` |
| 镜像标签 | `dp`、`math`、`number theory`、`*2600` |
| Codeforces 通过次数 | 538 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/93/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/93/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P93E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

