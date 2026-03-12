# CF-44D Hyperdrive

## 题面快照

## Description

In a far away galaxy there are n inhabited planets, numbered with numbers from 1 to n. They are located at large distances from each other, that's why the communication between them was very difficult until on the planet number 1 a hyperdrive was invented. As soon as this significant event took place, n - 1 spaceships were built on the planet number 1, and those ships were sent to other planets to inform about the revolutionary invention.

Paradoxical thought it may be, but the hyperspace is represented as simple three-dimensional Euclidean space. The inhabited planets may be considered fixed points in it, and no two points coincide and no three points lie on the same straight line. The movement of a ship with a hyperdrive between two planets is performed along a straight line at the constant speed, the same for all the ships. That's why the distance in the hyperspace are measured in hyperyears (a ship with a hyperdrive covers a distance of s hyperyears in s years).

When the ship reaches an inhabited planet, the inhabitants of the planet dissemble it, make n - 2 identical to it ships with a hyperdrive and send them to other n - 2 planets (except for the one from which the ship arrived). The time to make a new ship compared to the time in which they move from one planet to another is so small that it can be disregarded. New ships are absolutely identical to the ones sent initially: they move at the same constant speed along a straight line trajectory and, having reached a planet, perform the very same mission, i.e. are dissembled to build new n - 2 ships and send them to all the planets except for the one from which the ship arrived. Thus, the process of spreading the important news around the galaxy continues.

However the hyperdrive creators hurried to spread the news about their invention so much that they didn't study completely what goes on when two ships collide in the hyperspace. If two moving ships find themselves at one point, they provoke an explosion of colossal power, leading to the destruction of the galaxy!

Your task is to find the time the galaxy will continue to exist from the moment of the ships' launch from the first planet.

The first line contains a number n (3 ≤ n ≤ 5000) — the number of inhabited planets in the galaxy. The next n lines contain integer coordinates of the planets in format "xiyizi" ( - 104 ≤ xi, yi, zi ≤ 104).

Print the single number — the solution to the task with an absolute or relative error not exceeding 10 - 6.

## Input

The first line contains a number n (3 ≤ n ≤ 5000) — the number of inhabited planets in the galaxy. The next n lines contain integer coordinates of the planets in format "xiyizi" ( - 104 ≤ xi, yi, zi ≤ 104).

## Output

Print the single number — the solution to the task with an absolute or relative error not exceeding 10 - 6.

## Samples

```
4
0 0 0
0 0 1
0 1 0
1 0 0

```

```
1.7071067812

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-44D |
| Contest | 44 |
| Index | D |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `math` |
| 镜像标签 | `math`、`*1800` |
| Codeforces 通过次数 | 794 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/44/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/44/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P44D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

