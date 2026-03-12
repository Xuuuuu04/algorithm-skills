# CF-8B Obsession with Robots

## 题面快照

## Description

The whole world got obsessed with robots,and to keep pace with the progress, great Berland's programmer Draude decided to build his own robot. He was working hard at the robot. He taught it to walk the shortest path from one point to another, to record all its movements, but like in many Draude's programs, there was a bug — the robot didn't always walk the shortest path. Fortunately, the robot recorded its own movements correctly. Now Draude wants to find out when his robot functions wrong. Heh, if Draude only remembered the map of the field, where he tested the robot, he would easily say if the robot walked in the right direction or not. But the field map was lost never to be found, that's why he asks you to find out if there exist at least one map, where the path recorded by the robot is the shortest.

The map is an infinite checkered field, where each square is either empty, or contains an obstruction. It is also known that the robot never tries to run into the obstruction. By the recorded robot's movements find out if there exist at least one such map, that it is possible to choose for the robot a starting square (the starting square should be empty) such that when the robot moves from this square its movements coincide with the recorded ones (the robot doesn't run into anything, moving along empty squares only), and the path from the starting square to the end one is the shortest.

In one movement the robot can move into the square (providing there are no obstrutions in this square) that has common sides with the square the robot is currently in.

The first line of the input file contains the recording of the robot's movements. This recording is a non-empty string, consisting of uppercase Latin letters L, R, U and D, standing for movements left, right, up and down respectively. The length of the string does not exceed 100.

In the first line output the only word OK (if the above described map exists), or BUG (if such a map does not exist).

## Input

The first line of the input file contains the recording of the robot's movements. This recording is a non-empty string, consisting of uppercase Latin letters L, R, U and D, standing for movements left, right, up and down respectively. The length of the string does not exceed 100.

## Output

In the first line output the only word OK (if the above described map exists), or BUG (if such a map does not exist).

## Samples

```
LLUUUR

```

```
OK

```

```
RRUULLDD

```

```
BUG

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-8B |
| Contest | 8 |
| Index | B |
| Rating | 1400 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`graphs`、`implementation` |
| 镜像标签 | `constructive algorithms`、`graphs`、`implementation`、`*1400` |
| Codeforces 通过次数 | 4912 |
| 镜像尝试 / 通过 | 2 / 1 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/8/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/8/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P8B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

