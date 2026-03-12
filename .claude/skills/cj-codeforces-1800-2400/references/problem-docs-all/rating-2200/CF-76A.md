# CF-76A Gift

## 题面快照

## Description

The kingdom of Olympia consists of N cities and M bidirectional roads. Each road connects exactly two cities and two cities can be connected with more than one road. Also it possible that some roads connect city with itself making a loop.

All roads are constantly plundered with bandits. After a while bandits became bored of wasting time in road robberies, so they suggested the king of Olympia to pay off. According to the offer, bandits want to get a gift consisted of gold and silver coins. Offer also contains a list of restrictions: for each road it is known gi — the smallest amount of gold and si — the smallest amount of silver coins that should be in the gift to stop robberies on the road. That is, if the gift contains a gold and b silver coins, then bandits will stop robberies on all the roads that gi ≤ a and si ≤ b.

Unfortunately kingdom treasury doesn't contain neither gold nor silver coins, but there are Olympian tugriks in it. The cost of one gold coin in tugriks is G, and the cost of one silver coin in tugriks is S. King really wants to send bandits such gift that for any two cities there will exist a safe path between them. Your task is to find the minimal cost in Olympian tugriks of the required gift.

The first line of the input contains two integers N and M (2 ≤ N ≤ 200, 1 ≤ M ≤ 50 000) — the number of cities and the number of roads, respectively. The second line contains two integers G and S (1 ≤ G, S ≤ 109) — the prices of gold and silver coins in tugriks. The following M lines contain information about the offer. Each of the records in list is given as four integers xi, yi, gi, si, where xi and yi are the numbers of cities that the road connects and gi, si are minimal gold and silver coins requirements for the i-th road (1 ≤ xi, yi ≤ N, 1 ≤ gi, si ≤ 109). Cities are numbered from 1 to N. It is possible that there are more than one road between a pair of cities. It is possible that a road connects the city with itself.

The output should contain the minimal cost of the gift in Olympian tugriks. If there is no gift that satisfies the given requirements output .

## Input

The first line of the input contains two integers N and M (2 ≤ N ≤ 200, 1 ≤ M ≤ 50 000) — the number of cities and the number of roads, respectively. The second line contains two integers G and S (1 ≤ G, S ≤ 109) — the prices of gold and silver coins in tugriks. The following M lines contain information about the offer. Each of the records in list is given as four integers xi, yi, gi, si, where xi and yi are the numbers of cities that the road connects and gi, si are minimal gold and silver coins requirements for the i-th road (1 ≤ xi, yi ≤ N, 1 ≤ gi, si ≤ 109). Cities are numbered from 1 to N. It is possible that there are more than one road between a pair of cities. It is possible that a road connects the city with itself.

## Output

The output should contain the minimal cost of the gift in Olympian tugriks. If there is no gift that satisfies the given requirements output .

## Samples

```
3 3
2 1
1 2 10 15
1 2 4 20
1 3 5 1

```

```
30

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-76A |
| Contest | 76 |
| Index | A |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `dsu`、`graphs`、`sortings`、`trees` |
| 镜像标签 | `dsu`、`graphs`、`sortings`、`trees`、`*2200` |
| Codeforces 通过次数 | 2075 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/76/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/76/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P76A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

