# CF-28D Don't fear, DravDe is kind

## 题面快照

## Description

A motorcade of n trucks, driving from city «Z» to city «З», has approached a tunnel, known as Tunnel of Horror. Among truck drivers there were rumours about monster DravDe, who hunts for drivers in that tunnel. Some drivers fear to go first, others - to be the last, but let's consider the general case. Each truck is described with four numbers:

- v — value of the truck, of its passangers and cargo

- c — amount of passanger on the truck, the driver included

- l — total amount of people that should go into the tunnel before this truck, so that the driver can overcome his fear («if the monster appears in front of the motorcade, he'll eat them first»)

- r — total amount of people that should follow this truck, so that the driver can overcome his fear («if the monster appears behind the motorcade, he'll eat them first»).

Since the road is narrow, it's impossible to escape DravDe, if he appears from one side. Moreover, the motorcade can't be rearranged. The order of the trucks can't be changed, but it's possible to take any truck out of the motorcade, and leave it near the tunnel for an indefinite period. You, as the head of the motorcade, should remove some of the trucks so, that the rest of the motorcade can move into the tunnel and the total amount of the left trucks' values is maximal.

The first input line contains integer number n (1 ≤ n ≤ 105) — amount of trucks in the motorcade. The following n lines contain four integers each. Numbers in the i-th line: vi, ci, li, ri (1 ≤ vi ≤ 104, 1 ≤ ci ≤ 105, 0 ≤ li, ri ≤ 105) — describe the i-th truck. The trucks are numbered from 1, counting from the front of the motorcade.

In the first line output number k — amount of trucks that will drive into the tunnel. In the second line output k numbers — indexes of these trucks in ascending order. Don't forget please that you are not allowed to change the order of trucks. If the answer is not unique, output any.

## Input

The first input line contains integer number n (1 ≤ n ≤ 105) — amount of trucks in the motorcade. The following n lines contain four integers each. Numbers in the i-th line: vi, ci, li, ri (1 ≤ vi ≤ 104, 1 ≤ ci ≤ 105, 0 ≤ li, ri ≤ 105) — describe the i-th truck. The trucks are numbered from 1, counting from the front of the motorcade.

## Output

In the first line output number k — amount of trucks that will drive into the tunnel. In the second line output k numbers — indexes of these trucks in ascending order. Don't forget please that you are not allowed to change the order of trucks. If the answer is not unique, output any.

## Samples

```
5
1 1 0 3
1 1 1 2
1 1 2 1
1 1 3 0
2 1 3 0

```

```
4
1 2 3 5

```

```
5
1 1 0 3
10 1 2 1
2 2 1 1
10 1 1 2
3 1 3 0

```

```
3
1 3 5

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-28D |
| Contest | 28 |
| Index | D |
| Rating | 2400 |
| Points | 2000.0 |
| Codeforces 标签 | `binary search`、`data structures`、`dp`、`hashing` |
| 镜像标签 | `binary search`、`data structures`、`dp`、`hashing`、`*2400` |
| Codeforces 通过次数 | 671 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/28/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/28/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P28D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

