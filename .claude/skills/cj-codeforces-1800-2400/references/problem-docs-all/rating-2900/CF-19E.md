# CF-19E Fairy

## 题面快照

## Description

Once upon a time there lived a good fairy A. One day a fine young man B came to her and asked to predict his future. The fairy looked into her magic ball and said that soon the fine young man will meet the most beautiful princess ever and will marry her. Then she drew on a sheet of paper n points and joined some of them with segments, each of the segments starts in some point and ends in some other point. Having drawn that picture, she asked the young man to erase one of the segments from the sheet. Then she tries to colour each point red or blue so, that there is no segment having points of the same colour as its ends. If she manages to do so, the prediction will come true. B wants to meet the most beautiful princess, that's why he asks you to help him. Find all the segments that will help him to meet the princess.

The first input line contains two integer numbers: n — amount of the drawn points and m — amount of the drawn segments (1 ≤ n ≤ 104, 0 ≤ m ≤ 104). The following m lines contain the descriptions of the segments. Each description contains two different space-separated integer numbers v, u (1 ≤ v ≤ n, 1 ≤ u ≤ n) — indexes of the points, joined by this segment. No segment is met in the description twice.

In the first line output number k — amount of the segments in the answer. In the second line output k space-separated numbers — indexes of these segments in ascending order. Each index should be output only once. Segments are numbered from 1 in the input order.

## Input

The first input line contains two integer numbers: n — amount of the drawn points and m — amount of the drawn segments (1 ≤ n ≤ 104, 0 ≤ m ≤ 104). The following m lines contain the descriptions of the segments. Each description contains two different space-separated integer numbers v, u (1 ≤ v ≤ n, 1 ≤ u ≤ n) — indexes of the points, joined by this segment. No segment is met in the description twice.

## Output

In the first line output number k — amount of the segments in the answer. In the second line output k space-separated numbers — indexes of these segments in ascending order. Each index should be output only once. Segments are numbered from 1 in the input order.

## Samples

```
4 4
1 2
1 3
2 4
3 4

```

```
4
1 2 3 4

```

```
4 5
1 2
2 3
3 4
4 1
1 3

```

```
1
5

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-19E |
| Contest | 19 |
| Index | E |
| Rating | 2900 |
| Points | - |
| Codeforces 标签 | `dfs and similar`、`divide and conquer`、`dsu` |
| 镜像标签 | `dfs and similar`、`divide and conquer`、`dsu`、`*2900` |
| Codeforces 通过次数 | 2464 |
| 镜像尝试 / 通过 | 4 / 3 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/19/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/19/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P19E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

