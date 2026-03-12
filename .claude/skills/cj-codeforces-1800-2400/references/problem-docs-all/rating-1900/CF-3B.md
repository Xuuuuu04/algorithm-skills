# CF-3B Lorry

## 题面快照

## Description

A group of tourists is going to kayak and catamaran tour. A rented lorry has arrived to the boat depot to take kayaks and catamarans to the point of departure. It's known that all kayaks are of the same size (and each of them occupies the space of 1 cubic metre), and all catamarans are of the same size, but two times bigger than kayaks (and occupy the space of 2 cubic metres).

Each waterborne vehicle has a particular carrying capacity, and it should be noted that waterborne vehicles that look the same can have different carrying capacities. Knowing the truck body volume and the list of waterborne vehicles in the boat depot (for each one its type and carrying capacity are known), find out such set of vehicles that can be taken in the lorry, and that has the maximum total carrying capacity. The truck body volume of the lorry can be used effectively, that is to say you can always put into the lorry a waterborne vehicle that occupies the space not exceeding the free space left in the truck body.

The first line contains a pair of integer numbers n and v (1 ≤ n ≤ 105; 1 ≤ v ≤ 109), where n is the number of waterborne vehicles in the boat depot, and v is the truck body volume of the lorry in cubic metres. The following n lines contain the information about the waterborne vehicles, that is a pair of numbers ti, pi (1 ≤ ti ≤ 2; 1 ≤ pi ≤ 104), where ti is the vehicle type (1 – a kayak, 2 – a catamaran), and pi is its carrying capacity. The waterborne vehicles are enumerated in order of their appearance in the input file.

In the first line print the maximum possible carrying capacity of the set. In the second line print a string consisting of the numbers of the vehicles that make the optimal set. If the answer is not unique, print any of them.

## Input

The first line contains a pair of integer numbers n and v (1 ≤ n ≤ 105; 1 ≤ v ≤ 109), where n is the number of waterborne vehicles in the boat depot, and v is the truck body volume of the lorry in cubic metres. The following n lines contain the information about the waterborne vehicles, that is a pair of numbers ti, pi (1 ≤ ti ≤ 2; 1 ≤ pi ≤ 104), where ti is the vehicle type (1 – a kayak, 2 – a catamaran), and pi is its carrying capacity. The waterborne vehicles are enumerated in order of their appearance in the input file.

## Output

In the first line print the maximum possible carrying capacity of the set. In the second line print a string consisting of the numbers of the vehicles that make the optimal set. If the answer is not unique, print any of them.

## Samples

```
3 2
1 2
2 7
1 3

```

```
7
2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-3B |
| Contest | 3 |
| Index | B |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `greedy`、`sortings` |
| 镜像标签 | `greedy`、`sortings`、`*1900` |
| Codeforces 通过次数 | 5151 |
| 镜像尝试 / 通过 | 5 / 2 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/3/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/3/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P3B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

