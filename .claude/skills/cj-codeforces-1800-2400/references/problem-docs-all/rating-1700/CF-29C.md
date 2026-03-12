# CF-29C Mail Stamps

## 题面快照

## Description

One day Bob got a letter in an envelope. Bob knows that when Berland's post officers send a letter directly from city «A» to city «B», they stamp it with «A B», or «B A». Unfortunately, often it is impossible to send a letter directly from the city of the sender to the city of the receiver, that's why the letter is sent via some intermediate cities. Post officers never send a letter in such a way that the route of this letter contains some city more than once. Bob is sure that the post officers stamp the letters accurately.

There are n stamps on the envelope of Bob's letter. He understands that the possible routes of this letter are only two. But the stamps are numerous, and Bob can't determine himself none of these routes. That's why he asks you to help him. Find one of the possible routes of the letter.

The first line contains integer n (1 ≤ n ≤ 105) — amount of mail stamps on the envelope. Then there follow n lines with two integers each — description of the stamps. Each stamp is described with indexes of the cities between which a letter is sent. The indexes of cities are integers from 1 to 109. Indexes of all the cities are different. Every time the letter is sent from one city to another, exactly one stamp is put on the envelope. It is guaranteed that the given stamps correspond to some valid route from some city to some other city.

Output n + 1 numbers — indexes of cities in one of the two possible routes of the letter.

## Input

The first line contains integer n (1 ≤ n ≤ 105) — amount of mail stamps on the envelope. Then there follow n lines with two integers each — description of the stamps. Each stamp is described with indexes of the cities between which a letter is sent. The indexes of cities are integers from 1 to 109. Indexes of all the cities are different. Every time the letter is sent from one city to another, exactly one stamp is put on the envelope. It is guaranteed that the given stamps correspond to some valid route from some city to some other city.

## Output

Output n + 1 numbers — indexes of cities in one of the two possible routes of the letter.

## Samples

```
2
1 100
100 2

```

```
2 100 1

```

```
3
3 1
100 2
3 2

```

```
100 2 3 1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-29C |
| Contest | 29 |
| Index | C |
| Rating | 1700 |
| Points | 1500.0 |
| Codeforces 标签 | `data structures`、`dfs and similar`、`graphs`、`implementation` |
| 镜像标签 | `data structures`、`dfs and similar`、`graphs`、`implementation`、`*1700` |
| Codeforces 通过次数 | 6229 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/29/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/29/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P29C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

