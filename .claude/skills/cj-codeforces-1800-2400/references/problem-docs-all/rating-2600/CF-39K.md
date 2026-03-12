# CF-39K Testing

## 题面快照

## Description

You take part in the testing of new weapon. For the testing a polygon was created. The polygon is a rectangular field n × m in size, divided into unit squares 1 × 1 in size. The polygon contains k objects, each of which is a rectangle with sides, parallel to the polygon sides and entirely occupying several unit squares. The objects don't intersect and don't touch each other.

The principle according to which the weapon works is highly secret. You only know that one can use it to strike any rectangular area whose area is not equal to zero with sides, parallel to the sides of the polygon. The area must completely cover some of the unit squares into which the polygon is divided and it must not touch the other squares. Of course the area mustn't cross the polygon border. Your task is as follows: you should hit no less than one and no more than three rectangular objects. Each object must either lay completely inside the area (in that case it is considered to be hit), or lay completely outside the area.

Find the number of ways of hitting.

The first line has three integers n, m и k (1 ≤ n, m ≤ 1000, 1 ≤ k ≤ 90) — the sizes of the polygon and the number of objects on it respectively. Next n lines contain m symbols each and describe the polygon. The symbol "*" stands for a square occupied an object, whereas the symbol "." stands for an empty space. The symbols "*" form exactly k rectangular connected areas that meet the requirements of the task.

Output a single number — the number of different ways to hit a target.

## Input

The first line has three integers n, m и k (1 ≤ n, m ≤ 1000, 1 ≤ k ≤ 90) — the sizes of the polygon and the number of objects on it respectively. Next n lines contain m symbols each and describe the polygon. The symbol "*" stands for a square occupied an object, whereas the symbol "." stands for an empty space. The symbols "*" form exactly k rectangular connected areas that meet the requirements of the task.

## Output

Output a single number — the number of different ways to hit a target.

## Samples

```
3 3 3
*.*
...
*..

```

```
21

```

```
4 5 4
.*.**
...**
**...
...**

```

```
38

```

```
2 2 1
.*
..

```

```
4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-39K |
| Contest | 39 |
| Index | K |
| Rating | 2600 |
| Points | - |
| Codeforces 标签 | 无 |
| 镜像标签 | `*2600` |
| Codeforces 通过次数 | 100 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/39/K)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/39/problem/K)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P39K)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

