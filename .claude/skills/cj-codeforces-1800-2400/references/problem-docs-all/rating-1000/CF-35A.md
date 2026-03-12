# CF-35A Shell Game

## 题面快照

## Description

Today the «Z» city residents enjoy a shell game competition. The residents are gathered on the main square to watch the breath-taking performance. The performer puts 3 non-transparent cups upside down in a row. Then he openly puts a small ball under one of the cups and starts to shuffle the cups around very quickly so that on the whole he makes exactly 3 shuffles. After that the spectators have exactly one attempt to guess in which cup they think the ball is and if the answer is correct they get a prize. Maybe you can try to find the ball too?

The first input line contains an integer from 1 to 3 — index of the cup which covers the ball before the shuffles. The following three lines describe the shuffles. Each description of a shuffle contains two distinct integers from 1 to 3 — indexes of the cups which the performer shuffled this time. The cups are numbered from left to right and are renumbered after each shuffle from left to right again. In other words, the cup on the left always has index 1, the one in the middle — index 2 and the one on the right — index 3.

In the first line output an integer from 1 to 3 — index of the cup which will have the ball after all the shuffles.

## Input

The first input line contains an integer from 1 to 3 — index of the cup which covers the ball before the shuffles. The following three lines describe the shuffles. Each description of a shuffle contains two distinct integers from 1 to 3 — indexes of the cups which the performer shuffled this time. The cups are numbered from left to right and are renumbered after each shuffle from left to right again. In other words, the cup on the left always has index 1, the one in the middle — index 2 and the one on the right — index 3.

## Output

In the first line output an integer from 1 to 3 — index of the cup which will have the ball after all the shuffles.

## Samples

```
1
1 2
2 1
2 1

```

```
2

```

```
1
2 1
3 1
1 3

```

```
2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-35A |
| Contest | 35 |
| Index | A |
| Rating | 1000 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1000` |
| Codeforces 通过次数 | 7525 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/35/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/35/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P35A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

