# CF-74B Train

## 题面快照

## Description

A stowaway and a controller play the following game.

The train is represented by n wagons which are numbered with positive integers from 1 to n from the head to the tail. The stowaway and the controller are initially in some two different wagons. Every minute the train can be in one of two conditions — moving or idle. Every minute the players move.

The controller's move is as follows. The controller has the movement direction — to the train's head or to its tail. During a move the controller moves to the neighbouring wagon correspondingly to its movement direction. If at the end of his move the controller enters the 1-st or the n-th wagon, that he changes the direction of his movement into the other one. In other words, the controller cyclically goes from the train's head to its tail and back again during all the time of a game, shifting during each move by one wagon. Note, that the controller always have exactly one possible move.

The stowaway's move depends from the state of the train. If the train is moving, then the stowaway can shift to one of neighbouring wagons or he can stay where he is without moving. If the train is at a station and is idle, then the stowaway leaves the train (i.e. he is now not present in any train wagon) and then, if it is not the terminal train station, he enters the train again into any of n wagons (not necessarily into the one he's just left and not necessarily into the neighbouring one). If the train is idle for several minutes then each such minute the stowaway leaves the train and enters it back.

Let's determine the order of the players' moves. If at the given minute the train is moving, then first the stowaway moves and then the controller does. If at this minute the train is idle, then first the stowaway leaves the train, then the controller moves and then the stowaway enters the train.

If at some point in time the stowaway and the controller happen to be in one wagon, then the controller wins: he makes the stowaway pay fine. If after a while the stowaway reaches the terminal train station, then the stowaway wins: he simply leaves the station during his move and never returns there again.

At any moment of time the players know each other's positions. The players play in the optimal way. Specifically, if the controller wins, then the stowaway plays so as to lose as late as possible. As all the possible moves for the controller are determined uniquely, then he is considered to play optimally always. Determine the winner.

The first line contains three integers n, m and k. They represent the number of wagons in the train, the stowaway's and the controller's initial positions correspondingly (2 ≤ n ≤ 50, 1 ≤ m, k ≤ n, m ≠ k).

The second line contains the direction in which a controller moves. "to head" means that the controller moves to the train's head and "to tail" means that the controller moves to its tail. It is guaranteed that in the direction in which the controller is moving, there is at least one wagon. Wagon 1 is the head, and wagon n is the tail.

The third line has the length from 1 to 200 and consists of symbols "0" and "1". The i-th symbol contains information about the train's state at the i-th minute of time. "0" means that in this very minute the train moves and "1" means that the train in this very minute stands idle. The last symbol of the third line is always "1" — that's the terminal train station.

If the stowaway wins, print "Stowaway" without quotes. Otherwise, print "Controller" again without quotes, then, separated by a space, print the number of a minute, at which the stowaway will be caught.

## Input

The first line contains three integers n, m and k. They represent the number of wagons in the train, the stowaway's and the controller's initial positions correspondingly (2 ≤ n ≤ 50, 1 ≤ m, k ≤ n, m ≠ k).

The second line contains the direction in which a controller moves. "to head" means that the controller moves to the train's head and "to tail" means that the controller moves to its tail. It is guaranteed that in the direction in which the controller is moving, there is at least one wagon. Wagon 1 is the head, and wagon n is the tail.

The third line has the length from 1 to 200 and consists of symbols "0" and "1". The i-th symbol contains information about the train's state at the i-th minute of time. "0" means that in this very minute the train moves and "1" means that the train in this very minute stands idle. The last symbol of the third line is always "1" — that's the terminal train station.

## Output

If the stowaway wins, print "Stowaway" without quotes. Otherwise, print "Controller" again without quotes, then, separated by a space, print the number of a minute, at which the stowaway will be caught.

## Samples

```
5 3 2
to head
0001001

```

```
Stowaway

```

```
3 2 1
to tail
0001

```

```
Controller 2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-74B |
| Contest | 74 |
| Index | B |
| Rating | 1500 |
| Points | 1000.0 |
| Codeforces 标签 | `dp`、`games`、`greedy` |
| 镜像标签 | `dp`、`games`、`greedy`、`*1500` |
| Codeforces 通过次数 | 1719 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/74/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/74/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P74B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

