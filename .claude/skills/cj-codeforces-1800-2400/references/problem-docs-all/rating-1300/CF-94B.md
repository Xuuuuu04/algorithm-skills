# CF-94B Friends

## 题面快照

## Description

One day Igor K. stopped programming and took up math. One late autumn evening he was sitting at a table reading a book and thinking about something.

The following statement caught his attention: "Among any six people there are either three pairwise acquainted people or three pairwise unacquainted people"

Igor just couldn't get why the required minimum is 6 people. "Well, that's the same for five people, too!" — he kept on repeating in his mind. — "Let's take, say, Max, Ilya, Vova — here, they all know each other! And now let's add Dima and Oleg to Vova — none of them is acquainted with each other! Now, that math is just rubbish!"

Igor K. took 5 friends of his and wrote down who of them is friends with whom. Now he wants to check whether it is true for the five people that among them there are either three pairwise acquainted or three pairwise not acquainted people.

The first line contains an integer m(0 ≤ m ≤ 10), which is the number of relations of acquaintances among the five friends of Igor's.

Each of the following m lines contains two integers ai and bi(1 ≤ ai, bi ≤ 5;ai ≠ bi), where (ai, bi) is a pair of acquainted people. It is guaranteed that each pair of the acquaintances is described exactly once. The acquaintance relation is symmetrical, i.e. if x is acquainted with y, then y is also acquainted with x.

Print "FAIL", if among those five people there are no either three pairwise acquainted or three pairwise unacquainted people. Otherwise print "WIN".

## Input

The first line contains an integer m(0 ≤ m ≤ 10), which is the number of relations of acquaintances among the five friends of Igor's.

Each of the following m lines contains two integers ai and bi(1 ≤ ai, bi ≤ 5;ai ≠ bi), where (ai, bi) is a pair of acquainted people. It is guaranteed that each pair of the acquaintances is described exactly once. The acquaintance relation is symmetrical, i.e. if x is acquainted with y, then y is also acquainted with x.

## Output

Print "FAIL", if among those five people there are no either three pairwise acquainted or three pairwise unacquainted people. Otherwise print "WIN".

## Samples

```
4
1 3
2 3
1 4
5 3

```

```
WIN

```

```
5
1 2
2 3
3 4
4 5
5 1

```

```
FAIL

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-94B |
| Contest | 94 |
| Index | B |
| Rating | 1300 |
| Points | 1000.0 |
| Codeforces 标签 | `graphs`、`implementation`、`math` |
| 镜像标签 | `graphs`、`implementation`、`math`、`*1300` |
| Codeforces 通过次数 | 5340 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/94/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/94/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P94B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

