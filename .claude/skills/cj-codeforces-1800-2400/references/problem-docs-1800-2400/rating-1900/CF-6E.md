# CF-6E Exposition

## 题面快照

## Description

There are several days left before the fiftieth birthday of a famous Berland's writer Berlbury. In this connection the local library decided to make an exposition of the works of this famous science-fiction writer. It was decided as well that it is necessary to include into the exposition only those books that were published during a particular time period. It is obvious that if the books differ much in size, the visitors will not like it. That was why the organizers came to the opinion, that the difference between the highest and the lowest books in the exposition should be not more than k millimeters.

The library has n volumes of books by Berlbury, arranged in chronological order of their appearance. The height of each book in millimeters is know, it is hi. As Berlbury is highly respected in the city, the organizers want to include into the exposition as many books as possible, and to find out what periods of his creative work they will manage to cover. You are asked to help the organizers cope with this hard task.

The first line of the input data contains two integer numbers separated by a space n (1 ≤ n ≤ 105) and k (0 ≤ k ≤ 106) — the amount of books by Berlbury in the library, and the maximum allowed height difference between the lowest and the highest books. The second line contains n integer numbers separated by a space. Each number hi (1 ≤ hi ≤ 106) is the height of the i-th book in millimeters.

In the first line of the output data print two numbers a and b (separate them by a space), where a is the maximum amount of books the organizers can include into the exposition, and b — the amount of the time periods, during which Berlbury published a books, and the height difference between the lowest and the highest among these books is not more than k milllimeters.

In each of the following b lines print two integer numbers separated by a space — indexes of the first and the last volumes from each of the required time periods of Berlbury's creative work.

## Input

The first line of the input data contains two integer numbers separated by a space n (1 ≤ n ≤ 105) and k (0 ≤ k ≤ 106) — the amount of books by Berlbury in the library, and the maximum allowed height difference between the lowest and the highest books. The second line contains n integer numbers separated by a space. Each number hi (1 ≤ hi ≤ 106) is the height of the i-th book in millimeters.

## Output

In the first line of the output data print two numbers a and b (separate them by a space), where a is the maximum amount of books the organizers can include into the exposition, and b — the amount of the time periods, during which Berlbury published a books, and the height difference between the lowest and the highest among these books is not more than k milllimeters.

In each of the following b lines print two integer numbers separated by a space — indexes of the first and the last volumes from each of the required time periods of Berlbury's creative work.

## Samples

```
3 3
14 12 10

```

```
2 2
1 2
2 3

```

```
2 0
10 10

```

```
2 1
1 2

```

```
4 5
8 19 10 13

```

```
2 1
3 4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-6E |
| Contest | 6 |
| Index | E |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `binary search`、`data structures`、`dsu`、`trees`、`two pointers` |
| 镜像标签 | `binary search`、`data structures`、`dsu`、`trees`、`two pointers`、`*1900` |
| Codeforces 通过次数 | 3742 |
| 镜像尝试 / 通过 | 8 / 1 |
| 时限 | 1000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/6/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/6/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P6E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

