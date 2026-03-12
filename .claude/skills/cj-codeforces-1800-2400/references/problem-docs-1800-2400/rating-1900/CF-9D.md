# CF-9D How many trees?

## 题面快照

## Description

In one very old text file there was written Great Wisdom. This Wisdom was so Great that nobody could decipher it, even Phong — the oldest among the inhabitants of Mainframe. But still he managed to get some information from there. For example, he managed to learn that User launches games for pleasure — and then terrible Game Cubes fall down on the city, bringing death to those modules, who cannot win the game...

For sure, as guard Bob appeared in Mainframe many modules stopped fearing Game Cubes. Because Bob (as he is alive yet) has never been defeated by User, and he always meddles with Game Cubes, because he is programmed to this.

However, unpleasant situations can happen, when a Game Cube falls down on Lost Angles. Because there lives a nasty virus — Hexadecimal, who is... mmm... very strange. And she likes to play very much. So, willy-nilly, Bob has to play with her first, and then with User.

This time Hexadecimal invented the following entertainment: Bob has to leap over binary search trees with n nodes. We should remind you that a binary search tree is a binary tree, each node has a distinct key, for each node the following is true: the left sub-tree of a node contains only nodes with keys less than the node's key, the right sub-tree of a node contains only nodes with keys greater than the node's key. All the keys are different positive integer numbers from 1 to n. Each node of such a tree can have up to two children, or have no children at all (in the case when a node is a leaf).

In Hexadecimal's game all the trees are different, but the height of each is not lower than h. In this problem «height» stands for the maximum amount of nodes on the way from the root to the remotest leaf, the root node and the leaf itself included. When Bob leaps over a tree, it disappears. Bob gets the access to a Cube, when there are no trees left. He knows how many trees he will have to leap over in the worst case. And you?

The input data contains two space-separated positive integer numbers n and h (n ≤ 35, h ≤ n).

Output one number — the answer to the problem. It is guaranteed that it does not exceed 9·1018.

## Input

The input data contains two space-separated positive integer numbers n and h (n ≤ 35, h ≤ n).

## Output

Output one number — the answer to the problem. It is guaranteed that it does not exceed 9·1018.

## Samples

```
3 2

```

```
5

```

```
3 3

```

```
4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-9D |
| Contest | 9 |
| Index | D |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `combinatorics`、`divide and conquer`、`dp` |
| 镜像标签 | `combinatorics`、`divide and conquer`、`dp`、`*1900` |
| Codeforces 通过次数 | 4446 |
| 镜像尝试 / 通过 | 2 / 2 |
| 时限 | 1000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/9/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/9/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P9D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

