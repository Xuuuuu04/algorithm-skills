# CF-38F Smart Boy

## 题面快照

## Description

Once Petya and Vasya invented a new game and called it "Smart Boy". They located a certain set of words — the dictionary — for the game. It is admissible for the dictionary to contain similar words.

The rules of the game are as follows: first the first player chooses any letter (a word as long as 1) from any word from the dictionary and writes it down on a piece of paper. The second player adds some other letter to this one's initial or final position, thus making a word as long as 2, then it's the first player's turn again, he adds a letter in the beginning or in the end thus making a word as long as 3 and so on. But the player mustn't break one condition: the newly created word must be a substring of a word from a dictionary. The player who can't add a letter to the current word without breaking the condition loses.

Also if by the end of a turn a certain string s is written on paper, then the player, whose turn it just has been, gets a number of points according to the formula:

where

-  is a sequence number of symbol c in Latin alphabet, numbered starting from 1. For example, , and .

-  is the number of words from the dictionary where the line s occurs as a substring at least once.

Your task is to learn who will win the game and what the final score will be. Every player plays optimally and most of all tries to win, then — to maximize the number of his points, then — to minimize the number of the points of the opponent.

The first input line contains an integer n which is the number of words in the located dictionary (1 ≤ n ≤ 30). The n lines contain the words from the dictionary — one word is written on one line. Those lines are nonempty, consisting of Latin lower-case characters no longer than 30 characters. Equal words can be in the list of words.

On the first output line print a line "First" or "Second" which means who will win the game. On the second line output the number of points of the first player and the number of points of the second player after the game ends. Separate the numbers by a single space.

## Input

The first input line contains an integer n which is the number of words in the located dictionary (1 ≤ n ≤ 30). The n lines contain the words from the dictionary — one word is written on one line. Those lines are nonempty, consisting of Latin lower-case characters no longer than 30 characters. Equal words can be in the list of words.

## Output

On the first output line print a line "First" or "Second" which means who will win the game. On the second line output the number of points of the first player and the number of points of the second player after the game ends. Separate the numbers by a single space.

## Samples

```
2
aba
abac

```

```
Second
29 35

```

```
3
artem
nik
max

```

```
First
2403 1882

```

-  登录后递交

-

-  讨论 (0)

-  题解 (0)

-  文件

-  统计

-

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-38F |
| Contest | 38 |
| Index | F |
| Rating | 2100 |
| Points | - |
| Codeforces 标签 | `dp`、`games`、`strings` |
| 镜像标签 | `dp`、`games`、`strings`、`*2100` |
| Codeforces 通过次数 | 440 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 4000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/38/F)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/38/problem/F)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P38F)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

