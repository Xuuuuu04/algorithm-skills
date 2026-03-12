# CF-79B Colorful Field

## 题面快照

## Description

Fox Ciel saw a large field while she was on a bus. The field was a n × m rectangle divided into 1 × 1 cells. Some cells were wasteland, and other each cell contained crop plants: either carrots or kiwis or grapes.

After seeing the field carefully, Ciel found that the crop plants of each cell were planted in following procedure:

-  Assume that the rows are numbered 1 to n from top to bottom and the columns are numbered 1 to m from left to right, and a cell in row i and column j is represented as (i, j).

-  First, each field is either cultivated or waste. Crop plants will be planted in the cultivated cells in the order of (1, 1) → ... → (1, m) → (2, 1) → ... → (2, m) → ... → (n, 1) → ... → (n, m). Waste cells will be ignored.

-  Crop plants (either carrots or kiwis or grapes) will be planted in each cell one after another cyclically. Carrots will be planted in the first cell, then kiwis in the second one, grapes in the third one, carrots in the forth one, kiwis in the fifth one, and so on.

The following figure will show you the example of this procedure. Here, a white square represents a cultivated cell, and a black square represents a waste cell.

Now she is wondering how to determine the crop plants in some certain cells.

In the first line there are four positive integers n, m, k, t (1 ≤ n ≤ 4·104, 1 ≤ m ≤ 4·104, 1 ≤ k ≤ 103, 1 ≤ t ≤ 103), each of which represents the height of the field, the width of the field, the number of waste cells and the number of queries that ask the kind of crop plants in a certain cell.

Following each k lines contains two integers a, b (1 ≤ a ≤ n, 1 ≤ b ≤ m), which denotes a cell (a, b) is waste. It is guaranteed that the same cell will not appear twice in this section.

Following each t lines contains two integers i, j (1 ≤ i ≤ n, 1 ≤ j ≤ m), which is a query that asks you the kind of crop plants of a cell (i, j).

For each query, if the cell is waste, print Waste. Otherwise, print the name of crop plants in the cell: either Carrots or Kiwis or Grapes.

## Input

In the first line there are four positive integers n, m, k, t (1 ≤ n ≤ 4·104, 1 ≤ m ≤ 4·104, 1 ≤ k ≤ 103, 1 ≤ t ≤ 103), each of which represents the height of the field, the width of the field, the number of waste cells and the number of queries that ask the kind of crop plants in a certain cell.

Following each k lines contains two integers a, b (1 ≤ a ≤ n, 1 ≤ b ≤ m), which denotes a cell (a, b) is waste. It is guaranteed that the same cell will not appear twice in this section.

Following each t lines contains two integers i, j (1 ≤ i ≤ n, 1 ≤ j ≤ m), which is a query that asks you the kind of crop plants of a cell (i, j).

## Output

For each query, if the cell is waste, print Waste. Otherwise, print the name of crop plants in the cell: either Carrots or Kiwis or Grapes.

## Samples

```
4 5 5 6
4 3
1 3
3 3
2 5
3 2
1 3
1 4
2 3
2 4
1 1
1 1

```

```
Waste
Grapes
Carrots
Kiwis
Carrots
Carrots

```

## Note

The sample corresponds to the figure in the statement.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-79B |
| Contest | 79 |
| Index | B |
| Rating | 1400 |
| Points | 1000.0 |
| Codeforces 标签 | `implementation`、`sortings` |
| 镜像标签 | `implementation`、`sortings`、`*1400` |
| Codeforces 通过次数 | 7934 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/79/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/79/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P79B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

