# CF-34A Reconnaissance 2

## 题面快照

## Description

n soldiers stand in a circle. For each soldier his height ai is known. A reconnaissance unit can be made of such two neighbouring soldiers, whose heights difference is minimal, i.e. |ai - aj| is minimal. So each of them will be less noticeable with the other. Output any pair of soldiers that can form a reconnaissance unit.

The first line contains integer n (2 ≤ n ≤ 100) — amount of soldiers. Then follow the heights of the soldiers in their order in the circle — n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 1000). The soldier heights are given in clockwise or counterclockwise direction.

Output two integers — indexes of neighbouring soldiers, who should form a reconnaissance unit. If there are many optimum solutions, output any of them. Remember, that the soldiers stand in a circle.

## Input

The first line contains integer n (2 ≤ n ≤ 100) — amount of soldiers. Then follow the heights of the soldiers in their order in the circle — n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 1000). The soldier heights are given in clockwise or counterclockwise direction.

## Output

Output two integers — indexes of neighbouring soldiers, who should form a reconnaissance unit. If there are many optimum solutions, output any of them. Remember, that the soldiers stand in a circle.

## Samples

```
5
10 12 13 15 10

```

```
5 1

```

```
4
10 20 30 40

```

```
1 2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-34A |
| Contest | 34 |
| Index | A |
| Rating | 800 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*800` |
| Codeforces 通过次数 | 34280 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/34/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/34/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P34A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

