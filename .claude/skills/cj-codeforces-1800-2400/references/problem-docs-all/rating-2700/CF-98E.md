# CF-98E Help Shrek and Donkey

## 题面快照

## Description

Shrek and the Donkey (as you can guess, they also live in the far away kingdom) decided to play a card game called YAGame. The rules are very simple: initially Shrek holds m cards and the Donkey holds n cards (the players do not see each other's cards), and one more card lies on the table face down so that both players cannot see it as well. Thus, at the beginning of the game there are overall m + n + 1 cards. Besides, the players know which cards the pack of cards consists of and their own cards (but they do not know which card lies on the table and which ones the other player has). The players move in turn and Shrek starts. During a move a player can:

-  Try to guess which card is lying on the table. If he guesses correctly, the game ends and he wins. If his guess is wrong, the game also ends but this time the other player wins.

-  Name any card from the pack. If the other player has such card, he must show it and put it aside (so that this card is no longer used in the game). If the other player doesn't have such card, he says about that.
Recently Donkey started taking some yellow pills and winning over Shrek. Now Shrek wants to evaluate his chances to win if he too starts taking the pills.
Help Shrek assuming the pills are good in quality and that both players using them start playing in the optimal manner.

The first line contains space-separated integers m and n (0 ≤ m, n ≤ 1000).

Print space-separated probabilities that Shrek wins and Donkey wins correspondingly; the absolute error should not exceed 10 - 9.

## Input

The first line contains space-separated integers m and n (0 ≤ m, n ≤ 1000).

## Output

Print space-separated probabilities that Shrek wins and Donkey wins correspondingly; the absolute error should not exceed 10 - 9.

## Samples

```
0 3

```

```
0.25 0.75

```

```
1 0

```

```
1 0

```

```
1 1

```

```
0.5 0.5

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-98E |
| Contest | 98 |
| Index | E |
| Rating | 2700 |
| Points | 2500.0 |
| Codeforces 标签 | `dp`、`games`、`math`、`probabilities` |
| 镜像标签 | `dp`、`games`、`math`、`probabilities`、`*2700` |
| Codeforces 通过次数 | 557 |
| 镜像尝试 / 通过 | 6 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/98/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/98/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P98E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

