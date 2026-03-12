# CF-79A Bus Game

## 题面快照

## Description

After Fox Ciel won an onsite round of a programming contest, she took a bus to return to her castle. The fee of the bus was 220 yen. She met Rabbit Hanako in the bus. They decided to play the following game because they got bored in the bus.

-  Initially, there is a pile that contains x 100-yen coins and y 10-yen coins.

-  They take turns alternatively. Ciel takes the first turn.

-  In each turn, they must take exactly 220 yen from the pile. In Ciel's turn, if there are multiple ways to take 220 yen, she will choose the way that contains the maximal number of 100-yen coins. In Hanako's turn, if there are multiple ways to take 220 yen, she will choose the way that contains the maximal number of 10-yen coins.

-  If Ciel or Hanako can't take exactly 220 yen from the pile, she loses.

Determine the winner of the game.

The first line contains two integers x (0 ≤ x ≤ 106) and y (0 ≤ y ≤ 106), separated by a single space.

If Ciel wins, print "Ciel". Otherwise, print "Hanako".

## Input

The first line contains two integers x (0 ≤ x ≤ 106) and y (0 ≤ y ≤ 106), separated by a single space.

## Output

If Ciel wins, print "Ciel". Otherwise, print "Hanako".

## Samples

```
2 2

```

```
Ciel

```

```
3 22

```

```
Hanako

```

## Note

In the first turn (Ciel's turn), she will choose 2 100-yen coins and 2 10-yen coins. In the second turn (Hanako's turn), she will choose 1 100-yen coin and 12 10-yen coins. In the third turn (Ciel's turn), she can't pay exactly 220 yen, so Ciel will lose.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-79A |
| Contest | 79 |
| Index | A |
| Rating | 1200 |
| Points | 500.0 |
| Codeforces 标签 | `greedy` |
| 镜像标签 | `greedy`、`*1200` |
| Codeforces 通过次数 | 4516 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/79/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/79/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P79A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

